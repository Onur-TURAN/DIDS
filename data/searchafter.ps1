$originalCsvPath = "results.csv"
$newCsvPath = "updated_sql_dataset_v2.csv"

# Kullanıcıdan yeni sütun ismini al
$newColumnName = Read-Host -Prompt "Yeni sütun ismini girin"

$data = Import-Csv -Path $originalCsvPath
$updatedData = @()

foreach ($row in $data) {
    # Son sütundaki rakamı al
    $lastNumber = [regex]::Match($row.Query, '\d+$').Value

    $updatedRow = [PSCustomObject]@{
        Query = $row.Query
        Label = $row.Label
        SELECT = $row.SELECT
        UNION = $row.UNION
        OR = $row.OR
        AND = $row.AND
        $newColumnName = $lastNumber
    }
    $updatedData += $updatedRow
}

$updatedData | Export-Csv -Path $newCsvPath -NoTypeInformation -Delimiter "," -UseQuotes None