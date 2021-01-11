<template>
    <div>
        <h3>欢迎首页</h3>
        <hr>
        <el-table :data="book_list" border style="width: 100%">
            <el-table-column prop="id" label="ID" width="120"></el-table-column>
            <el-table-column prop="book_name" label="书名" width="120"></el-table-column>
            <el-table-column prop="price" label="价格" width="150"></el-table-column>
            <el-table-column prop="create_time" label="发表时间" width="250"></el-table-column>
            <el-table-column prop="publish" label="出版社" width="180"></el-table-column>
            <el-table-column prop="address" label="地址" width="100"></el-table-column>
            <el-table-column label="操作" width="300">
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
            //console.log(row);
            this.$router.push("/second/" + row)
        },
      del_book(id) {
            //console.log(id);
            this.$axios({
                //DRF类视图函数路由
                url: "http://127.0.0.1:8000/libraryapp/books/" + id,
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
            book_list: [],

        }
    },
    created() {
        this.$axios({
            url: "http://127.0.0.1:8000/libraryapp/books/",
            //请求方式
            method: "get",
        }).then(response => {
            // 请求成功后可以走到这个回调函
            // console.log(response)
            // console.log(response.data)
            this.book_list = response.data.results
        })
    },
}
</script>

<style scoped>
h3 {
    color: red;
}
</style>
