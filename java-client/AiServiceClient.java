import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

public class AiServiceClient {

    private final RestTemplate restTemplate;

    public AiServiceClient() {
        this.restTemplate = new RestTemplate();
    }

    public String callEndpoint(String endpoint, String input) {

        try {

            String url = "http://localhost:5000/" + endpoint;

            Map<String, String> requestBody = new HashMap<>();

            requestBody.put("input", input);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(requestBody);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(
                            url,
                            request,
                            String.class
                    );

            return response.getBody();

        } catch (Exception exception) {

            System.out.println("AI Service Error: " + exception.getMessage());

            return null;
        }
    }
}