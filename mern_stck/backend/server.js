require('dotenv').config()

const express = require('express')
const webroute = require('./routes/workout')
const app = express()

app.use(express.json())

app.use((req,res,next)=>{
      console.log(req.path,req.method)
      next()
})
    
app.use('/api/workout',webroute)

// app.get('/',(req,res)=>{
//     res.json({map:"The back of GraveYard."})
// })

app.listen(process.env.PORT,()=>{
    console.log("Listining to port 4000")
})


