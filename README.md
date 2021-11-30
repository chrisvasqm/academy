# Django Pet Project: Academy

This a pet project to try out a few things taking the example of a imginary Academy where Students can sign up for the Subjects they want to study.

## Administration Site

Admin and Staff members will be able to manage the following modules:

1. Academies
2. Students
3. Subjects
4. Groups

## Supported Endpoints

### Subjects

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Subject    | /subjects     | GET     | <span style="color:green">Yes</span>  |
| Subject    | /subjects     | POST     | <span style="color:green">Yes</span>  |
| Subject    | /subjects/{id}     | GET     |  <span style="color:green">Yes</span>  |
| Subject    | /subjects/{id}     | PUT     |  <span style="color:green">Yes</span>  |
| Subject    | /subjects/{id}     | DELETE     |  <span style="color:green">Yes</span> |

### Academies

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Academy    | /academy     | GET     | <span style="color:green">Yes</span>  |
| Academy    | /academy     | POST     | <span style="color:red">No</span>  |
| Academy    | /academy/{id}     | GET     |  <span style="color:red">No</span>  |
| Academy    | /academy/{id}     | PUT     |  <span style="color:red">No</span>  |
| Academy    | /academy/{id}     | DELETE     |  <span style="color:green">Yes</span> |

### Students

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Student    | /students     | GET     | <span style="color:green">Yes</span>  |
| Student    | /students     | POST     | <span style="color:red">No</span>  |
| Student    | /students/{id}     | GET     |  <span style="color:red">No</span>  |
| Student    | /students/{id}     | PUT     |  <span style="color:red">No</span>  |
| Student    | /students/{id}     | DELETE     |  <span style="color:green">Yes</span> |

### Enrollments

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Enrollment    | /enrollments     | GET     | <span style="color:green">Yes</span>  |
| Enrollment    | /enrollments     | POST     | <span style="color:red">No</span>  |
| Enrollment    | /enrollments/{id}     | GET     |  <span style="color:red">No</span>  |
| Enrollment    | /enrollments/{id}     | PUT     |  <span style="color:red">No</span>  |
| Enrollment    | /enrollments/{id}     | DELETE     |  <span style="color:green">Yes</span> |
