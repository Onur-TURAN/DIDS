$originalCsvPath = "results.csv"

$newCsvPath = "alldata.csv"

$data = Import-Csv -Path $originalCsvPath

$updatedData = @()

foreach ($row in $data) {
    $updatedRow = [PSCustomObject]@{
        Query = $row.Query
        Label = $row.Label
        SELECT = $row.SELECT
        UNION = $row.UNION
        OR = $row.OR
        AND = $row.AND
        NewColumn = $row.SELECT
    }
    $updatedData += $updatedRow
}

$updatedData | Export-Csv -Path $newCsvPath -NoTypeInformation