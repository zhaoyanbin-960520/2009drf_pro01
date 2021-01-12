<template>
    <div>
        <h3>添加学生</h3>
        <hr>
        <el-form :data="student" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="姓名" prop="name">
                <el-input type="text" v-model="student.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="text" v-model="student.password"></el-input>
            </el-form-item>
            <el-form-item label="年龄" prop="age">
                <el-input type="text" v-model="student.age"></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="sex">
                <el-input type="text" v-model="student.sex"></el-input>
            </el-form-item>
            <el-form-item label="生日" prop="bir">
                <el-input type="date" v-model="student.bir"></el-input>
            </el-form-item>
          <el-form-item label="联系方式" prop="phone">
            <el-input type="text" v-model="student.phone"></el-input>
          </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="add_book">提交</el-button>
            </el-form-item>
        </el-form>
    </div>

</template>

<script>
export default {
    name: "AddBook",
    data() {
        return {
          student: {
              name: '',
              password: '',
              age: '',
              sex: '',
              bir: '',
              phone:'',
            }
        }
    },
    methods: {
      add_book() {
            this.$axios({
                url: "http://127.0.0.1:8000/userapp/student/",
                method: 'post',
              data: {
                name: this.student.name,
                password: this.student.password,
                age: this.student.age,
                sex: this.student.sex,
                bir: this.student.bir,
                phone:this.student.phone,
              }
                //headers: {"Content-Type": 'application/x-www-form-urlencoded;charset=UTF-8'}
            }).then(res => {
                if (res.data) {
                    this.$router.go(-1)
                }
            })
        }
      }
    }

</script>

<style scoped>
h3 {
    color: blue;
}

</style>
