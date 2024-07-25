import asyncio
from asyncua import Server, ua
from asyncua.ua.uaerrors import BadNodeIdExists
import xml.etree.ElementTree as ET

async def main():
    # Parse the XML content
    xml_file = "export_ns2_withvalues.xml"
    root = ET.parse(xml_file)

    # Define the namespace
    ns = {'default': 'http://opcfoundation.org/UA/2011/03/UANodeSet.xsd'}

    # Extract the URI from the NamespaceUris element
    uri = root.find('default:NamespaceUris/default:Uri', ns).text

    # Create the server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("Server name")

    # Setup namespace with the expected URI from xml
    idx = await server.register_namespace(uri)
    
    # Print the namespace index to verify
    print(f"Namespace index for '{uri}' is {idx}")

    # Import XML configuration
    await server.import_xml(xml_file,strict_mode=False)

    # Starting the server
    async with server:
        print("Server is running at opc.tcp://0.0.0.0:4840/freeopcua/server/")
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
