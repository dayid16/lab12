class Television:
    '''
    Class that displays a television power, muting, channel, and volume control options
    '''


    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initialize the television class with default settings: off, unmuted, minimum volume, and minimum channel.
        '''

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        When called, toggles the television power on or off.
        '''

        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        Toggles the mute option on and off only when the television power is on.
        '''

        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        '''
        Increases the television channel up by 1 only if the television power is on. If the channel status is at the maximum, then it returns to the minimum channel.
        '''

        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Decreases the television channel up by 1 only if the television power is on. If the channel status is at the mininum,then it returns to the maximum channel.
        '''

        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Increases the volume by 1 until it reaches the maximum volume. It only works if the television power is on. If the television is muted, it unmutes it.
        '''

        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decreases the volume by 1 until it reaches the minimum volume. It only works if the television power is on. If the television is muted, it unmutes it.
        '''

        if self.__status == True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns a string that displays the television power, channel, and volume status.
        '''
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'