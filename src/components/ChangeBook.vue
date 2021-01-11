<template>
    <div>
        <h3>修改图书信息页面</h3>
        <hr>
        <el-form :data="book" status-icon  ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="id" prop="ID">
                <el-input type="text" v-model="book.id" ></el-input>
            </el-form-item>
            <el-form-item label="书名" prop="book_name">
                <el-input type="text" v-model="book.book_name" ></el-input>
            </el-form-item>
            <el-form-item label="价格" prop="price">
                <el-input type="text" v-model="book.price" ></el-input>
            </el-form-item>
            <el-form-item label="年龄" prop="create_time">
                <el-input  type="date" v-model="book.create_time"></el-input>
            </el-form-item>
            <el-form-item label="出版社" prop="publish">
                <el-input v-model="book.publish"></el-input>
            </el-form-item>
            <el-form-item label="地址" prop="address">
                <el-input v-model="book.address"></el-input>
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
          book:[]
        };
    },
    methods: {
      change_book(){
        let id = this.$route.params.id;
        //console.log(id)
        this.$axios({
          url: "http://127.0.0.1:8000/libraryapp/books/" + id,
          method: 'get',
        }).then(res => {
          //console.log(res)
          // console.log(res.data.result)
          //alert('123')
          this.book=res.data.results
        })
      },
      update(){
        this.$axios({
          url: "http://127.0.0.1:8000/libraryapp/books/" ,
          method: 'patch',
          data:{
            id:this.book.id,
            book_name: this.book.book_name,
            price: this.book.price,
            create_time: this.book.create_time,
            publish: this.book.publish,
            address: this.book.address,
          },
        }).then(res => {

          console.log(res.data.result)
          // this.book=res.data.results
          this.$router.go(-1)
          alert('更新成功')

        })
      }

        },
  created() {
      this.change_book();

  },

}
</script>

<style scoped>

</style>
