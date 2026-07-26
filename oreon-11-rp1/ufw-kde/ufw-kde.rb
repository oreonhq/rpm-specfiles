#!/usr/bin/env ruby

NAME      = "ufw-kde"
COMPONENT = "playground"
SECTION   = "sysadmin"

$options = {:barrier=>75}
$srcvcs   = "git"
$: << File.dirname( __FILE__)

require 'lib/starter'
