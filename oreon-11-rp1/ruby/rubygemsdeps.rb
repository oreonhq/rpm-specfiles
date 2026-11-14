#!/usr/bin/ruby
require 'rubygems'

mode = ARGV.shift

def rpm_requirements(name, requirement)
  out = []
  requirement.requirements.each do |op, ver|
    case op
    when '>='
      out << (ver.to_s == '0' ? "rubygem(#{name})" : "rubygem(#{name}) >= #{ver}")
    when '>', '<', '<='
      out << "rubygem(#{name}) #{op} #{ver}"
    when '='
      out << "rubygem(#{name}) = #{ver}"
    when '~>'
      out << "rubygem(#{name}) >= #{ver}"
      out << "rubygem(#{name}) < #{ver.bump}"
    when '!='
      out << "(rubygem(#{name}) < #{ver} or rubygem(#{name}) > #{ver})"
    end
  end
  out
end

STDIN.each_line do |line|
  path = line.chomp
  next if path.empty?
  spec = Gem::Specification.load(path)
  next unless spec
  case mode
  when 'provides'
    puts "rubygem(#{spec.name}) = #{spec.version}"
  when 'requires'
    spec.runtime_dependencies.each do |dep|
      rpm_requirements(dep.name, dep.requirement).each {|r| puts r }
    end
  end
end
