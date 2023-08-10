import os
from selene import browser, be, have, command
from selenium.webdriver import Keys


def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Имя')
    browser.element('#lastName').should(be.blank).type('Фамилия')
    browser.element('#userEmail').should(be.blank).type('pochta@pochta.com')
    browser.element('[for=gender-radio-3]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1998"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('#subjectsInput').should(be.blank).type('c').press_enter()
    browser.element('#subjectsInput').send_keys(Keys.ARROW_DOWN)
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('memasik.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Улица Кушкина, Дом Пушкина')
    # а вот тут у меня для выбора штата простой клик не сработал, а клик js сработал
    browser.element('#react-select-3-input').perform(command.js.click).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.ARROW_DOWN).press_enter()
    browser.element('#react-select-4-input').perform(command.js.click).send_keys(Keys.ARROW_DOWN).press_enter()
    browser.element('#submit').click()
    browser.element('.table').should(
        have.text('Имя'
                  and 'Фамилия'
                  and 'pochta@pochta.com'
                  and 'Other'
                  and '1234567890'
                  and '8 April,1998'
                  and 'Physics'
                  and 'Music, Reading, Sports'
                  and 'memasik.jpg'
                  and 'Улица Кушкина, Дом Пушкина'
                  and 'Uttar Pradesh Agra'))
