using System;
using System.ComponentModel.DataAnnotations;

namespace RazorPagesProduct.Models
{
    public class Product
    {
        public int ID { get; set; }
        public string product_id { get; set; }
        public string local_id { get; set; }
        public decimal price { get; set; }
        public string product_no { get; set; }
        public string item_name { get; set; }
        public int category { set; get; }
        public int sub_category { get; set; }

        public string image_path { get; set; }
    }
}