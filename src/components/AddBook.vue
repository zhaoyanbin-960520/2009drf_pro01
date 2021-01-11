<template>
    <div>
        <h3>添加图书</h3>
        <hr>
        <el-form :data="book" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="书名" prop="book_name">
                <el-input type="text" v-model="book.book_name"></el-input>
            </el-form-item>
            <el-form-item label="价格" prop="price">
                <el-input type="text" v-model="book.price"></el-input>
            </el-form-item>
            <el-form-item label="出版时间" prop="create_time">
                <el-input type="date" v-model="book.create_time"></el-input>
            </el-form-item>
            <el-form-item label="出版社" prop="publish">
                <el-input type="text" v-model="book.publish"></el-input>
            </el-form-item>
            <el-form-item label="地址" prop="address">
                <el-input type="text" v-model="book.address"></el-input>
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
            book: {
              book_name: '',
              price: '',
              create_time: '',
              publish: '',
              address: '',
            }
        }
    },
    methods: {
      add_book() {
            this.$axios({
                url: "http://127.0.0.1:8000/libraryapp/books/",
                method: 'post',
                //Django添加参数传递
                // data: this.$qs.stringify({
                //   book_name: this.book.book_name,
                //   price: this.book.price,
                //   create_time: this.book.create_time,
                //   publish: this.book.publish,
                //   address: this.book.address,
                // }),
              data: {
                book_name: this.book.book_name,
                price: this.book.price,
                create_time: this.book.create_time,
                publish: this.book.publish,
                address: this.book.address,}
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
