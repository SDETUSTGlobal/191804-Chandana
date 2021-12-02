package example;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;

public class NewTest {
	private WebDriver driver;
  @Test
  public void testEasy() {
	  driver.get("https://www.google.com/");
	  String title = driver.getTitle();
	  Assert.assertTrue(title.contains("Google"));
  }
  @BeforeTest
  public void beforeTest() {
	  System.setProperty("webdriver.chrome.driver","C://Users//HP_Owner//Desktop//ust doc//chromedriver.exe");
	  driver = new ChromeDriver();
  }

  @AfterTest
  public void afterTest() {
	  //driver.quit();
  }

}
