#!/usr/bin/env python3
# Author: Zhangxunan
import os
import time
import configparser
import logging
import logging.handlers


def get_config(config_filename, section=''):
    """
    获取配置文件
    :param config_filename:配置文件的文件名
    :param section: 配置文件里的section
    :return: conf_items字典
    """
    config = configparser.ConfigParser()
    config.read(config_filename)

    conf_items = dict(config.items('common')) if config.has_section('common') else {}
    if section and config.has_section(section):
        conf_items.update(config.items(section))
    return conf_items


def add_handler(log_name, formatter, level, logger=None):
    """
    增加handler
    :param log_name: 日志文件名
    :param formatter: 格式
    :param level: 日志级别
    :param logger: logger
    :return: None
    """
    if not logger:
        return

    log_handler = logging.handlers.TimedRotatingFileHandler(log_name, when='midnight')
    log_formatter = logging.Formatter(formatter)
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)
    logger.setLevel(level)


def set_logging(log_path, log_level='error'):
    """
    设置日志格式，日志文件
    :param log_path: 日志文件路径
    :param log_level: 日志级别
    :return: None
    """
    log_levels = {
                  'critical': logging.CRITICAL, 'error': logging.ERROR,
                  'warning': logging.WARNING, 'info': logging.INFO,
                  'debug': logging.DEBUG
                 }

    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    log_name = os.path.join(log_path, 'record.log')
    logger = logging.getLogger('record')
    formatter = '%(message)s'
    add_handler(log_name, formatter, logging.DEBUG, logger)

    log_name = os.path.join(log_path, 'service.log')
    logger = logging.getLogger()
    formatter = '%(asctime)s %(levelname)s %(process)d %(thread)d %(filename)s-%(funcName)s:%(lineno)d %(message)s'
    add_handler(log_name, formatter, log_levels.get(log_level.lower(), logging.ERROR), logger)


def write_log(user, msg):
    """
    写日志
    :param user: 用户名
    :param msg: 日志信息
    :return: None
    """
    logging.getLogger('record').debug('%s %s %s' % (time.ctime(), user, msg))
