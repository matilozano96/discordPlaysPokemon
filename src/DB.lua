console.clear()

SQL.createdatabase("DATABASE.db")
SQL.opendatabase("DATABASE.db")
print("Database created")

SQL.writecommand("CREATE TABLE Inputs (A BOOLEAN, B BOOLEAN, SEL BOOLEAN, Start BOOLEAN, Power BOOLEAN, move_Up BOOLEAN, move_Down BOOLEAN, move_Left BOOLEAN, move_Right BOOLEAN,L BOOLEAN,R BOOLEAN)")

SQL.writecommand("INSERT INTO Inputs (A, B, SEL, Start, Power, move_Up, move_Down, move_Left, move_Right, L, R) VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
print("Data Set")

counter = 0

while (true) do
    if (counter > -1) then
        counter = 0
    
        SQL.opendatabase("DATABASE.db")
        dbTable = {}
        dbTable = SQL.readcommand("SELECT * FROM Inputs")

        newTable = {}
    
        for key, value in pairs(dbTable) do
            -- Remove the trailing " 0" from the key
            local newKey = key:gsub(" 0$", "")
    
            -- Rename specific keys as needed
            if newKey == "move_Down" then
                newKey = "Down"
            elseif newKey == "move_Left" then
                newKey = "Left"
            elseif newKey == "move_Right" then
                newKey = "Right"
            elseif newKey == "move_Up" then
                newKey = "Up"
            elseif newKey == "SEL" then
                newKey = "Select"
            end
    
            newTable[newKey] = value
        end
    
        for key, value in pairs(newTable) do
            if (value) then 
                -- print("Pressing " .. key)
            end
        end
        emu.frameadvance()
        joypad.set(newTable)
    end
end