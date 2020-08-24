using Microsoft.EntityFrameworkCore;

namespace RazorPagesProduct.Data
{
    public class RazorPagesProductContext : DbContext
    {
        public RazorPagesProductContext(
            DbContextOptions<RazorPagesProductContext> options)
            : base(options)
        {
        }

        public DbSet<RazorPagesProduct.Models.Product> Product { get; set; }
    }
}