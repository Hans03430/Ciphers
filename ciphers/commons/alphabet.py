class Alphabet:
    '''Class that represents the letters of the Alphabet in a language. It
    stores letters in uppercase and lowercase in the order given.
    
    Attributes
    ----------
    __lower: str
        String that contains the lowercase letters in the alphabet.

    __upper: str
        String that contains the uppercase letters in the alphabet.
    
    order_lower: Dict
        Dictionary that contains the order of the lowercase letters.

    upper_lower: Dict
        Dictionary that contains the order of the uppercase letters.

    language: str
        Name of the language the alphabet belongs to.
    '''

    __slots__=[
        '__lower',
        '__upper',
        'order_lower',
        'order_upper',
        'language'
    ]

    def __init__(
        self,
        language: str='',
        lower: str='',
        upper: str=''
    ) -> None:
        if len(lower) == 0 or len(upper) == 0:
            raise AttributeError('The alphabet is empty.')
            
        if len(lower) != len(upper):
            raise AttributeError(
                'The alphabet does not have the same amount of letters in \
                upper and lowercase.'
            )
        
        self.lower = lower
        self.upper = upper
        self.language = language

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str) -> None:
        self.__lower = lower
        self.order_lower = {v: k for k, v in enumerate(lower)}

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str) -> None:
        self.__upper = upper
        self.order_upper = {v: k for k, v in enumerate(upper)}

    def __len__(self) -> int:
        '''The amount of letters in the alphabet.
        
        Returns
        -------
        length: int
            The amount of letters in the alphabet.
        '''
        return len(self.lower)

    def __getitem__(self, key: str) -> int:
        '''Returns the order of a letter or the letter in upper or lowercase.

        To return the order of a letter, just write the letter itself in
        brackets. To return the letter, write the order and the case in a tuple.

        Examples
        --------
        # Order of a letter
        alphabet['a']
        alphabet['A']
        
        # Letter in lowercase
        alphabet[0, 'lower']

        # Letter in uppercase
        alphabet[0, 'upper']
        
        Parameters
        ----------
        key: str
            The letter whose order is being looked.
        
        Returns
        -------
        response: Union[str, int]
            Order of the letter in the alphabet or the letter itself.

        Raises
        ------
        KeyError
            When the key was introduced wrongly.
        '''
        if isinstance(key, str):
            return self.__get_order_of_letter(key)
        elif isinstance(key, tuple):
            return self.__get_letter_cased_by_order(key)
        else:
            raise KeyError('The key has a bad format.')

    def __get_order_of_letter(self, key: str) -> int:
        '''Returns the order of a letter in the alphabet.

        Parameters
        ----------
        key: str
            The letter to search for.

        Returns
        -------
        order: int
            Order of the letter in the alphabet
        
        Raises
        ------
        KeyError
            When the letter does not belong to the alphabet.
        '''
        if key in self.order_lower:
            return self.order_lower[key]
        elif key in self.order_upper:
            return self.order_upper[key]
        else:
            raise KeyError(
                f'The letter "{key}" does not belong to the alphabet.'
            )

    def __get_letter_cased_by_order(self, key: tuple) -> int:
        '''Returns a letter, lower or uppercase, of the alphabet.

        Parameters
        ----------
        key: tuple
            The order and case of the letter to search for.

        Returns
        -------
        letter: str
            The letter in the alphabet
        
        Raises
        ------
        KeyError
            When the key has a bad format.
        '''
        order, case = key
        # Negative number error
        if order < 0:
            raise KeyError('Only positive numbers and 0 are allowed.')
        # Index out of bounds error
        if order > len(self):
            raise KeyError(
                f'The alphabet only has {len(self)} letters, not {order}.'
            )

        # Search in the lists
        if case.lower() == 'lower':
            return self.lower[order]
        elif case.lower() == 'upper':
            return self.upper[order]
        else:
            raise KeyError(
                'Unsupported type of case. Just "lower" and "upper" is allowed.'
            )
