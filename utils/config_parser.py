import configparser

class ReadProperties:
    """parses the ini file to read config variables"""
    
    def __init__(self, file_name) -> None:
        self._file_name = file_name
        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(self._file_name)
    
    def get_config_section(self, section_name):
        section_dict = {}
        section_keys = self._config_parser.options(section_name)
        for key in section_keys:
            try:
                section_dict[key] = self._config_parser.get(section_name, key)
            except Exception:
                section_dict[key] = None
        return section_dict