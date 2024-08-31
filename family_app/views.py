from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from family_app.serializer import MemberSerializer
from family_app.models import MemberRelationshipModel,MemberModel


def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start], 1
    queue = [(start, [start], 0)]
    visited = set()

    while queue:
        node, path, edge = queue.pop(0)
        if node == end:
            return path, edge

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], edge + 1))

    return None, 0




@api_view(['POST'])
def add_member(request):
    serializer = MemberSerializer(data=request.data,many= True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_relationship(request):
    try:
        request_body = request.data
        member_1_id = MemberModel.objects.get(name = request_body["member1"]).id
        member_2_id = MemberModel.objects.get(name = request_body["member2"]).id
        MemberRelationshipModel.objects.create(
            member1_id = member_1_id,
            member2_id = member_2_id,
            relation_type = request_body["relation"]
        )

        return Response({"message":"success"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        
        return Response({"messaage":str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def find_shortest_path(request):
    try:
        start_member_name = request.query_params.get('start')
        end_member_name = request.query_params.get('end')

        start_member = MemberModel.objects.filter(name=start_member_name).first()
        end_member = MemberModel.objects.filter(name=end_member_name).first()

        if not start_member or not end_member:
            return Response({"error": "Members not found"}, status=status.HTTP_400_BAD_REQUEST)

        graph = {}
        relationships = MemberRelationshipModel.objects.all()

        for relationship in relationships:
            if relationship.member1.name not in graph:
                graph[relationship.member1.name] = []
            if relationship.member2.name not in graph:
                graph[relationship.member2.name] = []
            
            graph[relationship.member1.name].append((relationship.member2.name))
            graph[relationship.member2.name].append((relationship.member1.name))

    
        path, edge_count = bfs_shortest_path(graph, start_member.name, end_member.name)
        
        if path:
            return Response({"path": path, "edge_count": edge_count})
        return Response({"error": "No path found"}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        