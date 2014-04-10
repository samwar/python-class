#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'samu6978'

import pyrax
import exceptions
from os.path import expanduser

default_cred_path = expanduser('~') + "/.pyrax_credentials"
default_region = 'ORD'
default_ssh_key_name = 'Macbook SSH Key'

regions = ['DFW', 'IAD', 'ORD']

def choose_region(region):
    return pyrax.connect_to_cloudservers(region=region)


def create_server(cs, args):
    from uuid import uuid4
    from pyrax.utils import wait_for_build

    server_image = find_image(cs, args)
    server_flavor = find_flavor(cs, args)
    for i in range(args.number_servers):
        speed = get_speed(args.performance)
        print "Starting {0} {1} {2} MB {3} server build number {4} in {5}...".format(args.os, args.version, args.ram,
                                                                                     speed, i + 1, args.region)
        server = cs.servers.create(args.prefix + '_' + str(uuid4()), server_image.id, server_flavor.id,
                                   key_name=args.ssh_key_name)
        finished_server = wait_for_build(server, verbose=True)
        admin_pass = server.adminPass
        print_server_info(finished_server, admin_pass)


def find_image(cs, args):
    server_image = [img for img in cs.images.list()
                    if args.os + ' ' + args.version in img.name]
    if server_image:
        return server_image[0]
    else:
        raise Exception('No image with the name "' + args.os + ' ' + args.version + '" found.')


def find_flavor(cs, args):
    speed = get_speed(args.performance)
    server_flavor = [flavor for flavor in cs.flavors.list()
                     if flavor.ram == args.ram and speed in flavor.id]
    if server_flavor:
        return server_flavor[0]
    else:
        raise Exception('No flavor found with the specs "' + str(args.ram) + 'MB ' + speed + '" found.')


def get_speed(performance_flag):
    return 'performance' if args.performance else ''


def print_server_info(server, admin_pass):
    print "Name: ", server.name
    print "Id: ", server.id
    print "Status: ", server.status
    print "Network Info: ", server.networks
    print "SSH Key Name:", server.key_name
    print "Admin Password: ", admin_pass
    print "\n"


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Pyrax Server Creation on the Rackspace Cloud')
    parser.add_argument('-c', '--cred_path', type=str, dest='cred_path', default=default_cred_path,
                        help='The path to your pyrax credentials. (default ' + default_cred_path + ')')
    parser.add_argument('-rg', '--region', type=str, dest='region', default=default_region, choices=regions,
                        help='The region where you want to create your servers. (default ' + default_region + ')')
    parser.add_argument('-lf', '--list_flavors', dest='list_flavors', action='store_true',
                        help='List the pyrax flavors available.')
    parser.add_argument('-li', '--list_images', dest='list_images', action='store_true',
                        help='List the pyrax images available.')
    parser.add_argument('-ls', '--list_servers', dest='list_servers', action='store_true',
                        help='List the servers created in your specified US region.')
    parser.add_argument('-lsa', '--list_all_servers', dest='list_all_servers', action='store_true',
                        help='List the servers created in all US regions.')
    parser.add_argument('-p', '--prefix', type=str, dest='prefix', default='pyrax_server',
                        help='The prefix for your server name. (default "pyrax_server" )')
    parser.add_argument('-n', '--number_servers', type=int, dest='number_servers', default=1,
                        help='The number of servers you want to spin up. (default ' + str(1) + ')')
    parser.add_argument('-o', '--os', type=str, dest='os', help='The OS you want to use.')
    parser.add_argument('-v', '--version', type=str, dest='version',
                        help='The version of the OS you want to use.')
    parser.add_argument('-r', '--ram', type=int, dest='ram',
                        help='The amount of RAM you want in your server in MB.')
    parser.add_argument('-m', '--performance', dest='performance', action='store_true',
                        help='Use this option if you want the performance flavor.')
    parser.add_argument('-ssh', '--ssh_key_name', dest='ssh_key_name', type=str, default=default_ssh_key_name,
                        help='The name of the SSH key you want to use.')

    args = parser.parse_args()

    if args.cred_path and args.list_servers:
        cs_region = choose_region(args.region)
        print "\nAvailable Servers in {0}:".format(args.region)
        print cs_region.servers.list()
    elif args.cred_path and args.list_all_servers:
        print "\nAvailable Servers in all US regions:"
        all_servers = []
        for val in regions:
            all_servers += choose_region(val).servers.list()
        print all_servers
    elif args.cred_path:
        cs = choose_region(args.region)
        print "Authenticated"

        if args.list_flavors:
            print "\nAvailable Flavors:"
            print cs.list_flavors()

        if args.list_images:
            print "\nAvailable Images:"
            print cs.list_images()

        if args.os and args.version and args.ram:
            create_server(cs, args)
    else:
        print "No credentials found."










