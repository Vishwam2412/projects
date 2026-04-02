const express = require('express')
const Workout = require("../models/workoutSchema")

const router = express.Router()

router.get('/',(req,res)=>{
    res.json({mssg:"GET all Workout"})
})

router.get('/:id',(req,res)=>{
    res.json({mssg:"GET a Workout"})
})

router.post('/', async (req,res)=>{
    const {title,reps,load} = req.body

    try{
        const workout = await Workout.create({title,reps,load}) 
        return res.status(200).json(workout)
    }catch(error){
        console.log({"error":error.message()})
    }

    res.json({mssg:"POST a new Workout"})
})

router.delete('/:id',(req,res)=>{
    res.json({mssg:"DELETE a Workout"})
})

router.patch('/:id',(req,res)=>{
    res.json({mssg:"UPDATE a Workout"})
})

module.exports = router