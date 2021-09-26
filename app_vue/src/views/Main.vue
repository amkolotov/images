<template>

  <main class="flex-shrink-0">

    <div class="container-fluid">
      <div class="row justify-content-center mt-5">
        <div class="col-lg-6">
          <form class="d-flex" action="#">
            <input class="form-control" type="file" id="formFile">
            <button class="btn btn-secondary pl-2" type="button" @click="saveImage">Сохранить</button>
          </form>
        </div>
      </div>

      <div v-for="image in listImages" :key="image.id" class="row justify-content-between">

        <div class="col-xxl-3 col-xl-6 align-self-center text-center my-5">
          <div>
            <img :src="image.image.first_size_crop" alt="">
          </div>
        </div>

        <div class="col-xxl-3 col-xl-6 align-self-center text-center my-5"><a :href="image.image.first_size_thum"
                                                                              download><img
            :src="image.image.first_size_thum" alt=""></a></div>

        <div class="col align-self-center text-center my-5"><a :href="image.image.second_size_crop" download><img
            :src="image.image.second_size_crop" alt=""></a></div>
        <div class="col align-self-center text-center my-5"><a :href="image.image.second_size_thum" download><img
            :src="image.image.second_size_thum" alt=""></a></div>

        <div class="col align-self-center text-center my-5"><a :href="image.image.third_size_crop" download><img
            :src="image.image.third_size_crop" alt=""></a></div>
        <div class="col align-self-center text-center my-5"><a :href="image.image.third_size_thum" download><img
            :src="image.image.third_size_thum" alt=""></a></div>

        <hr>

      </div>

      <Pagination :total="totalPages" @pageChange="loadListImages"/>

    </div>

  </main>

</template>

<script>

import Pagination from "../components/Pagination"


export default {
  name: 'Main',
  data() {
    return {
      listImages: [],
      page: 1,
      totalPages: 0,
    }
  },
  components: {
    Pagination
  },
  created() {
    this.loadListImages(this.page)
  },
  methods: {
    async loadListImages(pageNumber) {
      this.listImages = await fetch(
          `${this.$store.getters.getServerUrl}/images/?page=${pageNumber}`
      ).then(response => response.json()
      ).then(response => {
        this.totalPages = response.count_pages;
        return response.results;
      })
    },
    async saveImage() {
      let input = document.querySelector('input[type="file"]')
      let data = new FormData()
      data.append('image', input.files[0])
      await fetch(`${this.$store.getters.getServerUrl}/images/save/`,
          {
            method: 'POST',
            body: data
          }
      ).then(response => {
        response.json()
        input.value = null
        window.location.reload();
      })
    }
  }
}
</script>

<style scoped>

a {
  text-decoration: none;
}

</style>
