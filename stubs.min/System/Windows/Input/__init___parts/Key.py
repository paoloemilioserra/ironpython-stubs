class Key(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible key values on a keyboard.
    
    enum Key, values: A (44), AbntC1 (147), AbntC2 (148), Add (85), Apps (72), Attn (163), B (45), Back (2), BrowserBack (122), BrowserFavorites (127), BrowserForward (123), BrowserHome (128), BrowserRefresh (124), BrowserSearch (126), BrowserStop (125), C (46), Cancel (1), Capital (8), CapsLock (8), Clear (5), CrSel (164), D (47), D0 (34), D1 (35), D2 (36), D3 (37), D4 (38), D5 (39), D6 (40), D7 (41), D8 (42), D9 (43), DbeAlphanumeric (157), DbeCodeInput (167), DbeDbcsChar (161), DbeDetermineString (169), DbeEnterDialogConversionMode (170), DbeEnterImeConfigureMode (165), DbeEnterWordRegisterMode (164), DbeFlushString (166), DbeHiragana (159), DbeKatakana (158), DbeNoCodeInput (168), DbeNoRoman (163), DbeRoman (162), DbeSbcsChar (160), DeadCharProcessed (172), Decimal (88), Delete (32), Divide (89), Down (26), E (48), End (21), Enter (6), EraseEof (166), Escape (13), Execute (29), ExSel (165), F (49), F1 (90), F10 (99), F11 (100), F12 (101), F13 (102), F14 (103), F15 (104), F16 (105), F17 (106), F18 (107), F19 (108), F2 (91), F20 (109), F21 (110), F22 (111), F23 (112), F24 (113), F3 (92), F4 (93), F5 (94), F6 (95), F7 (96), F8 (97), F9 (98), FinalMode (11), G (50), H (51), HangulMode (9), HanjaMode (12), Help (33), Home (22), I (52), ImeAccept (16), ImeConvert (14), ImeModeChange (17), ImeNonConvert (15), ImeProcessed (155), Insert (31), J (53), JunjaMode (10), K (54), KanaMode (9), KanjiMode (12), L (55), LaunchApplication1 (138), LaunchApplication2 (139), LaunchMail (136), Left (23), LeftAlt (120), LeftCtrl (118), LeftShift (116), LineFeed (4), LWin (70), M (56), MediaNextTrack (132), MediaPlayPause (135), MediaPreviousTrack (133), MediaStop (134), Multiply (84), N (57), Next (20), NoName (169), None (0), NumLock (114), NumPad0 (74), NumPad1 (75), NumPad2 (76), NumPad3 (77), NumPad4 (78), NumPad5 (79), NumPad6 (80), NumPad7 (81), NumPad8 (82), NumPad9 (83), O (58), Oem1 (140), Oem102 (154), Oem2 (145), Oem3 (146), Oem4 (149), Oem5 (150), Oem6 (151), Oem7 (152), Oem8 (153), OemAttn (157), OemAuto (160), OemBackslash (154), OemBackTab (162), OemClear (171), OemCloseBrackets (151), OemComma (142), OemCopy (159), OemEnlw (161), OemFinish (158), OemMinus (143), OemOpenBrackets (149), OemPeriod (144), OemPipe (150), OemPlus (141), OemQuestion (145), OemQuotes (152), OemSemicolon (140), OemTilde (146), P (59), Pa1 (170), PageDown (20), PageUp (19), Pause (7), Play (167), Print (28), PrintScreen (30), Prior (19), Q (60), R (61), Return (6), Right (25), RightAlt (121), RightCtrl (119), RightShift (117), RWin (71), S (62), Scroll (115), Select (27), SelectMedia (137), Separator (86), Sleep (73), Snapshot (30), Space (18), Subtract (87), System (156), T (63), Tab (3), U (64), Up (24), V (65), VolumeDown (130), VolumeMute (129), VolumeUp (131), W (66), X (67), Y (68), Z (69), Zoom (168)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    A = None
    AbntC1 = None
    AbntC2 = None
    Add = None
    Apps = None
    Attn = None
    B = None
    Back = None
    BrowserBack = None
    BrowserFavorites = None
    BrowserForward = None
    BrowserHome = None
    BrowserRefresh = None
    BrowserSearch = None
    BrowserStop = None
    C = None
    Cancel = None
    Capital = None
    CapsLock = None
    Clear = None
    CrSel = None
    D = None
    D0 = None
    D1 = None
    D2 = None
    D3 = None
    D4 = None
    D5 = None
    D6 = None
    D7 = None
    D8 = None
    D9 = None
    DbeAlphanumeric = None
    DbeCodeInput = None
    DbeDbcsChar = None
    DbeDetermineString = None
    DbeEnterDialogConversionMode = None
    DbeEnterImeConfigureMode = None
    DbeEnterWordRegisterMode = None
    DbeFlushString = None
    DbeHiragana = None
    DbeKatakana = None
    DbeNoCodeInput = None
    DbeNoRoman = None
    DbeRoman = None
    DbeSbcsChar = None
    DeadCharProcessed = None
    Decimal = None
    Delete = None
    Divide = None
    Down = None
    E = None
    End = None
    Enter = None
    EraseEof = None
    Escape = None
    Execute = None
    ExSel = None
    F = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F13 = None
    F14 = None
    F15 = None
    F16 = None
    F17 = None
    F18 = None
    F19 = None
    F2 = None
    F20 = None
    F21 = None
    F22 = None
    F23 = None
    F24 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    FinalMode = None
    G = None
    H = None
    HangulMode = None
    HanjaMode = None
    Help = None
    Home = None
    I = None
    ImeAccept = None
    ImeConvert = None
    ImeModeChange = None
    ImeNonConvert = None
    ImeProcessed = None
    Insert = None
    J = None
    JunjaMode = None
    K = None
    KanaMode = None
    KanjiMode = None
    L = None
    LaunchApplication1 = None
    LaunchApplication2 = None
    LaunchMail = None
    Left = None
    LeftAlt = None
    LeftCtrl = None
    LeftShift = None
    LineFeed = None
    LWin = None
    M = None
    MediaNextTrack = None
    MediaPlayPause = None
    MediaPreviousTrack = None
    MediaStop = None
    Multiply = None
    N = None
    Next = None
    NoName = None
    None = None
    NumLock = None
    NumPad0 = None
    NumPad1 = None
    NumPad2 = None
    NumPad3 = None
    NumPad4 = None
    NumPad5 = None
    NumPad6 = None
    NumPad7 = None
    NumPad8 = None
    NumPad9 = None
    O = None
    Oem1 = None
    Oem102 = None
    Oem2 = None
    Oem3 = None
    Oem4 = None
    Oem5 = None
    Oem6 = None
    Oem7 = None
    Oem8 = None
    OemAttn = None
    OemAuto = None
    OemBackslash = None
    OemBackTab = None
    OemClear = None
    OemCloseBrackets = None
    OemComma = None
    OemCopy = None
    OemEnlw = None
    OemFinish = None
    OemMinus = None
    OemOpenBrackets = None
    OemPeriod = None
    OemPipe = None
    OemPlus = None
    OemQuestion = None
    OemQuotes = None
    OemSemicolon = None
    OemTilde = None
    P = None
    Pa1 = None
    PageDown = None
    PageUp = None
    Pause = None
    Play = None
    Print = None
    PrintScreen = None
    Prior = None
    Q = None
    R = None
    Return = None
    Right = None
    RightAlt = None
    RightCtrl = None
    RightShift = None
    RWin = None
    S = None
    Scroll = None
    Select = None
    SelectMedia = None
    Separator = None
    Sleep = None
    Snapshot = None
    Space = None
    Subtract = None
    System = None
    T = None
    Tab = None
    U = None
    Up = None
    V = None
    value__ = None
    VolumeDown = None
    VolumeMute = None
    VolumeUp = None
    W = None
    X = None
    Y = None
    Z = None
    Zoom = None

