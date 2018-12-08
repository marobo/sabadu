# SIMPLE FLOWCHART

Ask the user for an odd number

If the number is even, respond “THAT IS NOT  AN ODD NUMBER” and ask again

If the number is 5, respond “MY FAVOURITE NUMBER!”

If the number is odd respond with “THANKYOU THAT NUMBER IS ODD”

```mermaid
graph LR
A(START)--> B>Please enter an odd number]
B-->C{Is the number 5?}
C--Yes-->D>MY FAVOUTRITE NUMBER!]
C--No-->E{Is the number odd?}
E--Yes-->F>Thankyou that number is odd]
E--No-->H>THAT IS NOT AN ODD NUBER]
H--No-->K>PLEASE CHOOSE A NUMBER]
K-->B
F-->G[END]
D-->G
```

```

```