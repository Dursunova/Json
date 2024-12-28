Create database layihe_db;
Use layihe_db;
Create table Wikipedia(
id int primary key,
result varchar(50),
comment_d varchar(50),
test VARCHAR(100) NOT NULL,
time_d varchar(50)
);
Insert into Wikipedia(id, result,comment_d, test, time_d)
values(
1, "Failed", null, "test_logo_dimensions", "00:00:12"
);
Insert into Wikipedia(id, result,comment_d, test, time_d)
values(
2, "Failed", null, "test_page_color", "00:00:12"
);
Insert into Wikipedia(id, result,comment_d, test, time_d)
values(
3, "Failed", null, "test_font_family", "00:00:26"
);
Insert into Wikipedia(id, result,comment_d, test, time_d)
values(
4, "Passed", null, "test_table_css", "00:00:12"
);
