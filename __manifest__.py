#-*- coding: utf-8 -*-

{
	"name": "simpeldes",
	"version": "1.0", 
	"depends": [
		'base',
		'mail',
	],
	"author": "Divisi RnD Cendana2000",
	"category": "Utility",
	"website": "http://cendana2000.co.id",
	"images": ["static/description/images/main_screenshot.jpg"],
	"license": "OPL-1",
	"summary": "Aplikasi Sistem Informasi Manajemen Data Desa",
	"description": """

Information
======================================================================

* created menus
* created objects
* created views
* logics

""",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/warga.xml",
		"view/pendidikan.xml",
		"view/pekerjaan.xml",
		"view/suku.xml",
		"view/hobi.xml",
		"view/lahan_warga.xml",
		"view/ref_data.xml",
		"report/warga.xml",
		"report/pendidikan.xml",
		"report/pekerjaan.xml",
		"report/suku.xml",
		"report/hobi.xml",
		"report/lahan_warga.xml",
		"report/ref_data.xml",
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}