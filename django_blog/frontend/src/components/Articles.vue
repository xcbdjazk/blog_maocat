<template>
  <div class="articles">
    <p v-for="(article, index) in articles" :key="index">
      {{ article.id }}
      {{ article.title }}
      {{ article.desc_txt }}
    </p>
  </div>
</template>

<script>
  import {getArticles} from '../api/article'

  export default {
    name: 'Articles',
    data() {
      return {
        articles: []
      }
    },
    created() {
      getArticles().then((data) => {
        this.articles = data
      })
    }


  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
