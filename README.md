# qa_guru_python_8_2

This is the homework following the **second lecture**

Feedback on how to improve the code is highly appreciated

## Problems I faced in implementation:

* The Chrome notifications popup still was shown after adding --disable notifications option, like this:
  
 ```
  options = webdriver.ChromeOptions()
  options.add_argument('--disable-notifications')
  browser.config.driver_options = options
```

**Solution**: I removed the option cause the pop-up doesn't affect test results. Also, at some point the pop-up just stopped showing


* Google search stops showing 'Your search - **X** - did not match any documents.' text when I run all tests in the suit. The text is shown when I run the test separately.
  
**Solution**: I changed the assertion to check only the number of results text

* the test_google_should_find_selene is unstable: it can fail in random run though no changes in the code were made

**Solution**: not found



