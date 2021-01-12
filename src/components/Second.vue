<template>
    <div>
        <h3>学生详情信息</h3>
        <hr>
      <el-table :data="stu_list" border style="width: 100%">
        <el-table-column prop="id" label="ID" width="50"></el-table-column>
        <el-table-column prop="name" label="姓名" width="120"></el-table-column>
        <el-table-column prop="password" label="密码" width="150"></el-table-column>
        <el-table-column prop="age" label="年龄" width="50"></el-table-column>
        <el-table-column prop="sex" label="性别" width="180"></el-table-column>
        <el-table-column prop="bir" label="生日" width="100"></el-table-column>
        <el-table-column prop="phone" label="联系方式" width="200"></el-table-column>
      </el-table>
    </div>
</template>

<script>
export default {
  name: "Second",
  data() {
    return {
      stu_list: [],
    }

  },
  methods: {
    get_emp() {
      let id = this.$route.params.id;
      //console.log(id);
      this.$axios({
        url: "http://127.0.0.1:8000/userapp/student/" + id,
        method: 'get',
      }).then(res => {
        //console.log(res);
        console.log(res.data);
        this.stu_list = [res.data];
        alert("查询成功")


      })



    },
  },
    created() {
      this.get_emp();

    },

}
</script>

<style scoped>
h3 {
    color: red;
}

</style>
