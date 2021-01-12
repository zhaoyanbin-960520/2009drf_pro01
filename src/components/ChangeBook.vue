<template>
    <div>
        <h3>修改图书信息页面</h3>
        <hr>
        <el-form :data="student" status-icon  ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="id" prop="ID">
                <el-input type="text" v-model="student.id" ></el-input>
            </el-form-item>
            <el-form-item label="姓名" prop="name">
                <el-input type="text" v-model="student.name" ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="text" v-model="student.password" ></el-input>
            </el-form-item>
            <el-form-item label="年龄" prop="age">
                <el-input  type="text" v-model="student.age"></el-input>
            </el-form-item>
            <el-form-item label="生日" prop="bir">
                <el-input  type="date" v-model="student.bir"></el-input>
            </el-form-item>
            <el-form-item label="联系方式" prop="phone">
                <el-input v-model="student.phone"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="update">提交</el-button>
<!--                <el-button type="primary" >提交</el-button>-->
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: "ChangeBook",
    data() {

        return {
          student:[]
        };
    },
    methods: {
      change_book(){
        let id = this.$route.params.id;
        //console.log(id)
        this.$axios({
          url: "http://127.0.0.1:8000/userapp/student/" + id,
          method: 'get',
        }).then(res => {
          //console.log(res)
          // console.log(res.data.result)
          //alert('123')
          this.student=res.data
        })
      },
      // update(){
      //   this.$axios({
      //     url: "http://127.0.0.1:8000/userapp/student/" ,
      //     method: 'patch',
      //     data:{
      //       id:this.student.id,
      //       name: this.student.name,
      //       password: this.student.password,
      //       age: this.student.age,
      //       sex: this.student.sex,
      //       bir: this.student.bir,
      //       phone:this.student.phone,
      //     },
      //   }).then(res => {
      //
      //     console.log(res.data.result)
      //     // this.book=res.data.results
      //     this.$router.go(-1)
      //     alert('更新成功')
      //
      //   })
      // }

        },
  created() {
      this.change_book();

  },

}
</script>

<style scoped>

</style>
