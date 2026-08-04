GET_LISTS = """
query myCreatedFavoriteList($currentQuestionSlug: String) {
  myCreatedFavoriteList(currentQuestionSlug: $currentQuestionSlug) {
    favorites {
      name
      slug
    }
  }
}
"""

CREATE_LIST = """
mutation AddQuestionToNewFavoriteV2(
    $name: String!,
    $isPublicFavorite: Boolean!,
    $questionSlug: String!
){
  addQuestionToNewFavoriteV2(
    name: $name,
    isPublicFavorite: $isPublicFavorite,
    questionSlug: $questionSlug
  ){
    ok
    error
    slug
  }
}
"""

ADD_QUESTION = """
mutation addQuestionToFavoriteV2(
    $favoriteSlug: String!,
    $questionSlug: String!
){
  addQuestionToFavoriteV2(
    favoriteSlug: $favoriteSlug,
    questionSlug: $questionSlug
  ){
    ok
    error
  }
}
"""