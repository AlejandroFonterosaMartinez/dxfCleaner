import os
import ezdxf

def eliminar_info(doc, nombres_capas):
    msp = doc.modelspace()

    for nombre_capa in nombres_capas:
        # Eliminar entidades en capa
        entidades_a_eliminar = [entidad for entidad in msp.query('*[layer=="{}"]'.format(nombre_capa))]
        for entidad in entidades_a_eliminar:
            msp.delete_entity(entidad)

    ole_entities = [entidad for entidad in msp.query('OLE2FRAME OLE')]
    for entidad in ole_entities:
        msp.delete_entity(entidad)

if __name__ == "__main__":
    carpeta_archivos_dxf = "dxfs"
    nombres_capas_a_eliminar = ["NOTAS", "FORMAT"]

    try:
        for filename in os.listdir(carpeta_archivos_dxf):
            if filename.endswith(".dxf"):
                ruta_archivo_dxf = os.path.join(carpeta_archivos_dxf, filename)

                doc = ezdxf.readfile(ruta_archivo_dxf)
                eliminar_info(doc, nombres_capas_a_eliminar)
                doc.saveas(ruta_archivo_dxf)

        print("Proceso completado.")
    except Exception as e:
        print(f"Error: {e}")
