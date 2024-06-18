import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}
class _HomePageState extends State<HomePage> {
  List data = [];
  // This widget is the root of your application.
  Future <void> fetchData() async {
    try {
      final response = await http.get(Uri.parse('http://127.0.0.1:8000/product/'));
      if (response.statusCode == 200) {
        setState(() {
          data = [''];
        });
      } else {
        throw Exception('Failed to load data');
      }
    } catch (e) {
      setState(() {
        data = ['Error: $e'];
      });
    }
  }
   @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('api test'),actions: [
        IconButton(onPressed:fetchData , icon: Icon(Icons.add_circle_outline)),
      ], ),
      body: Text('${data}')
    );
  }
  }
