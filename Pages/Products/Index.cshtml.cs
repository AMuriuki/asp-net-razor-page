using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using RazorPagesProduct.Data;
using RazorPagesProduct.Models;
using RazorPagesProduct.Pagination;

namespace E_commerce.Pages.Products
{
    public class IndexModel : PageModel
    {
        private readonly RazorPagesProduct.Data.RazorPagesProductContext _context;

        public IndexModel(RazorPagesProduct.Data.RazorPagesProductContext context)
        {
            _context = context;
        }

        public PaginatedList<Product> Products { get; set; }

        public async Task OnGetAsync(string sortOrder,
            string currentFilter, string searchString, int? pageIndex)
        {
            if (searchString != null)
            {
                pageIndex = 1;
            }
            else
            {
                searchString = currentFilter;
            }

            int pageSize = 23;
            Products = await PaginatedList<Product>.CreateAsync(
                _context.Product.AsNoTracking(), pageIndex ?? 1, pageSize);
        }

        // public IList<Product> Product { get; set; }

        // public async Task OnGetAsync()
        // {
        //     Product = await _context.Product.Take(23).ToListAsync();
        // }
    }
}
