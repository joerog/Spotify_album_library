<template>
  <div>
    <div>TEST {{ code }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Callback',
  data() {
    return {
      code: '',
    };
  },
  methods: {
  },
  mounted() {
    this.code = this.$route.query.code;
    const postdata = {
      code: this.code,
    };
    const path = `${this.$hostname}/callback/`;
    axios(path, {
      method: 'post',
      data: postdata,
      withCredentials: true,
    })
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.error(error);
      });
    this.$router.push({ name: 'Albums' });
  },
};
</script>

<style scoped>
img {
  max-width: 100px;
}
</style>
