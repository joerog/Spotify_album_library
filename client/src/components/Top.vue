<template>
  <div>
    <h2>Top Artists</h2>
    <ul v-if="authed && getTop && getTop.length > 0">
      <li class="TopContainer" v-for="artist in getTop" :key="artist.id">
        {{ artist.name }}
      </li>
    </ul>
    <div v-else>
      <a :href="redirect_url">Please Log In</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Top',
  data() {
    return {
      redirect_url: '',
      authed: false,
    };
  },
  asyncComputed: {
    async getTop() {
      const pathTop = `${this.$hostname}/top/`;
      const res = await axios.get(pathTop, { withCredentials: true });
      console.log(res);
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
ul {
  list-style-type: none;
  padding: 0px;
}
</style>
