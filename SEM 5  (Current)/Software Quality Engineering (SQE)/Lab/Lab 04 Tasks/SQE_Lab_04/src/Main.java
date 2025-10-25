import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;

import java.util.Set;

public class Main {

    public static void main(String[] args) throws InterruptedException {

        // --- Setup ---
        // 1. Set the path to your downloaded msedgedriver.exe
        // IMPORTANT: Replace this path with the actual location of your driver file.
        System.setProperty("webdriver.edge.driver", "A:\\Academic\\Webdrivers\\edgedriver_win64\\msedgedriver.exe");

        // 2. Instantiate the WebDriver for Edge
        WebDriver driver = new EdgeDriver();

        System.out.println("--- Browser Window Management ---");

        // 3. Manage the browser window
        driver.manage().window().maximize(); // Maximize the window
        System.out.println("Window maximized.");
        Thread.sleep(1500); // Pausing for 1.5 seconds to observe

        driver.manage().window().minimize(); // Minimize the window
        System.out.println("Window minimized.");
        Thread.sleep(1500);

        driver.manage().window().maximize(); // Maximize again to continue
        driver.manage().window().fullscreen(); // Enter fullscreen mode
        System.out.println("Entered fullscreen mode.");
        Thread.sleep(1500);
        driver.manage().window().maximize(); // Exit fullscreen

        // Set a custom window size
        driver.manage().window().setSize(new Dimension(1200, 800));
        System.out.println("Window size set to 1200x800.");
        Thread.sleep(1500);

        System.out.println("\n--- Navigation and Information Retrieval ---");

        // 4. Navigate to a URL
        driver.get("https://www.google.com");
        System.out.println("Navigated to Google.");

        // 5. Get browser information
        System.out.println("Current Page Title: " + driver.getTitle());
        System.out.println("Current URL: " + driver.getCurrentUrl());

        // 6. Use Navigation commands
        driver.navigate().to("https://www.bing.com");
        System.out.println("Navigated to Bing using navigate().to()");
        Thread.sleep(1500);

        driver.navigate().back(); // Go back to Google
        System.out.println("Navigated back. Current URL: " + driver.getCurrentUrl());
        Thread.sleep(1500);

        driver.navigate().forward(); // Go forward to Bing
        System.out.println("Navigated forward. Current URL: " + driver.getCurrentUrl());
        Thread.sleep(1500);

        driver.navigate().refresh(); // Refresh the page
        System.out.println("Page refreshed.");
        Thread.sleep(1500);


        System.out.println("\n--- Handling Multiple Windows/Tabs ---");

        // 7. Open and switch between tabs
        String originalWindowHandle = driver.getWindowHandle();
        driver.switchTo().newWindow(WindowType.TAB); // Open a new tab
        driver.get("https://www.selenium.dev");
        System.out.println("Opened new tab. New Title: " + driver.getTitle());
        Thread.sleep(2000);

        driver.close(); // Close the current (new) tab
        System.out.println("Closed the new tab.");

        driver.switchTo().window(originalWindowHandle); // Switch back to the first tab
        System.out.println("Switched back to original tab. Title: " + driver.getTitle());
        Thread.sleep(1500);

        // --- Teardown ---
        // 8. Quit the entire browser session
        driver.quit();
        System.out.println("Browser session terminated.");
    }
}