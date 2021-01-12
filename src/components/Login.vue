<template>
  <div>
    <hr>
    <el-form :data="student" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="用户名" prop="name">
        <el-input type="text" v-model="student.name"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="text" v-model="student.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login_logic">提交</el-button>
      </el-form-item>
    </el-form>

  </div>
</template>

<script>
export default {
name: "Login",
data(){
  return{
    student:{
      name:'',
      password: ''

    }
  }
},
  methods:{
    login_logic(){
      this.$axios({
        url: "http://127.0.0.1:8000/userapp/login/",
        method: 'post',
        data: {
          name: this.student.name,
          password: this.student.password,
        }
      }).then(res => {
        if (res.data) {
          this.$router.push("/first")
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
