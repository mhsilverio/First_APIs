const express = require('express')
const routes = express.Router()

let db = [
    {'1': { Nome: 'Nome 1', CPF: 'XXX.XXX.XXX-XX', email: 'XXXXXXXXXX@email.com'}},
    {'2': { Nome: 'Nome 2', CPF: 'XXX.XXX.XXX-XX', email: 'XXXXXXXXXX@email.com'}},
    {'3': { Nome: 'Nome 3', CPF: 'XXX.XXX.XXX-XX', email: 'XXXXXXXXXX@email.com'}},
    {'4': { Nome: 'Nome 4', CPF: 'XXX.XXX.XXX-XX', email: 'XXXXXXXXXX@email.com'}},
    {'5': { Nome: 'Nome 5', CPF: 'XXX.XXX.XXX-XX', email: 'XXXXXXXXXX@email.com'}},

]
routes.get('/', (req, res) => {
    return res.json("200 OK")
})

routes.get('/usuarios', (req, res) => {
    return res.json(db)
})

routes.get('/:id', (req, res) => {
    const id =  req.params.id
    let newDB = db.filter(item => {
        if(item[id])
            return item
    })
    return res.json(newDB)
})

routes.post('/add', (req, res) => {
    const body = req.body

    if (!body)
        return res.status(400).end()
    db.push(body)
        return res.json(body)
})

routes.delete('/:id', (req, res) => {
    const id =  req.params.id

    let newDB = db.filter(item => {
        if(!item[id])
            return item
    })
    db = newDB
    return res.send(newDB)
})

module.exports = routes