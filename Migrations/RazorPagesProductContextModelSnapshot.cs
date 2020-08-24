﻿// <auto-generated />
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using RazorPagesProduct.Data;

namespace E_commerce.Migrations
{
    [DbContext(typeof(RazorPagesProductContext))]
    partial class RazorPagesProductContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "3.1.7");

            modelBuilder.Entity("RazorPagesProduct.Models.Product", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("INTEGER");

                    b.Property<int>("category")
                        .HasColumnType("INTEGER");

                    b.Property<string>("item_name")
                        .HasColumnType("TEXT");

                    b.Property<string>("local_id")
                        .HasColumnType("TEXT");

                    b.Property<decimal>("price")
                        .HasColumnType("TEXT");

                    b.Property<string>("product_id")
                        .HasColumnType("TEXT");

                    b.Property<string>("product_no")
                        .HasColumnType("TEXT");

                    b.Property<int>("sub_category")
                        .HasColumnType("INTEGER");

                    b.HasKey("ID");

                    b.ToTable("Product");
                });
#pragma warning restore 612, 618
        }
    }
}
