const express = require('express')

const router = express.Router()

router.get('/',(req,res)=>{
    res.json({mssg:"GET all Workout"})
})

router.get('/:id',(req,res)=>{
    res.json({mssg:"GET a Workout"})
})

router.post('/',(req,res)=>{
    res.json({mssg:"POST a new Workout"})
})

router.delete('/:id',(req,res)=>{
    res.json({mssg:"DELETE a Workout"})
})

router.patch('/:id',(req,res)=>{
    res.json({mssg:"UPDATE a Workout"})
})

module.exports = router