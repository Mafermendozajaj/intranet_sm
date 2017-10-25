# coding=utf-8
import time
import datetime

from django.core.management.base import BaseCommand

from intranet.asistencia_app.models import Marca, Dispositivo, EmpleadoClienteDispositivo
from intranet.utils.utils import EnviarCorreo


class Command(BaseCommand):

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument('--verificar',
                            action='store_true',
                            dest='verificar',
                            default=False,
                            help='Verificar un archivo de marcas')

        parser.add_argument('--importar',
                            action='store_true',
                            dest='importar',
                            default=False,
                            help='Importa un archio de marcas')

        parser.add_argument('--importar_aso',
                            action='store_true',
                            dest='importar_aso',
                            default=False,
                            help='Importa asociacion dispositivo users')

        parser.add_argument('--enviar_correo',
                            action='store_true',
                            dest='enviar_correo',
                            default=False,
                            help='Prueba para enviar correo')

        parser.add_argument('dispositivo')
        parser.add_argument('archivo')

    def handle(self, *args, **options):
        # ...
        if options['verificar']:
            """
            Comando para verificar archivo de marcas
            """

            dispositivo = options['dispositivo']
            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            for fileLine in fileList:
                [id_user, nombre, fecha, hora] = fileLine.split("\t")
                hora = hora.strip(' \t\n\r')
                # print dispositivo, id_user, fecha, hora

                # Verifica si el dispositivo esta registrado

                try:
                    d = Dispositivo.objects.get(id=dispositivo)
                except:
                    print( "El dispositivo: " + dispositivo + " no esta registrado")
                    # enviar un correo de advertencia
                    ec = EnviarCorreo(
                        'appscuy@gmail.com', 'soporte@smartec.com.uy', 'dispositivo ' + dispositivo + ' no está registrado')
                    ec.enviar()
                    break

        if options['importar']:
            """
            Comando para importar archivo de dispositivos
            """
            # Tomar el tiempo de incio
            start_time = time.clock()

            dispositivo = options['dispositivo']
            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            idx = 0
            for fileLine in fileList:
                idx += 1
                try:
                    [id_user, nombre, fecha, tipo_registro, accion] = fileLine.split('\t')
                except:
                    print("Ocurrio un error al intentar leer la linea "+str(idx)+" del archivo" + archivo)

                accion = accion.strip(' \t\n\r')

                title = ''

                if accion == '0':
                    title = 'Entrada'
                elif accion == '1':
                    title = 'Salida'

                print(id_user, fecha)

                fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')

                try:
                    marcas = Marca(dispositivo_id=dispositivo, id_user=id_user,
                                   start=fecha, title=title
                                   )
                    marcas.save()

                except:
                    print("Ocurrio un error al intentar grabar el ",  dispositivo, id_user, fecha,   " no esta registrado")
                    #break

            totalTime = time.clock() - start_time, "seconds"

            print(totalTime)

        if options['enviar_correo']:
            """
            Comando enviar correo
            """
            ec = EnviarCorreo(
                'hr@hernanramirez.info', 'hr@hernanramirez', 'Este es el mensaje')
            ec.enviar()

        if options['importar_aso']:
            """
            Comando para importar archivo de dispositivos y asociaciones con user
            """
            # Tomar el tiempo de incio
            start_time = time.clock()

            dispositivo = options['dispositivo']
            archivo = options['archivo']
            fileHandle = open(archivo)
            fileList = fileHandle.readlines()

            idx = 0
            for fileLine in fileList:
                idx += 1
                try:
                    [dispositivo, id_user, user_id ] = fileLine.split(',')
                except:
                    print("Ocurrio un error al intentar leer la linea " + str(idx) + " del archivo" + archivo)

                user_id = user_id.strip(' \t\n\r')



                #try:
                empAso = EmpleadoClienteDispositivo(dispositivo_id=dispositivo, id_user=id_user,
                               empleado_id=user_id
                               )
                empAso.save()
                print(id_user, user_id)

                #except:
                #    print("Ocurrio un error al intentar grabar el " + dispositivo + " no esta registrado")
                #    # enviar un correo de advertencia
                #    break

            totalTime = time.clock() - start_time, "seconds"

            print(totalTime)

