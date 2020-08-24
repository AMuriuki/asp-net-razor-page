using Microsoft.EntityFrameworkCore.Migrations;

namespace E_commerce.Migrations
{
    public partial class InitialCreate : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Product",
                columns: table => new
                {
                    ID = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    product_id = table.Column<string>(nullable: true),
                    local_id = table.Column<string>(nullable: true),
                    price = table.Column<decimal>(nullable: false),
                    product_no = table.Column<string>(nullable: true),
                    item_name = table.Column<string>(nullable: true),
                    category = table.Column<int>(nullable: false),
                    sub_category = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Product", x => x.ID);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Product");
        }
    }
}
