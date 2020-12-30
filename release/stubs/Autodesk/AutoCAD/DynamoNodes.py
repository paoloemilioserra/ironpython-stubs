# encoding: utf-8
# module Autodesk.AutoCAD.DynamoNodes calls itself DynamoNodes
# from AutoCADNodes, Version=13.3.860.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutoCADObjectDescriptors(object):
    """ AutoCADObjectDescriptors() """
    def RegisterDescriptors(self):
        """ RegisterDescriptors(self: AutoCADObjectDescriptors) """
        pass


class AutoCADUtility(object):
    # no doc
    @staticmethod
    def ConvertUnitToDynamo(unit):
        """ ConvertUnitToDynamo(unit: UnitsValue) -> ConversionUnit """
        pass

    @staticmethod
    def CooridnateSystemToMatrix(coordinateSystem):
        """ CooridnateSystemToMatrix(coordinateSystem: CoordinateSystem) -> Matrix3d """
        pass

    @staticmethod
    def EnsureLayer(ctx, layer):
        """
        EnsureLayer(ctx: DocumentContext, layer: str)
            Verifica che un layer specificato esista nella Carta corrente. In caso 
             contrario, crea un nuovo layer.
        """
        pass

    @staticmethod
    def FilterByValueOperator(value, referenceValue, valueOperator):
        """ FilterByValueOperator(value: object, referenceValue: object, valueOperator: str) -> bool """
        pass

    @staticmethod
    def GetBlockByName(name, acdocument):
        """ GetBlockByName(name: str, acdocument: Document) -> Block """
        pass

    @staticmethod
    def GetBlockColor(entity):
        """
        GetBlockColor(entity: Entity) -> Color
        
            Consente di ottenere il colore blocco di un'entit? di AutoCAD.
        """
        pass

    @staticmethod
    def GetConverionFactor(satfile):
        """ GetConverionFactor(satfile: str) -> float """
        pass

    @staticmethod
    def GetModelSpaceId(ctx):
        """ GetModelSpaceId(ctx: DocumentContext) -> ObjectId """
        pass

    @staticmethod
    def MatrixToCoordinateSystem(matrix):
        """ MatrixToCoordinateSystem(matrix: Matrix3d) -> CoordinateSystem """
        pass

    @staticmethod
    def PrintMessage(message):
        """
        PrintMessage(message: str)
            Stampa una riga del messaggio sulla riga di comando di AutoCAD o nella finestra 
             della console di AcCoreConsole.
                    Il messaggio verr? aggiunto 
             automaticamente con \r\n.
        """
        pass

    @staticmethod
    def RemoveDuplicationPoints(points, tolerance):
        """ RemoveDuplicationPoints(points: IList[Point], tolerance: float) -> IList[Point] """
        pass

    HorizontalModes = None
    ValueOperators = None
    VerticalModes = None
    __all__ = [
        'ConvertUnitToDynamo',
        'CooridnateSystemToMatrix',
        'EnsureLayer',
        'FilterByValueOperator',
        'GetBlockByName',
        'GetBlockColor',
        'GetConverionFactor',
        'GetModelSpaceId',
        'HorizontalModes',
        'MatrixToCoordinateSystem',
        'PrintMessage',
        'RemoveDuplicationPoints',
        'ValueOperators',
        'VerticalModes',
    ]


class Block(object):
    # no doc
    def AttributeDefaultValueByTag(self, tag):
        """
        AttributeDefaultValueByTag(self: Block, tag: str) -> str
        
            Consente di ottenere la stringa di testo di default dell'attributo del blocco 
             con l'indicatore specificato.
        """
        pass

    @staticmethod
    def Import(drawingFileName, blockName, overwrite, document):
        """
        Import(drawingFileName: str, blockName: str, overwrite: bool, document: Document) -> Block
        
            Importa un blocco da un file cartografico esterno.
        """
        pass

    def SetAttributeDefaultValueByTag(self, tag, value):
        """
        SetAttributeDefaultValueByTag(self: Block, tag: str, value: str) -> Block
        
            Imposta la stringa di testo di default dell'attributo del blocco con 
             l'indicatore specificato.
        """
        pass

    def SetDescription(self, description):
        """
        SetDescription(self: Block, description: str) -> Block
        
            Imposta la descrizione di un blocco.
        """
        pass

    def ToString(self):
        """ ToString(self: Block) -> str """
        pass

    AttributeDefinitionTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ottenere tutti gli indicatori di attributo definiti da questo blocco.

Get: AttributeDefinitionTags(self: Block) -> IList[str]

"""

    BlockReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ottenere tutti i riferimenti in blocco del blocco.

Get: BlockReferences(self: Block) -> IList[BlockReference]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione di un blocco.

Get: Description(self: Block) -> str

"""

    Extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ottenere le estensioni di un blocco.

Get: Extents(self: Block) -> BoundingBox

"""

    HasAttributeDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ottenere se questo blocco contiene attributi definiti.

Get: HasAttributeDefinitions(self: Block) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del blocco.

Get: Name(self: Block) -> str

"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenre gli oggetti di un blocco.

Get: Objects(self: Block) -> IList[Object]

"""



class Traceable(object):
    # no doc
    def Delete(self):
        """ Delete(self: Traceable) """
        pass

    def Dispose(self):
        """ Dispose(self: Traceable) """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: Traceable, id: ObjectId, isDynamoOwned: bool)SetHandle(self: Traceable, handle: str, isDynamoOwned: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Propriet? che contiene il gestore dell'oggetto

Get: Handle(self: Traceable) -> str

"""


    IsDynamoOwned = None
    ObjectHandle = None


class ObjectBase(Traceable):
    # no doc
    def CommonConstruct(self, *args): #cannot find CLR method
# Error generating skeleton for function CommonConstruct: Method must be called on a Type for which Type.IsGenericParameter is false.

    def ConstructDynamoInstance(self, *args): #cannot find CLR method
# Error generating skeleton for function ConstructDynamoInstance: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Delete(self):
        """ Delete(self: ObjectBase) """
        pass

    def DoDelete(self, *args): #cannot find CLR method
        """ DoDelete(self: ObjectBase, ctx: DocumentContext) """
        pass

    @staticmethod
    def InternalMakeObject(obj, isDynamoOwned):
        """ InternalMakeObject(obj: DBObject, isDynamoOwned: bool) -> ObjectBase """
        pass

    def UpdateForEvaluation(self):
        """ UpdateForEvaluation(self: ObjectBase) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, obj: DBObject, isDynamoOwned: bool) """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalDBObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalDBObject(self: ObjectBase) -> DBObject

"""

    InternalObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalObjectId(self: ObjectBase) -> ObjectId

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Object(ObjectBase):
    """ Rappresenta un'entit? di AutoCAD, utilizzare 'Oggetto' come termine per il cliente. """
    def AddPropertySet(self, propertySetDefinitionName):
        """
        AddPropertySet(self: Object, propertySetDefinitionName: str) -> Object
        
            Aggiunge un gruppo di propriet? all'oggetto in base al nome di definizione del 
             gruppo di propriet?.
        """
        pass

    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Geometry, layer: str, block: Block) -> Object
        
            Crea un oggetto di AutoCAD da una geometria di Dynamo.
        """
        pass

    def Copy(self, basePoint, location):
        """
        Copy(self: Object, basePoint: Point, location: Point) -> Object
        
            Consente di copiare questo oggetto.
        """
        pass

    def Delete(self):
        """
        Delete(self: Object)
            Elimina questo oggetto.
        """
        pass

    def DoExportGeometry(self, *args): #cannot find CLR method
        """ DoExportGeometry(self: Object) -> Geometry """
        pass

    def Explode(self):
        """
        Explode(self: Object) -> IList[Object]
        
            Consente di esplodere questo oggetto.
        """
        pass

    @staticmethod
    def FilterByProperty(objects, propertySetName, propertyName, propertyValue, valueOperator):
        """ FilterByProperty(objects: IList[Object], propertySetName: str, propertyName: str, propertyValue: object, valueOperator: str) -> IList[Object] """
        pass

    def InsertEntityToBlockTable(self, *args): #cannot find CLR method
        """ InsertEntityToBlockTable(ctx: DocumentContext, entity: Entity, blockId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def InternalMakeObject(ent, isDynamoOwned):
        """ InternalMakeObject(ent: Entity, isDynamoOwned: bool) -> Object """
        pass

    def PropertySetByDefiniton(self, psd):
        """
        PropertySetByDefiniton(self: Object, psd: PropertySetDefinition) -> PropertySet
        
            Consente di ottenere il gruppo di propriet? in base alla sua definizione.
        """
        pass

    def PropertySetByName(self, propertySetDefinitionName):
        """
        PropertySetByName(self: Object, propertySetDefinitionName: str) -> PropertySet
        
            Consente di ottenere il gruppo di propriet? in base al nome della sua 
             definizione.
        """
        pass

    def RemovePropertySet(self, propertySetDefinitionName):
        """
        RemovePropertySet(self: Object, propertySetDefinitionName: str) -> Object
        
            Rimuove un gruppo di propriet? dall'oggetto in base al nome di definizione del 
             gruppo di propriet?.
        """
        pass

    def SetColor(self, color):
        """
        SetColor(self: Object, color: Color) -> Object
        
            Imposta il colore di questo oggetto.
        """
        pass

    def SetLayer(self, layer):
        """
        SetLayer(self: Object, layer: str) -> Object
        
            Imposta il layer di questo oggetto.
        
            layer: Nome del layer
        """
        pass

    def ToString(self):
        """ ToString(self: Object) -> str """
        pass

    def Transform(self, coordinateSystem):
        """
        Transform(self: Object, coordinateSystem: CoordinateSystem) -> Object
        
            Trasforma l'oggetto in base all'input della matrice CoordinateSystem.
        """
        pass

    def UpdateProperty(self, propertySetName, propertyName, propertyValue):
        """
        UpdateProperty(self: Object, propertySetName: str, propertyName: str, propertyValue: str) -> Object
        
            Aggiorna il valore della propriet? in base al nome del gruppo di propriet?, al 
             nome propriet? e al valore propriet?.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ent: Entity, isDynamoOwned: bool) """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il colore di questo oggetto.

Get: Color(self: Object) -> Color

"""

    Extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenre le estensioni di un oggetto.

Get: Extents(self: Object) -> BoundingBox

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la rappresentazione di Dynamo di questo oggetto.

Get: Geometry(self: Object) -> Geometry

"""

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome layer di questo oggetto.

Get: Layer(self: Object) -> str

"""

    PropertySets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i gruppi di propriet? dall'oggetto.

Get: PropertySets(self: Object) -> IList[PropertySet]

"""


    IsDynamoOwned = None
    ObjectHandle = None


class BlockReference(Object):
    # no doc
    def AttributeByTag(self, tag):
        """
        AttributeByTag(self: BlockReference, tag: str) -> str
        
            Consente di ottenere la stringa di testo dell'attributo del riferimento blocco 
             con l'indicatore specificato.
        """
        pass

    @staticmethod
    def ByCoordinateSystem(sourceBlock, coordinateSystem, layer, block):
        """
        ByCoordinateSystem(sourceBlock: Block, coordinateSystem: CoordinateSystem, layer: str, block: Block) -> BlockReference
        
            Crea un riferimento blocco in base al sistema di coordinate.
        """
        pass

    @staticmethod
    def Create(sourceBlock, position, normal, rotationDegrees, scaleFactors, layer, block):
        """
        Create(sourceBlock: Block, position: Point, normal: Vector, rotationDegrees: float, scaleFactors: Vector, layer: str, block: Block) -> BlockReference
        
            Crea un blocco.
        """
        pass

    def DynamicPropertyByName(self, name):
        """
        DynamicPropertyByName(self: BlockReference, name: str) -> Dictionary[str, object]
        
            Consente di ottenere la propriet? dinamica specificata dal rispettivo nome nel 
             riferimento blocco.
        """
        pass

    def SetAttributeByTag(self, tag, value):
        """
        SetAttributeByTag(self: BlockReference, tag: str, value: str) -> BlockReference
        
            Consente di impostare la stringa di testo dell'attributo del riferimento blocco 
             con l'indicatore specificato.
                    Se l'attributo non ? definito, verr? 
             aggiunto.
        """
        pass

    def SetDynamicPropertyByName(self, name, value):
        """
        SetDynamicPropertyByName(self: BlockReference, name: str, value: object) -> BlockReference
        
            Imposta il valore della propriet? dinamica specificata dal rispettivo nome nel 
             riferimento blocco.
        """
        pass

    def ToString(self):
        """ ToString(self: BlockReference) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AttributeTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti gli indicatori di attributi contenuti in questo riferimento blocco.

Get: AttributeTags(self: BlockReference) -> IList[str]

"""

    Block = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di recuperare il blocco utilizzato da questo riferimento blocco.

Get: Block(self: BlockReference) -> Block

"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenre il sistema di coordinate di un blocco.

Get: CoordinateSystem(self: BlockReference) -> CoordinateSystem

"""

    DynamicPropertyNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di recuperare i nomi delle propriet? dinamiche contenute nel riferimento blocco.

Get: DynamicPropertyNames(self: BlockReference) -> IList[str]

"""

    HasAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indica se questo riferimento blocco dispone di un attributo specificato.

Get: HasAttributes(self: BlockReference) -> bool

"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di verificare se il riferimento blocco contiene propriet? dinamiche.

Get: IsDynamic(self: BlockReference) -> bool

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Circle(Object):
    # no doc
    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Circle, layer: str, block: Block) -> Circle
        
            Crea un cerchio di AutoCAD da un cerchio di Dynamo.
        """
        pass

    def ToString(self):
        """ ToString(self: Circle) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Document(object):
    # no doc
    def BlockByName(self, name):
        """
        BlockByName(self: Document, name: str) -> Block
        
            Consente di ottenere un record della tabella del blocco in base ad un nome 
             specificato.
        """
        pass

    @staticmethod
    def Detail(document):
        """
        Detail(document: Document) -> Dictionary[str, str]
        
            Consente di ottenere il nome della cartella e del file di questo documento.
        """
        pass

    def LayerByName(self, name):
        """
        LayerByName(self: Document, name: str) -> Layer
        
            Consente di ottenere un layer con il nome specificato.
        """
        pass

    def PropertySetDefinitionByName(self, name):
        """
        PropertySetDefinitionByName(self: Document, name: str) -> PropertySetDefinition
        
            Consente di ottenere una definizione del gruppo di propriet? in base al nome 
             all'interno del documento.
        """
        pass

    def SetCurrentLayer(self, layer):
        """
        SetCurrentLayer(self: Document, layer: str) -> str
        
            Imposta il layer selezionato come layer corrente.
        """
        pass

    def ToString(self):
        """ ToString(self: Document) -> str """
        pass

    AcDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcDocument(self: Document) -> Document

"""

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i record della tabella del blocco dal documento corrente.

Get: Blocks(self: Document) -> IList[Block]

"""

    CurrentLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il layer corrente del documento corrente.

Get: CurrentLayer(self: Document) -> str

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i nomi layer dal documento corrente.

Get: Layers(self: Document) -> IList[str]

"""

    LineTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutti i nomi dei tipi di linea dal documento corrente.

Get: LineTypes(self: Document) -> IList[str]

"""

    ModelSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il record della tabella del blocco dello spazio modello.

Get: ModelSpace(self: Document) -> Block

"""

    PaperSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il record della tabella del blocco dello spazio carta.

Get: PaperSpace(self: Document) -> Block

"""

    PropertySetDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le definizioni del gruppo di propriet? all'interno del documento.

Get: PropertySetDefinitions(self: Document) -> IList[PropertySetDefinition]

"""


    Current = None


class Face(Object):
    # no doc
    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Face, layer: str, block: Block) -> Face
        
            Crea una faccia di AutoCAD da una faccia di Dynamo.
        """
        pass

    def ToString(self):
        """ ToString(self: Face) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la rappresentazione di Dynamo di questa faccia.

Get: Geometry(self: Face) -> Face

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Layer(object):
    # no doc
    @staticmethod
    def Create(name, document, color, linetype, lineweight):
        """
        Create(name: str, document: Document, color: Color, linetype: str, lineweight: str) -> Layer
        
            Crea un layer nel documento.
        """
        pass

    def SetColor(self, color):
        """
        SetColor(self: Layer, color: Color) -> Layer
        
            Imposta il colore del layer selezionato.
        """
        pass

    def SetDescription(self, description):
        """
        SetDescription(self: Layer, description: str) -> Layer
        
            Imposta la descrizione del layer.
        """
        pass

    def SetLinetype(self, linetype):
        """
        SetLinetype(self: Layer, linetype: str) -> Layer
        
            Imposta il tipo di linea del layer selezionato.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: Layer, name: str) -> Layer
        
            Imposta il nome del layer selezionato.
        """
        pass

    def ToString(self):
        """ ToString(self: Layer) -> str """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il colore del layer selezionato.

Get: Color(self: Layer) -> Color

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione del layer.

Get: Description(self: Layer) -> str

"""

    IsFrozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di verificare se il layer selezionato ? congelato.

Get: IsFrozen(self: Layer) -> bool

"""

    IsOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di verificare se il layer selezionato ? attivo.

Get: IsOn(self: Layer) -> bool

"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il tipo di linea del layer selezionato.

Get: Linetype(self: Layer) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del layer.

Get: Name(self: Layer) -> str

"""



class Line(Object):
    # no doc
    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Line, layer: str, block: Block) -> Line
        
            Crea una linea di AutoCAD da una linea di Dynamo.
        """
        pass

    @staticmethod
    def ByPointLengthDirection(startPoint, length, dir, layer, block):
        """
        ByPointLengthDirection(startPoint: Point, length: float, dir: Vector, layer: str, block: Block) -> Line
        
            Crea una linea di AutoCAD da un punto, una lunghezza e una direzione di Dynamo.
        """
        pass

    @staticmethod
    def ByTwoPoints(startPoint, endPoint, layer, block):
        """
        ByTwoPoints(startPoint: Point, endPoint: Point, layer: str, block: Block) -> Line
        
            Crea una linea di AutoCAD utilizzando due punti di Dynamo come punti iniziale e 
             finale.
        """
        pass

    def ToString(self):
        """ ToString(self: Line) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Mesh(Object):
    # no doc
    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Mesh, layer: str, block: Block) -> Mesh
        
            Crea una mesh di AutoCAD da una mesh di Dynamo.
        """
        pass

    def ToString(self):
        """ ToString(self: Mesh) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere una rappresentazione di Dynamo di questa mesh.

Get: Geometry(self: Mesh) -> Mesh

"""


    IsDynamoOwned = None
    ObjectHandle = None


class MText(Object):
    # no doc
    @staticmethod
    def Create(text, insertionPoint, columns, width, height, columnGutterWidth, horizontalAttachment, verticalAttachment, layer, block):
        """
        Create(text: str, insertionPoint: Point, columns: int, width: float, height: float, columnGutterWidth: float, horizontalAttachment: str, verticalAttachment: str, layer: str, block: Block) -> MText
        
            Crea un MText di AutoCAD da una stringa di testo.
        """
        pass

    def SetColumns(self, columns):
        """
        SetColumns(self: MText, columns: int) -> MText
        
            Imposta il numero di colonne di MText.
        """
        pass

    def SetContents(self, contents):
        """
        SetContents(self: MText, contents: str) -> MText
        
            Imposta i contenuti di MText.
        """
        pass

    def SetHeight(self, height):
        """
        SetHeight(self: MText, height: float) -> MText
        
            Imposta l'altezza di MText.
        """
        pass

    def SetWidth(self, width):
        """
        SetWidth(self: MText, width: float) -> MText
        
            Imposta la larghezza di MText.
        """
        pass

    def ToString(self):
        """ ToString(self: MText) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di eseguire query sul numero di colonne di MText.

Get: Columns(self: MText) -> int

"""

    Contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di eseguire query sui contenuti di MText.

Get: Contents(self: MText) -> str

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di eseguire query sull'altezza di MText.

Get: Height(self: MText) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di eseguire query sulla larghezza di MText.

Get: Width(self: MText) -> float

"""


    IsDynamoOwned = None
    ObjectHandle = None


class Polyline(Object):
    # no doc
    @staticmethod
    def ByPoints(points, layer, block):
        """ ByPoints(points: IList[Point], layer: str, block: Block) -> Polyline """
        pass

    def ToString(self):
        """ ToString(self: Polyline) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Polyline3D(Object):
    # no doc
    @staticmethod
    def ByPoints(points, layer, block):
        """ ByPoints(points: IList[Point], layer: str, block: Block) -> Polyline3D """
        pass

    def ToString(self):
        """ ToString(self: Polyline3D) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Property(object):
    # no doc
    def SetValue(self, value):
        """
        SetValue(self: Property, value: str) -> Property
        
            Imposta il valore di propriet?.
        """
        pass

    def ToString(self):
        """ ToString(self: Property) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome della propriet?.

Get: Name(self: Property) -> str

"""

    PropertyDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la definizione di propriet?.

Get: PropertyDefinition(self: Property) -> PropertyDefinition

"""

    PropertySet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il gruppo di propriet?.

Get: PropertySet(self: Property) -> PropertySet

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il valore della propriet?.

Get: Value(self: Property) -> object

"""



class PropertyDefinition(object):
    # no doc
    def ToString(self):
        """ ToString(self: PropertyDefinition) -> str """
        pass

    Automatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di stabilire se il valore della definizione di propriet? ? automatico.

Get: Automatic(self: PropertyDefinition) -> bool

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il tipo di dati della definizione di propriet?.

Get: DataType(self: PropertyDefinition) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione della definizione di propriet?

Get: Description(self: PropertyDefinition) -> str

"""

    InternalPD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalPD(self: PropertyDefinition) -> PropertyDefinition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome della definizione di propriet?.

Get: Name(self: PropertyDefinition) -> str

"""



class PropertySet(ObjectBase):
    # no doc
    def PropertyByName(self, name):
        """
        PropertyByName(self: PropertySet, name: str) -> Property
        
            Consente di ottenere una propriet? in base al nome.
        """
        pass

    def ToString(self):
        """ ToString(self: PropertySet) -> str """
        pass

    def UpdatePropertyValue(self, name, value):
        """
        UpdatePropertyValue(self: PropertySet, name: str, value: str) -> PropertySet
        
            Aggiorna un valore di propriet? in base al nome.
        """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AppliesTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesTo(self: PropertySet) -> object

"""

    InternalPS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalPS(self: PropertySet) -> PropertySet

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome del gruppo di propriet?.

Get: Name(self: PropertySet) -> str

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le propriet? all'interno del gruppo di propriet?.

Get: Properties(self: PropertySet) -> IList[Property]

"""

    PropertySetDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la definizione del relativo gruppo di propriet?.

Get: PropertySetDefinition(self: PropertySet) -> PropertySetDefinition

"""


    IsDynamoOwned = None
    ObjectHandle = None


class PropertySetDefinition(ObjectBase):
    # no doc
    def PropertyDefinitionByName(self, name):
        """
        PropertyDefinitionByName(self: PropertySetDefinition, name: str) -> PropertyDefinition
        
            Consente di ottenere la definizione di propriet? in base al suo nome.
        """
        pass

    def ToString(self):
        """ ToString(self: PropertySetDefinition) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AppliesToAll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToAll(self: PropertySetDefinition) -> bool

"""

    AppliesToFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToFilter(self: PropertySetDefinition) -> IList[str]

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere la descrizione della definizione del gruppo di propriet?.

Get: Description(self: PropertySetDefinition) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere il nome della definizione del gruppo di propriet?.

Get: Name(self: PropertySetDefinition) -> str

"""

    PropertyDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consente di ottenere tutte le definizioni di propriet?.

Get: PropertyDefinitions(self: PropertySetDefinition) -> IList[PropertyDefinition]

"""


    IsDynamoOwned = None
    ObjectHandle = None


class PropertySetUtils(object):
    # no doc
    @staticmethod
    def AddPropertySetToObject(obj, propertySetDefinitionName):
        """ AddPropertySetToObject(obj: DBObject, propertySetDefinitionName: str) """
        pass

    @staticmethod
    def ContainPropertiesInObject(obj, nameValues):
        """ ContainPropertiesInObject(obj: DBObject, nameValues: IList[KeyValuePair[str, str]]) -> bool """
        pass

    @staticmethod
    def CopyPropertySet(trans, source, dest):
        """
        CopyPropertySet(trans: Transaction, source: DBObject, dest: DBObject)
            Copia il gruppo di propriet? dall'oggetto di origine all'oggetto di 
             destinazione.
        
        
            trans: La transazione a GetObject
            source: L'oggetto di origine
            dest: L'oggetto di destinazione
        """
        pass

    @staticmethod
    def GetPropertySetDefinitionByPropertySet(ps):
        """ GetPropertySetDefinitionByPropertySet(ps: PropertySet) -> PropertySetDefinition """
        pass

    @staticmethod
    def GetPropertySetFromObject(obj, propertySetDefinitionName):
        """ GetPropertySetFromObject(obj: DBObject, propertySetDefinitionName: str) -> PropertySet """
        pass

    @staticmethod
    def GetPropertySetsFromObject(obj):
        """ GetPropertySetsFromObject(obj: DBObject) -> IList[PropertySet] """
        pass

    @staticmethod
    def RemovePropertySetFromObject(obj, propertySetDefinitionName):
        """ RemovePropertySetFromObject(obj: DBObject, propertySetDefinitionName: str) """
        pass

    @staticmethod
    def UpdatePropertyValuesToObject(obj, propertySetDefinitionName, nameValues):
        """ UpdatePropertyValuesToObject(obj: DBObject, propertySetDefinitionName: str, nameValues: IList[KeyValuePair[str, str]]) """
        pass

    __all__ = [
        'AddPropertySetToObject',
        'ContainPropertiesInObject',
        'CopyPropertySet',
        'GetPropertySetDefinitionByPropertySet',
        'GetPropertySetFromObject',
        'GetPropertySetsFromObject',
        'RemovePropertySetFromObject',
        'UpdatePropertyValuesToObject',
    ]


class SelectionByQuery(object):
    # no doc
    @staticmethod
    def GetAllObjectsByProperty(document, propertySetName, propertyName, propertyValue, valueOperator):
        """
        GetAllObjectsByProperty(document: Document, propertySetName: str, propertyName: str, propertyValue: object, valueOperator: str) -> IList[Object]
        
            Seleziona l'oggetto in base a nome e valore di propriet? e gruppo di propriet?.
        """
        pass

    @staticmethod
    def GetAllObjectsOfType(objectType, block):
        """
        GetAllObjectsOfType(objectType: str, block: Block) -> IList[Object]
        
            Consente di ottenere tutti gli oggetti da un tipo di oggetto specificato.
        """
        pass

    @staticmethod
    def GetAllObjectsOfTypeByRXClass(cls, block):
        """
        GetAllObjectsOfTypeByRXClass(cls: RXClass, block: Block) -> IList[Object]
        
            Consente di ottenere tutti gli oggetti da una classe di runtime specificata.
        """
        pass

    @staticmethod
    def GetAllObjectsOnLayer(layer, block):
        """
        GetAllObjectsOnLayer(layer: str, block: Block) -> IList[Object]
        
            Consente di ottenere tutti gli oggetti su un layer specificato.
        """
        pass

    @staticmethod
    def GetObjectByObjectHandle(handle):
        """
        GetObjectByObjectHandle(handle: str) -> Object
        
            Consente di ottenere l'oggetto dal suo gestore.
        """
        pass

    __all__ = [
        'GetAllObjectsByProperty',
        'GetAllObjectsOfType',
        'GetAllObjectsOfTypeByRXClass',
        'GetAllObjectsOnLayer',
        'GetObjectByObjectHandle',
    ]


class Solid(Object):
    # no doc
    @staticmethod
    def ByGeometry(geometry, layer, block):
        """
        ByGeometry(geometry: Solid, layer: str, block: Block) -> Solid
        
            Crea un solido di AutoCAD da un solido di Dynamo.
        """
        pass

    def SliceByPlanes(self, planes):
        """ SliceByPlanes(self: Solid, planes: IList[Plane]) -> IList[Solid] """
        pass

    def ToString(self):
        """ ToString(self: Solid) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


class Text(Object):
    # no doc
    @staticmethod
    def Create(text, insertionPoint, height, rotation, horizontalMode, verticalMode, layer, block):
        """
        Create(text: str, insertionPoint: Point, height: float, rotation: Vector, horizontalMode: str, verticalMode: str, layer: str, block: Block) -> Text
        
            Crea un testo di AutoCAD da una stringa di testo.
        """
        pass

    def ToString(self):
        """ ToString(self: Text) -> str """
        pass

    AcadObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AcObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IsDynamoOwned = None
    ObjectHandle = None


