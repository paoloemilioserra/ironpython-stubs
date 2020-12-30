# encoding: utf-8
# module Autodesk.Civil.DynamoNodes calls itself DynamoNodes
# from Civil3DNodes, Version=13.3.860.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CivilObject(Object):
    # no doc
    @staticmethod
    def InternalMakeCivilObject(ent, isDynamoOwned):
        """ InternalMakeCivilObject(ent: Entity, isDynamoOwned: bool) -> CivilObject """
        pass

    def SetDescription(self, description):
        """
        SetDescription(self: CivilObject, description: str) -> CivilObject
        
            Consente di impostare la descrizione dell'oggetto Civil.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: CivilObject, name: str) -> CivilObject
        
            Imposta il nome dell'oggetto di Civil.
        """
        pass

    def ToString(self):
        """ ToString(self: CivilObject) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, entity: Entity, isDynamoOwned: bool) """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione dell'oggetto Civil.

Get: Description(self: CivilObject) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome dell'oggetto di Civil.

Get: Name(self: CivilObject) -> str

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Alignment(CivilObject):
    # no doc
    def CoordinateSystemByStationOffset(self, station, offset):
        """
        CoordinateSystemByStationOffset(self: Alignment, station: float, offset: float) -> CoordinateSystem
        
            Consente di ottenere il sistema di coordinate per una progressiva e uno 
             scostamento specifici.
        """
        pass

    def NearestAlignment(self, referenceAlignments):
        """ NearestAlignment(self: Alignment, referenceAlignments: IList[Alignment]) -> Dictionary[str, object] """
        pass

    def ProfileByName(self, name):
        """
        ProfileByName(self: Alignment, name: str) -> Profile
        
            Consente di ottenere il profilo in base a un nome specificato.
        """
        pass

    def StationOffsetByPoint(self, point):
        """
        StationOffsetByPoint(self: Alignment, point: Point) -> Dictionary[str, float]
        
            Ottenere la progressiva e lo scostamento per punto.
        """
        pass

    def Stations(self, interval, includeGeometryStations):
        """
        Stations(self: Alignment, interval: float, includeGeometryStations: bool) -> IList[float]
        
            Consente di ottenere le progressive del tracciato.
        """
        pass

    def ToString(self):
        """ ToString(self: Alignment) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva finale del tracciato.

Get: EndStation(self: Alignment) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la lunghezza del tracciato.

Get: Length(self: Alignment) -> float

"""

    Profiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i profili dal tracciato.

Get: Profiles(self: Alignment) -> IList[Profile]

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva iniziale del tracciato.

Get: StartStation(self: Alignment) -> float

"""


    IsDynamoOwned = None
    ObjectHandle = None


class AppliedSubassembly(object):
    # no doc
    def SetParameterByName(self, name, value, rebuild):
        """
        SetParameterByName(self: AppliedSubassembly, name: str, value: object, rebuild: bool) -> AppliedSubassembly
        
            Imposta il valore di un parametro con nome.
        """
        pass

    def ToString(self):
        """ ToString(self: AppliedSubassembly) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del componente sezione tipo.

Get: Name(self: AppliedSubassembly) -> str

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i parametri dal componente sezione tipo.

Get: Parameters(self: AppliedSubassembly) -> IList[SubassemblyParameter]

"""



class Baseline(object):
    # no doc
    def Codes(self):
        """
        Codes(self: Baseline) -> Dictionary[str, object]
        
            Consente di ottenere i codici della linea base.
        """
        pass

    def CoordinateSystemByStation(self, station, vertical):
        """
        CoordinateSystemByStation(self: Baseline, station: float, vertical: bool) -> CoordinateSystem
        
            Consente di ottenere il sistema di coordinate da una progressiva associata alla 
             linea di base.
        """
        pass

    def CorridorFeatureLinesByCode(self, code):
        """
        CorridorFeatureLinesByCode(self: Baseline, code: str) -> IList[CorridorFeatureLine]
        
            Consente di ottenere le linee caratteristiche della linea base in base ad un 
             nome codice specificato.
        """
        pass

    def ElevationByStation(self, station):
        """
        ElevationByStation(self: Baseline, station: float) -> float
        
            Consente di ottenere la quota altimetrica della linea base in corrispondenza di 
             una progressiva specificata.
        """
        pass

    def PointByStationOffsetElevation(self, station, offset, elevationOffset):
        """
        PointByStationOffsetElevation(self: Baseline, station: float, offset: float, elevationOffset: float) -> Point
        
            Consente di ottenere il punto in base a progressiva, scostamento e scostamento 
             quota altimetrica rispetto alla linea base.
        """
        pass

    def PointsByLinkCodeAtNearestStation(self, station, code):
        """
        PointsByLinkCodeAtNearestStation(self: Baseline, station: float, code: str) -> Dictionary[str, object]
        
            Consente di ottenere un elenco di punti in corrispondenza della progressiva 
             della linea base del modellatore pi? vicina che forma i collegamenti di un 
             codice collegamento specificato.
        """
        pass

    def PointsByPointCodeAtNearestStation(self, station, code):
        """
        PointsByPointCodeAtNearestStation(self: Baseline, station: float, code: str) -> Dictionary[str, object]
        
            Consente di ottenere un elenco di punti in corrispondenza della progressiva 
             della linea base del modellatore pi? vicina che dispone del codice punto 
             specificato.
        """
        pass

    def PointsByShapeCodeAtNearestStation(self, station, code):
        """
        PointsByShapeCodeAtNearestStation(self: Baseline, station: float, code: str) -> Dictionary[str, object]
        
            Consente di ottenere un elenco di punti in corrispondenza della progressiva 
             della linea di base del modellatore pi? vicina che determina le forme di un 
             codice forma specificato.
        """
        pass

    def PolyCurveByRange(self, startStn, endStn, offset, elevationOffset):
        """
        PolyCurveByRange(self: Baseline, startStn: float, endStn: float, offset: float, elevationOffset: float) -> PolyCurve
        
            Consente di ottenere la PolyCurve della linea base in base ad un intervallo 
             progressive, uno scostamento e uno scostamento quota altimetrica specificati.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: Baseline, name: str) -> Baseline
        
            Imposta il nome della linea base.
        """
        pass

    def StationOffsetByPoint(self, point):
        """
        StationOffsetByPoint(self: Baseline, point: Point) -> Dictionary[str, object]
        
            Consente di ottenere la progressiva e lo scostamento in corrispondenza di un 
             punto specificato.
        """
        pass

    def SubassembliesByStation(self, station):
        """
        SubassembliesByStation(self: Baseline, station: float) -> IList[AppliedSubassembly]
        
            Consente di ottenere tutti i componenti sezione tipo in corrispondenza di una 
             progressiva specificata.
        """
        pass

    def ToString(self):
        """ ToString(self: Baseline) -> str """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il tracciato associato alla linea base.

Get: Alignment(self: Baseline) -> Alignment

"""

    Corridor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il modellatore associato alla linea base.

Get: Corridor(self: Baseline) -> Corridor

"""

    CorridorFeatureLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le linee caratteristiche associate alla linea di base.

Get: CorridorFeatureLines(self: Baseline) -> IList[CorridorFeatureLine]

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva finale della linea base.

Get: EndStation(self: Baseline) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il numero di indice della linea base.

Get: Index(self: Baseline) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome della linea base.

Get: Name(self: Baseline) -> str

"""

    PolyCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la PolyCurve della linea base.

Get: PolyCurve(self: Baseline) -> PolyCurve

"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il profilo associato alla linea base.

Get: Profile(self: Baseline) -> Profile

"""

    Regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le regioni della linea base.

Get: Regions(self: Baseline) -> IList[BaselineRegion]

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva iniziale della linea base.

Get: StartStation(self: Baseline) -> float

"""

    Stations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le progressive lungo la linea base.

Get: Stations(self: Baseline) -> Array[float]

"""



class BaselineRegion(object):
    # no doc
    def SetName(self, name):
        """
        SetName(self: BaselineRegion, name: str) -> BaselineRegion
        
            Imposta il nome dell'area della linea base.
        """
        pass

    def ToString(self):
        """ ToString(self: BaselineRegion) -> str """
        pass

    Baseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ottenere la linea base della regione.

Get: Baseline(self: BaselineRegion) -> Baseline

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva finale della regione.

Get: EndStation(self: BaselineRegion) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il numero di indice della regione linea base.

Get: Index(self: BaselineRegion) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome dell'area della linea base.

Get: Name(self: BaselineRegion) -> str

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva iniziale della regione.

Get: StartStation(self: BaselineRegion) -> float

"""

    Stations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le progressive nella regione.

Get: Stations(self: BaselineRegion) -> Array[float]

"""



class Civil3DObjectDescriptors(object):
    """ Civil3DObjectDescriptors() """
    def RegisterDescriptors(self):
        """ RegisterDescriptors(self: Civil3DObjectDescriptors) """
        pass


class CogoPoint(Object):
    # no doc
    @staticmethod
    def ByBlockReference(blockReference, layer, document, name, rawDescription):
        """
        ByBlockReference(blockReference: BlockReference, layer: str, document: Document, name: str, rawDescription: str) -> CogoPoint
        
            Crea punti COGO in base al riferimento blocco.
        """
        pass

    @staticmethod
    def ByGeometry(geometry, layer, document, name, rawDescription):
        """
        ByGeometry(geometry: Point, layer: str, document: Document, name: str, rawDescription: str) -> CogoPoint
        
            Crea un punto COGO da un punto Dynamo.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: CogoPoint, name: str) -> CogoPoint
        
            Imposta il nome dei punti COGO selezionati
        """
        pass

    def SetRawDescription(self, rawDescription):
        """
        SetRawDescription(self: CogoPoint, rawDescription: str) -> CogoPoint
        
            Imposta una descrizione originaria dei punti COGO selezionati
        """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FullDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione completa dei punti COGO selezionati

Get: FullDescription(self: CogoPoint) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome dei punti COGO selezionati

Get: Name(self: CogoPoint) -> str

"""

    RawDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione originaria dei punti COGO selezionati

Get: RawDescription(self: CogoPoint) -> str

"""


    IsDynamoOwned = None
    ObjectHandle = None


class CogoPointGroup(ObjectBase):
    # no doc
    @staticmethod
    def ByCogoPoints(cogoPoints, cogoPointGroupName, document, description):
        """ ByCogoPoints(cogoPoints: IList[CogoPoint], cogoPointGroupName: str, document: Document, description: str) -> CogoPointGroup """
        pass

    def SetDescription(self, description):
        """
        SetDescription(self: CogoPointGroup, description: str) -> CogoPointGroup
        
            Imposta una descrizione per il gruppo di punti COGO selezionato
        """
        pass

    def SetName(self, name):
        """
        SetName(self: CogoPointGroup, name: str) -> CogoPointGroup
        
            Imposta un nome per il gruppo di punti COGO selezionato
        """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CogoPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i punti COGO da un gruppo di punti.

Get: CogoPoints(self: CogoPointGroup) -> IList[CogoPoint]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione del gruppo di punti COGO selezionato

Get: Description(self: CogoPointGroup) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del gruppo di punti COGO.

Get: Name(self: CogoPointGroup) -> str

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Corridor(CivilObject):
    # no doc
    def BaselineByName(self, name):
        """
        BaselineByName(self: Corridor, name: str) -> Baseline
        
            Consente di ottenere una linea base specificata in base al suo nome dal 
             modellatore.
        """
        pass

    def Codes(self):
        """
        Codes(self: Corridor) -> Dictionary[str, object]
        
            Consente di ottenere i codici del modellatore.
        """
        pass

    def GetSolids(self, baselineName, regionName, assemblyName, codeName, side):
        """
        GetSolids(self: Corridor, baselineName: str, regionName: str, assemblyName: str, codeName: str, side: str) -> IList[Solid]
        
            Consente di ottenere solidi generati dal modellatore, filtrati in base ai 
             valori delle propriet? dei solidi.
        """
        pass

    def Rebuild(self):
        """
        Rebuild(self: Corridor) -> Corridor
        
            Ricostruisce il modellatore.
        """
        pass

    def SurfaceByName(self, name):
        """
        SurfaceByName(self: Corridor, name: str) -> Object
        
            Selezionare una superficie di propriet? del modellatore utilizzando il nome 
             specificato.
        """
        pass

    def ToString(self):
        """ ToString(self: Corridor) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Baselines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le linee base dal modellatore.

Get: Baselines(self: Corridor) -> IList[Baseline]

"""

    Surfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Selezionare tutte le superfici di propriet? del modellatore.

Get: Surfaces(self: Corridor) -> IList[Object]

"""


    IsDynamoOwned = None
    ObjectHandle = None


class CorridorFeatureLine(object):
    # no doc
    def CoordinateSystemByStation(self, station, vertical):
        """
        CoordinateSystemByStation(self: CorridorFeatureLine, station: float, vertical: bool) -> CoordinateSystem
        
            Consente di ottenere il sistema di coordinate in corrispondenza di una 
             progressiva specificata.
        """
        pass

    def Dispose(self):
        """ Dispose(self: CorridorFeatureLine) """
        pass

    def OffsetElevationByStation(self, station):
        """
        OffsetElevationByStation(self: CorridorFeatureLine, station: float) -> Dictionary[str, object]
        
            Consente di ottenere lo scostamento e la quota altimetrica in corrispondenza di 
             una progressiva specificata.
        """
        pass

    def ToString(self):
        """ ToString(self: CorridorFeatureLine) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome codice associato alla linea caratteristica.

Get: Code(self: CorridorFeatureLine) -> str

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva finale della linea caratteristica.

Get: EndStation(self: CorridorFeatureLine) -> float

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i punti della linea caratteristica.

Get: Points(self: CorridorFeatureLine) -> IList[Point]

"""

    PolyCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la PolyCurve della linea caratteristica.

Get: PolyCurve(self: CorridorFeatureLine) -> PolyCurve

"""

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il lato della linea caratteristica. Se il lato ? quello sinistro, questa operazione restituisce -1.0, altrimenti 1.0.

Get: Side(self: CorridorFeatureLine) -> float

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva iniziale della linea caratteristica.

Get: StartStation(self: CorridorFeatureLine) -> float

"""



class Surface(CivilObject):
    # no doc
    def ElevationByXY(self, x, y):
        """
        ElevationByXY(self: Surface, x: float, y: float) -> float
        
            Consente di ottenere la quota altimetrica in corrispondenza di una posizione 
             specifica della superficie.
        """
        pass

    def IntersectionPoints(self, coordinateSystem, slope, side):
        """
        IntersectionPoints(self: Surface, coordinateSystem: CoordinateSystem, slope: float, side: str) -> Point
        
            Consente di ottenere i vertici planimetrici della superficie.
        """
        pass

    def QuickProfileByObject(self, obj):
        """
        QuickProfileByObject(self: Surface, obj: Object) -> PolyCurve
        
            Consente di ottenere una PolyCurve contenente il profilo rapido della 
             superficie in base all'oggetto.
        """
        pass

    def QuickProfileByPoints(self, points):
        """ QuickProfileByPoints(self: Surface, points: IList[Point]) -> PolyCurve """
        pass

    def Rebuild(self):
        """
        Rebuild(self: Surface) -> Surface
        
            Ricrea la superficie.
        """
        pass

    @staticmethod
    def SamplePoint(surface, point):
        """
        SamplePoint(surface: Surface, point: Point) -> Point
        
            Consente di ottenere i punti campione sulla superficie.
        """
        pass

    def TerrainStatistics(self):
        """
        TerrainStatistics(self: Surface) -> Dictionary[str, object]
        
            Consente di ottenere la statica del terreno della superficie.
        """
        pass

    def ToString(self):
        """ ToString(self: Surface) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Boundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere PolyCurve chiuse dei contorni della superficie.

Get: Boundaries(self: Surface) -> IList[PolyCurve]

"""


    IsDynamoOwned = None
    ObjectHandle = None


class GridSurface(Surface):
    # no doc
    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Profile(CivilObject):
    # no doc
    def CoordinateSystemByStation(self, station, vertical):
        """
        CoordinateSystemByStation(self: Profile, station: float, vertical: bool) -> CoordinateSystem
        
            Consente di ottenere il sistema di coordinate di una progressiva specificata.
        """
        pass

    def ElevationByStation(self, station):
        """
        ElevationByStation(self: Profile, station: float) -> float
        
            Consente di ottenere la quota altimetrica in corrispondenza di una progressiva 
             specificata del profilo.
        """
        pass

    def ElevationRange(self):
        """
        ElevationRange(self: Profile) -> Dictionary[str, float]
        
            Consente di ottenere l'intervallo di quota altimetrica del profilo.
        """
        pass

    def GradeByStation(self, station):
        """
        GradeByStation(self: Profile, station: float) -> float
        
            Consente di ottenere la pendenza in una progressiva specificata del profilo.
        """
        pass

    def PolyCurveByRange(self, startStation, endStation, offset, elevationOffset, interval, includeGeometryStations):
        """
        PolyCurveByRange(self: Profile, startStation: float, endStation: float, offset: float, elevationOffset: float, interval: float, includeGeometryStations: bool) -> PolyCurve
        
            Consente di ottenere la PolyCurve della linea base da un intervallo di 
             progressive, dalla frequenza, dallo scostamento e dallo scostamento quota 
             altimetrica specificati.
        """
        pass

    def StationOffsetByPoint(self, point):
        """
        StationOffsetByPoint(self: Profile, point: Point) -> Dictionary[str, float]
        
            Ottenere la progressiva e lo scostamento per punto.
        """
        pass

    def ToString(self):
        """ ToString(self: Profile) -> str """
        pass

    def UpdateForEvaluation(self):
        """ UpdateForEvaluation(self: Profile) """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il tracciato principale del profilo.

Get: Alignment(self: Profile) -> Alignment

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva finale del profilo.

Get: EndStation(self: Profile) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la lunghezza del profilo.

Get: Length(self: Profile) -> float

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la progressiva iniziale del profilo.

Get: StartStation(self: Profile) -> float

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Selection(object):
    # no doc
    @staticmethod
    def AlignmentByName(name, document):
        """
        AlignmentByName(name: str, document: Document) -> Alignment
        
            Seleziona un tracciato in base ad un nome tracciato specificato.
        """
        pass

    @staticmethod
    def Alignments(document):
        """
        Alignments(document: Document) -> IList[Alignment]
        
            Seleziona tutti i tracciati nella Carta.
        """
        pass

    @staticmethod
    def CogoPointGroupByName(name, document):
        """
        CogoPointGroupByName(name: str, document: Document) -> CogoPointGroup
        
            Seleziona un gruppo di punti COGO in base ad un nome specificato.
        """
        pass

    @staticmethod
    def CogoPointGroups(document):
        """
        CogoPointGroups(document: Document) -> IList[CogoPointGroup]
        
            Seleziona tutti i gruppi di punti COGO nella Carta.
        """
        pass

    @staticmethod
    def CorridorByName(name, document):
        """
        CorridorByName(name: str, document: Document) -> Corridor
        
            Seleziona un modellatore in base ad un nome modellatore specificato.
        """
        pass

    @staticmethod
    def Corridors(document):
        """
        Corridors(document: Document) -> IList[Corridor]
        
            Seleziona tutti i modellatori nella Carta.
        """
        pass

    @staticmethod
    def SurfaceByName(name, document):
        """
        SurfaceByName(name: str, document: Document) -> Surface
        
            Seleziona una superficie in base ad un nome superficie specificato.
        """
        pass

    @staticmethod
    def Surfaces(document):
        """
        Surfaces(document: Document) -> IList[Surface]
        
            Seleziona tutte le superfici nella Carta.
        """
        pass


class SubassemblyParameter(object):
    # no doc
    def ToString(self):
        """ ToString(self: SubassemblyParameter) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del parametro.

Get: Name(self: SubassemblyParameter) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il tipo del parametro.

Get: Type(self: SubassemblyParameter) -> Type

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il valore del parametro.

Get: Value(self: SubassemblyParameter) -> object

"""



class TinSurface(Surface):
    # no doc
    @staticmethod
    def ByCogoPointGroup(cogoPointGroupName, surfaceName, layer, document):
        """
        ByCogoPointGroup(cogoPointGroupName: str, surfaceName: str, layer: str, document: Document) -> TinSurface
        
            Crea la superficie TIN in base a gruppo di punti COGO.
        """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere i triangoli della superficie.

Get: Triangles(self: TinSurface) -> IList[PolyCurve]

"""


    IsDynamoOwned = None
    ObjectHandle = None


