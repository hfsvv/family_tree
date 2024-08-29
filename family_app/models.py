from django.db import models
from family_app.enums import RelationTypes
# Create your models here.



class TimestampedModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
    
class MemberModel(TimestampedModel):
    name = models.CharField(max_length = 100 , unique=True , null=False )
    
    class Meta:
        db_table = "members"
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        
class MemberRelationshipModel(TimestampedModel):
    
    member1 = models.ForeignKey(MemberModel, related_name= 'relation_from' , on_delete= models.CASCADE)
    member2 = models.ForeignKey(MemberModel, related_name= 'relation_to' , on_delete= models.CASCADE)
    relation_type = models.SmallIntegerField(null=False,choices=RelationTypes.choices())
    
    class Meta:
        db_table = "member_relations"
        verbose_name = 'Member Relations'
        verbose_name_plural = verbose_name
        unique_together = ('member1', 'member2',)

        
    
    def __str__(self):
        return f"{self.member1.name} - {RelationTypes(self.relation_type).name} - {self.member2.name}"
    