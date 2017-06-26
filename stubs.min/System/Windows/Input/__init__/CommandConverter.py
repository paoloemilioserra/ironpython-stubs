class CommandConverter(TypeConverter):
    """
    Converts an System.Windows.Input.ICommand object to and from other types.
    
    CommandConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CommandConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.ICommand, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CommandConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.ICommand can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CommandConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to an System.Windows.Input.ICommand, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object, or null if source is an empty string.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CommandConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an System.Windows.Input.ICommand to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object, or an empty string.
        """
        pass

