<template>
    <div>
        <h3>欢迎首页</h3>
        <hr>
      <el-table :data="stu_list" border style="width: 100%">
        <el-table-column prop="id" label="ID" width="50"></el-table-column>
        <el-table-column prop="name" label="姓名" width="120"></el-table-column>
        <el-table-column prop="password" label="密码" width="120"></el-table-column>
        <el-table-column prop="age" label="年龄" width="150"></el-table-column>
        <el-table-column prop="sex" label="性别" width="50"></el-table-column>
        <el-table-column prop="bir" label="生日" width="180"></el-table-column>
        <el-table-column prop="phone" label="联系方式" width="180"></el-table-column>
        <el-table-column label="操作" width="400">
          <template slot-scope="scope">
            <el-button @click="checkBook(scope.row.id)" type="text" size="small">查看</el-button>
            |
            <el-button @click="add_book" type="text" size="small">增加</el-button>
            |
            <el-button @click="del_book(scope.row.id)" type="text" size="small">删除</el-button>
            |
            <el-button @click="change_page(scope.row.id)" type="text" size="small">修改</el-button>

          </template>
        </el-table-column>
      </el-table>
    </div>

</template>

<script>
export default {
    name: "First",
    methods: {
      checkBook(row) {
            console.log(row);
            this.$router.push("/second/" + row)
        //console.log(row)
        },
      del_book(id) {
            //console.log(id);
            this.$axios({
                //DRF类视图函数路由
                url: "http://127.0.0.1:8000/userapp/student/" + id,
                method: 'delete',
                //data: {'id': id},
            }).then(res => {
                if (res.data) {
                    this.$router.go(0)
                    alert('删除成功')
                }
            })
        },
        change_page(row) {
            console.log(row)
            this.$router.push("/change/" + row)
        },

      add_book() {
            this.$router.push("/add_book")
        },

    },

    data() {
        return {
            stu_list: [],

        }
    },
    created() {

      this.$axios({
        url: "http://127.0.0.1:8000/userapp/student/",
        //请求方式
        method: "get",
      }).then(response => {
        this.stu_list = response.data
      })
    },
}
</script>

<style scoped>
h3 {
    color: red;
}
</style>
