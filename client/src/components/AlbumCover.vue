<template>
  <div>
    <img :src=cover() v-tooltip=tooltip()
     @click=goToAlbum()>
  </div>
</template>

<script>
export default {
  name: 'AlbumCover',
  props: {
    album: Object,
  },
  methods: {
    cover() {
      return this.album.album.images[0].url;
    },
    tooltip() {
      const artists = [];
      this.album.album.artists.forEach((value) => {
        artists.push(value.name);
      });
      return `<b>${this.album.album.name}</b><br>${artists.join(', ')}`;
    },
    goToAlbum() {
      window.open(this.album.album.external_urls.spotify, '_blank');
    },
  },
};
</script>

<style scoped>
img {
  max-width: 100px;
}
div {
  display: inline;
}
</style>
