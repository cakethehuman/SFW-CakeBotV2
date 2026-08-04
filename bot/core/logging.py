import logging
import typing

from yachalk import chalk


class LogException(Exception):
    """Exception that happens in Logger class"""

class ColoredFormatter(logging.Formatter):
    level_colors: typing.ClassVar[dict[int, typing.Callable]] = {
        logging.DEBUG: chalk.cyan_bright,
        logging.INFO: chalk.blue_bright,
        logging.WARNING: chalk.yellow_bright,
        logging.ERROR: chalk.red_bright,
        logging.CRITICAL: chalk.bg_red_bright.white_bright
    }
    
    format_str = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    def format(self, record):
        color = self.level_colors.get(record.levelno, None)
        if color == None:
            raise LogException(f"Invalid Log Level {record.levelno}")
            
        formatter = logging.Formatter(color(self.format_str), datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)
    
def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler])
    logging.basicConfig(level=logging.WARNING, handlers=[handler])
    logging.basicConfig(level=logging.ERROR, handlers=[handler])
    logging.basicConfig(level=logging.CRITICAL, handlers=[handler])