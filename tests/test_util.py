import os
import types
import unittest
from unittest import mock

from dotenv import load_dotenv
from test_mock_data import (
    channel_snippet_list_result, channel_stat_list_result,
    video_list_snippet_result, video_search_snippet_result,
    video_stat_list_result
)

import pyytdata
from pyytdata import PyYtData, util

load_dotenv()


class TestPyYtData(unittest.TestCase):
    def test_check_env(self):
        self.assertTrue(os.environ.get("API_KEY") is not None)

    @mock.patch(
        "pyytdata.util.fetcher.VideoDataFetcher.get_result",
        return_value=video_search_snippet_result,
    )
    @mock.patch(
        "pyytdata.util.fetcher.VideoDataFetcher.qtype",
        new_callable=mock.PropertyMock,
        return_value="search",
    )
    def test_get_videoinfo(self, get_result_mock, qtype_mock):
        self.data = PyYtData("flask", 6)
        self.rslt = self.data.get_videoinfo()
        self.assertIsInstance(self.rslt, types.GeneratorType)
        self.assertTrue(len(list(self.rslt)) == 6)


class TestVideoInfo(unittest.TestCase):
    @mock.patch(
        "pyytdata.util.fetcher.VideoDataFetcher.get_result",
        return_value=video_list_snippet_result,
    )
    @mock.patch(
        "pyytdata.util.fetcher.VideoDataFetcher.qtype",
        new_callable=mock.PropertyMock,
        return_value="list",
    )
    def test_get_result(self, get_result_moc, qtype_mock):
        video_fetcher = util.fetcher.VideoDataFetcher()
        vid = util.info.VideoInfo(video_fetcher, "snippet", video_id="zmWf_cHyo8s")
        assert (
            vid.get_info(0).title
            == "More Python Code Smells: Avoid These 7 Smelly Snags"
        )


class TestChannelInfo(unittest.TestCase):
    @mock.patch(
        "pyytdata.util.fetcher.ChannelDataFetcher.get_result",
        return_value=channel_snippet_list_result,
    )
    def test_get_result(self, get_result_moc):
        channel_fetcher = util.fetcher.ChannelDataFetcher()
        channel_info = util.info.ChannelInfo(
            channel_fetcher, "snippet", channel_name="zeenews"
        )
        assert channel_info.get_info().title == "Zee News"


class TestVideoStat(unittest.TestCase):
    @mock.patch(
        "pyytdata.util.fetcher.VideoDataFetcher.get_result",
        return_value=video_stat_list_result,
    )
    def test_get_result(self, get_result_moc):
        video_fetcher = util.fetcher.VideoDataFetcher()
        vid = util.info.VideoStatInfo(
            video_fetcher, "statistic", video_id="zmWf_cHyo8s"
        )
        assert vid.get_info().total_view == "74462"


class TestChannelStat(unittest.TestCase):
    @mock.patch(
        "pyytdata.util.fetcher.ChannelDataFetcher.get_result",
        return_value=channel_stat_list_result,
    )
    def test_get_result(self, get_result_moc):
        channel_fetcher = util.fetcher.ChannelDataFetcher()
        channel_info = util.info.ChannelStatInfo(
            channel_fetcher, "statistic", channel_name="zeenews"
        )
        assert channel_info.get_info().total_viewcount == "14634734282"


if __name__ == "__main__":
    unittest.main()
