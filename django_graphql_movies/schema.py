import graphene
import django_graphql_movies.movies.schema

class Query(django_graphql_movies.movies.schema.Query, graphene.ObjectType):
    pass

class Mutation(django_graphql_movies.movies.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)