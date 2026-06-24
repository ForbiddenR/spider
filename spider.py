from __future__ import annotations

  import time

  from crawlerkit import Spider


  class QuickSpider(Spider):
      def run(self) -> None:
          self.log("INFO", "quick spider starting")
          time.sleep(1)
          self.item({"ok": True, "spider": "quick"})
          self.log("INFO", "quick spider done")
