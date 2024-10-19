class ObjectFactory:
    """Factory class to create objects based on the type from the goal map."""

    @staticmethod
    def create_object(type_string):
        """Method to parse the type string from the goal map and returns the appropriate parameters."""
        if type_string == "POLYANET":
            return {"type": "polyanets"}
        
        typ_string_list = type_string.split("_")
        arg_val = typ_string_list[0].lower()
        obj_type = typ_string_list[1].lower() + "s"

        if obj_type == "comeths":
            return {"type": obj_type, "direction": arg_val}
        elif obj_type == "soloons":
            return {"type": obj_type, "color": arg_val}

        return None