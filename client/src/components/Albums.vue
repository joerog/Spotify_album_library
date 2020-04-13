<template>
  <div>
    <h2>Album Library</h2>
    <div v-if="authed && getAlbums && getAlbums.length > 0">
      <div class="AlbumContainer" v-for="album in getAlbums" :key="album.id">
        <AlbumCover :album=album></AlbumCover>
      </div>
    </div>
    <div v-else>
      <a :href="redirect_url">Please Log In</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import AlbumCover from './AlbumCover.vue';

export default {
  name: 'Album',
  components: {
    AlbumCover,
  },
  props: {
    cover: String,
  },
  data() {
    return {
      albums: [],
      redirect_url: '',
      authed: false,
    };
  },
  asyncComputed: {
    async getAlbums() {
      console.log(`${this.$hostname}/albums/`);
      const pathAlbums = `${this.$hostname}/albums/`;
      const res = await axios.get(pathAlbums, { withCredentials: true });
      return res.data;
    },
  },
  mounted() {
    const path = `${this.$hostname}/auth`;
    axios.get(path, { withCredentials: true })
      .then((res) => {
        this.redirect_url = res.data.url;
        this.authed = res.data.authed;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style scoped>
.AlbumContainer {
  display: inline-block;
  width: auto;
  padding: 5px;
}
</style>
