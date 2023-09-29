MOV R1, #5 

CMP R1, #5

BLT if
B else

if:
    mov R1, #5

else:
    ADD R1, #1
    