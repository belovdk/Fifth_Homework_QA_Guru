import os
import resources

from selene import browser, be, have


def test_form():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).type('Имя')
    browser.element('#lastName').should(be.blank).type('Фамилия')
    browser.element('#userEmail').should(be.blank).type('pochta@pochta.com')
    browser.all('[name=gender]').element_by(have.value('Other')).element('..').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('April')
    browser.element('.react-datepicker__year-select').send_keys('1998')
    browser.element(f'.react-datepicker__day--00{8}').click()

    browser.element('#subjectsInput').should(be.blank).type('Physics').press_enter()

    browser.all('[for*=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.all('[for*=hobbies-checkbox]').element_by(have.text('Reading')).click()
    browser.all('[for*=hobbies-checkbox]').element_by(have.text('Music')).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(resources.__file__), 'memasik.jpg')))

    browser.element('#currentAddress').should(be.blank).type('Улица Кушкина, Дом Пушкина')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Uttar Pradesh')).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Agra')).click()

    browser.element('#submit').click()

    # THEN
    browser.element('.table').all('td').even.should(
        have.texts('Имя Фамилия', 'pochta@pochta.com', 'Other', '1234567890', '8 April,1998', 'Physics',
                   'Sports, Reading, Music', 'memasik.jpg', 'Улица Кушкина, Дом Пушкина', 'Uttar Pradesh Agra'))
