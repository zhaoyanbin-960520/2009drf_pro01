<template>
    <div>
        <h3>用户详情信息</h3>
        <hr>
        <el-table :data="book_list" border style="width: 100%">
            <el-table-column prop="id" label="ID" width="120"></el-table-column>
            <el-table-column prop="book_name" label="书名" width="120"></el-table-column>
            <el-table-column prop="price" label="价格" width="150"></el-table-column>
            <el-table-column prop="create_time" label="发表时间" width="250"></el-table-column>
            <el-table-column prop="publish" label="出版版" width="180"></el-table-column>
            <el-table-column prop="address" label="地址" width="100"></el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: "Second",
    data() {
        return {
            book_list: [],
        }

    },
    methods: {
        get_emp() {
            //console.log(this.$route.params.id);
            let id = this.$route.params.id;
            this.$axios({
                url: "http://127.0.0.1:8000/libraryapp/books/" + id,
                method: 'get',

            }).then(res => {
                //console.log(res)
                //console.log(res.data.result)
                this.book_list=[res.data.results]
                alert("查询成功")

            })


        }

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
