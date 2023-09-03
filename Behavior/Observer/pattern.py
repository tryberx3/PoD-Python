

class NewsPublisher:
    def __init__(self):
        self._subscribers = set()
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.add(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self._latest_news)

    def publish_news(self, news):
        self._latest_news = news
        self.notify_subscribers()


class NewsSubscriber:
    def __init__(self, name):
        self._name = name

    def update(self, news):
        print(f"{self._name} received news: {news}")


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    
    subscriber1 = NewsSubscriber("Subscriber 1")
    subscriber2 = NewsSubscriber("Subscriber 2")
    subscriber3 = NewsSubscriber("Subscriber 3")

    
    news_publisher.attach(subscriber1)
    news_publisher.attach(subscriber2)
    news_publisher.attach(subscriber3)

    
    news_publisher.publish_news("Breaking News: Major Event!")