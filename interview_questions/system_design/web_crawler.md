# Web Crawler

## Description

Design a web crawler that will crawl a website (e.g. Wikipedia)

## Initial Question(s)
* What are the expected number of URLs to crawl (write QPS) and expected number of Query API Calls (read QPS)?

## Main Components
1. The crawler
2. The indexer

## Crawler
* For crawling, need a "seed of URLs" to begin the crawling; place them in a queue
* Queue workers would work on one URL at a time. Each queue working has to
  *  Extract text from URL and send it to a Document Indexing Service
  *  Insert found link in the page back into the queue. Before inserting the link, look up in a NoSQL store and ensure they haven't already been crawled
*  When the queue becomes empty, reseed the queue with new URLs and restart the process

## Challenges
* How does the crawler handle dead links. Maintain a list of links that are considered "dead" and don't place them in the next queue
* Temporarily offline sites. Assume crawler connected but took 30 seconds to receive a 503. By this time, the queue released the URL to another worker to attempt to reconnect.

References:
* [Leetcode Discussion Board](https://leetcode.com/discuss/interview-question/system-design/124657/Facebook-or-System-Design-or-A-web-crawler-that-will-crawl-Wikipedia)

