MOV R1, 0
MOV R2, 0

CMP R1, #10
BGE skip

loop:
    ADD R2, R2, #2
    ADD R1, R1, #1
    CMP R1, #10
    BLT loop

skip:
    B skip

.end