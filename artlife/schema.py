import graphene
import api.schema

schema = graphene.Schema(query=api.schema.Query ) # , mutation=api.schema.Mutation)
