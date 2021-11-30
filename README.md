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
| Subject    | /subjects     | GET     | Yes  |
| Subject    | /subjects     | POST     | Yes  |
| Subject    | /subjects/{id}     | GET     |  Yes  |
| Subject    | /subjects/{id}     | PUT     |  Yes  |
| Subject    | /subjects/{id}     | DELETE     |  Yes |

### Academies

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Academy    | /academy     | GET     | Yes  |
| Academy    | /academy     | POST     | No  |
| Academy    | /academy/{id}     | GET     |  No  |
| Academy    | /academy/{id}     | PUT     |  No  |
| Academy    | /academy/{id}     | DELETE     |  Yes |

### Students

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Student    | /students     | GET     | Yes  |
| Student    | /students     | POST     | No  |
| Student    | /students/{id}     | GET     |  No  |
| Student    | /students/{id}     | PUT     |  No  |
| Student    | /students/{id}     | DELETE     |  Yes |

### Enrollments

| Model  | Endpoint   | HTTP Method   | Is Supported
|-------------- | -------------- | -------------- | -------------- |
| Enrollment    | /enrollments     | GET     | Yes  |
| Enrollment    | /enrollments     | POST     | No  |
| Enrollment    | /enrollments/{id}     | GET     |  No  |
| Enrollment    | /enrollments/{id}     | PUT     |  No  |
| Enrollment    | /enrollments/{id}     | DELETE     |  Yes |
