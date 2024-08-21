using UnityEngine;
using UnityEngine.Tilemaps;

public class TilePlacement : MonoBehaviour
{
    public Tilemap tilemap;
    public TileBase[] buildingTiles; // Array of building tiles
    private int selectedBuildingIndex = 0; // Currently selected building

    void Update()
    {
        // Handle mouse click for placing a building
        if (Input.GetMouseButtonDown(0))
        {
            Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            Vector3Int gridPos = tilemap.WorldToCell(mousePos);

            // Highlight the tile before placing (optional)
            HighlightTile(gridPos);

            // Place the building if the tile is valid
            PlaceBuilding(gridPos);
        }

        // Handle input for selecting different building types
        if (Input.GetKeyDown(KeyCode.Alpha1)) { selectedBuildingIndex = 0; }
        if (Input.GetKeyDown(KeyCode.Alpha2)) { selectedBuildingIndex = 1; }
        // Add more keys as needed for additional building types
    }

    void PlaceBuilding(Vector3Int gridPos)
    {
        // Check if the tile is already occupied
        if (tilemap.GetTile(gridPos) == null)
        {
            tilemap.SetTile(gridPos, buildingTiles[selectedBuildingIndex]);
        }
        else
        {
            Debug.Log("Tile already occupied!");
        }
    }

    void HighlightTile(Vector3Int gridPos)
    {
        // Optionally, use another tile or color to highlight the placement area
        tilemap.SetTileFlags(gridPos, TileFlags.None);
        tilemap.SetColor(gridPos, Color.green); // Highlight in green
    }
}
