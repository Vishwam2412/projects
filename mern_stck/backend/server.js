require('dotenv').config()


const mongoose = require("mongoose");
const express = require('express')
const webroute = require('./routes/workout.js')



const app = express()

app.use(express.json())


app.use((req,res,next)=>{
    console.log(req.path,req.method)
    next()
})

app.use('/api/workout',webroute)

mongoose.connect(process.env.MONG_URI)
    .then(()=>{
        app.listen(process.env.PORT,()=>{
            console.log("Connected to DataBase & Listining to port ",process.env.PORT)
        })
    })    
    .catch((error)=>{console.log(error)})


// app.get('/',(req,res)=>{
//     res.json({map:"The back of GraveYard."})    
// })

