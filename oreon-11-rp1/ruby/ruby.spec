# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a8057adb39f51ad6dc3106237504c93dd792bb515837b4fe7817ae21ed7e51f4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global major_minor_version 4.0
%global ruby_abi 4.0.0
%global ruby_arch %{_arch}-%{_target_os}
%global rubygems_version 4.0.20
%global bundler_version 4.0.20

%global ruby_libdir %{_libdir}/ruby/%{ruby_abi}
%global ruby_libarchdir %{ruby_libdir}/%{ruby_arch}
%global ruby_vendordir %{_libdir}/ruby/vendor_ruby
%global ruby_vendorlibdir %{ruby_vendordir}/%{ruby_abi}
%global ruby_vendorarchdir %{ruby_vendorlibdir}/%{ruby_arch}
%global ruby_sitedir %{_prefix}/local/%{_lib}/ruby/site_ruby
%global ruby_default_gemdir %{_libdir}/ruby/gems/%{ruby_abi}
%global gem_dir %{_datadir}/gems
%global gem_extdir_mri %{_libdir}/gems/ruby

Name:           ruby
Version:        4.0.9
Release:        1%{?dist}
Summary:        Ruby programming language interpreter
License:        (Ruby OR BSD-2-Clause) AND BSD-2-Clause AND BSD-3-Clause AND MIT AND Unicode-3.0 AND CC0-1.0 AND Zlib AND ISC
URL:            https://www.ruby-lang.org/
Source0:        https://cache.ruby-lang.org/pub/ruby/%{major_minor_version}/ruby-%{version}.tar.xz
Source1:        operating_system.rb
Source2:        macros.ruby
Source3:        macros.rubygems
Source4:        rubygems.attr
Source5:        rubygemsdeps.rb
Source6:        rubygems.prov
Source7:        rubygems.req

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  oreon-rpm-macros
BuildRequires:  gmp-devel
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libyaml-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRequires:  hostname
BuildRequires:  procps-ng
BuildRequires:  tzdata

Requires:       ruby-libs%{?_isa} = %{version}-%{release}
Requires:       rubygems = %{rubygems_version}-%{release}
Requires:       ruby-default-gems = %{version}-%{release}

%description
Ruby is the interpreted scripting language for quick and easy object-oriented
programming. It has many features to process text files and to do system
management tasks, as in Perl. It is simple, straightforward, and extensible.

%package        libs
Summary:        Libraries necessary to run Ruby programs
Provides:       ruby(release) = %{ruby_abi}
Provides:       bundled(onigmo)

%description    libs
This package includes the libruby shared library, the Ruby standard library
and the default load path directories needed to run Ruby programs.

%package        devel
Summary:        A Ruby development environment
Requires:       ruby-libs%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for building extension libraries for Ruby.

%package        doc
Summary:        Ruby API documentation
BuildArch:      noarch

%description    doc
The ri data and the HTML API documentation for the Ruby core classes and
the standard library.

%package -n     rubygems
Summary:        The Ruby standard for packaging Ruby libraries
Version:        %{rubygems_version}
License:        (Ruby OR BSD-2-Clause) AND MIT
Requires:       ruby(release)
Provides:       ruby(rubygems) = %{rubygems_version}
Provides:       rubygem(rubygems) = %{rubygems_version}
Provides:       bundled(rubygems-molinillo)
Provides:       bundled(rubygems-net-http)
Provides:       bundled(rubygems-optparse)
Provides:       bundled(rubygems-net-protocol)
Provides:       bundled(rubygems-resolv)
Provides:       bundled(rubygems-securerandom)
Provides:       bundled(rubygems-timeout)
Provides:       bundled(rubygems-tsort)
Provides:       bundled(rubygems-uri)

%description -n rubygems
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%package -n     rubygems-devel
Summary:        Macros and development tools for packaging RubyGems
Version:        %{rubygems_version}
License:        (Ruby OR BSD-2-Clause) AND MIT
Requires:       ruby(rubygems) >= %{rubygems_version}
Requires:       ruby >= %{version}
BuildArch:      noarch

%description -n rubygems-devel
Macros and development tools for packaging RubyGems. Includes the dependency
generators that create rubygem(name) provides and requires from gemspecs.

%package        default-gems
Summary:        Default gems that ship with Ruby
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(date) = 3.5.1
Provides:       rubygem(delegate) = 0.6.1
Provides:       rubygem(did_you_mean) = 2.0.0
Provides:       rubygem(digest) = 3.2.1
Provides:       rubygem(english) = 0.8.1
Provides:       rubygem(erb) = 6.0.7
Provides:       rubygem(error_highlight) = 0.7.2
Provides:       rubygem(etc) = 1.4.6
Provides:       rubygem(fcntl) = 1.3.0
Provides:       rubygem(fileutils) = 1.8.0
Provides:       rubygem(find) = 0.2.0
Provides:       rubygem(forwardable) = 1.4.0
Provides:       rubygem(io-console) = 0.8.2
Provides:       rubygem(io-nonblock) = 0.3.2
Provides:       rubygem(io-wait) = 0.4.0
Provides:       rubygem(ipaddr) = 1.2.8
Provides:       rubygem(json) = 2.18.0
Provides:       rubygem(net-http) = 0.9.1
Provides:       rubygem(net-protocol) = 0.2.2
Provides:       rubygem(open-uri) = 0.5.0
Provides:       rubygem(open3) = 0.2.1
Provides:       rubygem(openssl) = 4.0.2
Provides:       rubygem(optparse) = 0.8.1
Provides:       rubygem(pp) = 0.6.3
Provides:       rubygem(prettyprint) = 0.2.0
Provides:       rubygem(prism) = 1.8.2
Provides:       rubygem(psych) = 5.3.1
Provides:       rubygem(resolv) = 0.7.2
Provides:       rubygem(ruby2_keywords) = 0.0.5
Provides:       rubygem(securerandom) = 0.4.1
Provides:       rubygem(shellwords) = 0.2.2
Provides:       rubygem(singleton) = 0.3.0
Provides:       rubygem(stringio) = 3.2.0
Provides:       rubygem(strscan) = 3.1.6
Provides:       rubygem(syntax_suggest) = 2.0.3
Provides:       rubygem(tempfile) = 0.3.1
Provides:       rubygem(time) = 0.4.2
Provides:       rubygem(timeout) = 0.6.0
Provides:       rubygem(tmpdir) = 0.3.1
Provides:       rubygem(tsort) = 0.2.0
Provides:       rubygem(un) = 0.3.0
Provides:       rubygem(uri) = 1.1.1
Provides:       rubygem(weakref) = 0.1.4
Provides:       rubygem(yaml) = 0.4.0
Provides:       rubygem(zlib) = 3.2.3

%description    default-gems
The gems that are part of the Ruby standard library and are installed by
default. They are loaded from the standard library paths and only their
specifications live in the gem directory.

%package -n     rubygem-bundler
Summary:        The best way to manage a Ruby application's gems
Version:        %{bundler_version}
License:        MIT
URL:            https://bundler.io/
Requires:       ruby(release)
Requires:       ruby(rubygems) >= %{rubygems_version}
Provides:       rubygem(bundler) = %{bundler_version}
Provides:       bundler = %{bundler_version}
Provides:       bundled(bundler-connection_pool)
Provides:       bundled(bundler-fileutils)
Provides:       bundled(bundler-net-http-persistent)
Provides:       bundled(bundler-pub_grub)
Provides:       bundled(bundler-securerandom)
Provides:       bundled(bundler-thor)
Provides:       bundled(bundler-uri)

%description -n rubygem-bundler
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.

%package -n rubygem-abbrev
Summary:        Calculates a set of unique abbreviations for a given set of strings
Version:        0.1.2
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/abbrev
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(abbrev) = 0.1.2

%description -n rubygem-abbrev
Calculates a set of unique abbreviations for a given set of strings.

%package -n rubygem-base64
Summary:        Support for encoding and decoding binary data using a Base64 representation
Version:        0.3.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/base64
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(base64) = 0.3.0

%description -n rubygem-base64
Support for encoding and decoding binary data using a Base64 representation.

%package -n rubygem-benchmark
Summary:        a performance benchmarking library
Version:        0.5.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/benchmark
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(benchmark) = 0.5.0

%description -n rubygem-benchmark
a performance benchmarking library.

%package -n rubygem-bigdecimal
Summary:        Arbitrary-precision decimal floating-point number library
Version:        4.0.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/bigdecimal
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(bigdecimal) = 4.0.1

%description -n rubygem-bigdecimal
This library provides arbitrary-precision decimal floating-point number
class.

%package -n rubygem-csv
Summary:        CSV Reading and Writing
Version:        3.3.5
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/csv
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(csv) = 3.3.5

%description -n rubygem-csv
The CSV library provides a complete interface to CSV files and data. It
offers tools to enable you to read and write to and from Strings or IO
objects, as needed.

%package -n rubygem-debug
Summary:        Debugging functionality for Ruby
Version:        1.11.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/debug
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(irb) >= 1.10
Requires:       rubygem(irb) < 2
Requires:       rubygem(reline) >= 0.3.8
Provides:       rubygem(debug) = 1.11.1

%description -n rubygem-debug
Debugging functionality for Ruby. This is completely rewritten debug.rb
which was contained by the ancient Ruby versions.

%package -n rubygem-drb
Summary:        Distributed object system for Ruby
Version:        2.2.3
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/drb
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(drb) = 2.2.3

%description -n rubygem-drb
Distributed object system for Ruby.

%package -n rubygem-fiddle
Summary:        A libffi wrapper for Ruby
Version:        1.1.8
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/fiddle
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(fiddle) = 1.1.8

%description -n rubygem-fiddle
A libffi wrapper for Ruby.

%package -n rubygem-getoptlong
Summary:        GetoptLong for Ruby
Version:        0.2.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/getoptlong
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(getoptlong) = 0.2.1

%description -n rubygem-getoptlong
GetoptLong for Ruby.

%package -n rubygem-irb
Summary:        Interactive Ruby command-line tool for REPL (Read Eval Print Loop)
Version:        1.16.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/irb
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(reline) >= 0.4.2
Requires:       rubygem(rdoc) >= 4.0.0
Requires:       rubygem(pp) >= 0.6.0
Provides:       rubygem(irb) = 1.16.0

%description -n rubygem-irb
Interactive Ruby command-line tool for REPL (Read Eval Print Loop).

%package -n rubygem-logger
Summary:        Provides a simple logging utility for outputting messages
Version:        1.7.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/logger
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(logger) = 1.7.0

%description -n rubygem-logger
Provides a simple logging utility for outputting messages.

%package -n rubygem-matrix
Summary:        An implementation of Matrix and Vector classes
Version:        0.4.3
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/matrix
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(matrix) = 0.4.3

%description -n rubygem-matrix
An implementation of Matrix and Vector classes.

%package -n rubygem-minitest
Summary:        minitest provides a complete suite of testing facilities supporting TDD, BDD, and benchmarking
Version:        6.0.0
License:        MIT
URL:            https://minite.st/
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(prism) >= 1.5
Requires:       rubygem(prism) < 2
Provides:       rubygem(minitest) = 6.0.0

%description -n rubygem-minitest
minitest provides a complete suite of testing facilities supporting TDD,
BDD, and benchmarking. "I had a class with Jim Weirich on testing last week
and we were allowed to choose our testing frameworks. Kirk Haines and I were
paired up and we cracked open the code for a few test frameworks... I MUST
say that minitest is *very* readable / understandable compared to the 'other
two' options we looked at. Nicely done and thank you for helping us keep our
mental sanity." -- Wayne E. Seguin minitest/test is a small and incredibly
fast unit testing framework. It provides a rich set of assertions to make
your tests clean and readable. minitest/spec is a functionally complete spec
engine. It hooks onto minitest/test and seamlessly bridges test assertions
over to spec expectations. minitest/benchmark is an awesome way to assert
the performance of your algorithms in a repeatable manner. Now you can
assert that your newb co-worker doesn't replace your linear algorithm with
an exponential one! minitest/pride shows pride in testing and adds coloring
to your test output. I guess it is an example of how to write IO pipes too.
:P minitest/test is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working test
suite. For example, there is no magic involved for test-case discovery.
"Again, I can't praise enough the idea of a testing/specing framework that I
can actually read in full in one sitting!" -- Piotr Szotkowski Comparing to
rspec: rspec is a testing DSL. minitest is ruby. -- Adam Hawkins, "Bow
Before MiniTest" minitest doesn't reinvent anything that ruby already
provides, like: classes, modules, inheritance, methods. This means you only
have to learn ruby to use minitest and all of your regular OO practices like
extract-method refactorings still apply.

%package -n rubygem-mutex_m
Summary:        Mixin to extend objects to be handled like a Mutex
Version:        0.3.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/mutex_m
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(mutex_m) = 0.3.0

%description -n rubygem-mutex_m
Mixin to extend objects to be handled like a Mutex.

%package -n rubygem-net-ftp
Summary:        Support for the File Transfer Protocol
Version:        0.3.9
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/net-ftp
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(net-protocol)
Requires:       rubygem(time)
Provides:       rubygem(net-ftp) = 0.3.9

%description -n rubygem-net-ftp
Support for the File Transfer Protocol.

%package -n rubygem-net-imap
Summary:        Ruby client api for Internet Message Access Protocol
Version:        0.6.4.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/net-imap
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(net-protocol)
Requires:       rubygem(date)
Provides:       rubygem(net-imap) = 0.6.4.1

%description -n rubygem-net-imap
Ruby client api for Internet Message Access Protocol.

%package -n rubygem-net-pop
Summary:        Ruby client library for POP3
Version:        0.1.2
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/net-pop
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(net-protocol)
Provides:       rubygem(net-pop) = 0.1.2

%description -n rubygem-net-pop
Ruby client library for POP3.

%package -n rubygem-net-smtp
Summary:        Simple Mail Transfer Protocol client library for Ruby
Version:        0.5.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/net-smtp
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(net-protocol)
Provides:       rubygem(net-smtp) = 0.5.1

%description -n rubygem-net-smtp
Simple Mail Transfer Protocol client library for Ruby.

%package -n rubygem-nkf
Summary:        Ruby extension for Network Kanji Filter
Version:        0.2.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/nkf
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(nkf) = 0.2.0

%description -n rubygem-nkf
Ruby extension for Network Kanji Filter.

%package -n rubygem-observer
Summary:        Implementation of the Observer object-oriented design pattern
Version:        0.1.2
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/observer
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(observer) = 0.1.2

%description -n rubygem-observer
Implementation of the Observer object-oriented design pattern.

%package -n rubygem-ostruct
Summary:        Class to build custom data structures, similar to a Hash
Version:        0.6.3
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/ostruct
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(ostruct) = 0.6.3

%description -n rubygem-ostruct
Class to build custom data structures, similar to a Hash.

%package -n rubygem-power_assert
Summary:        Power Assert for Ruby
Version:        3.0.1
License:        BSD-2-Clause OR Ruby
URL:            https://github.com/ruby/power_assert
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(power_assert) = 3.0.1

%description -n rubygem-power_assert
Power Assert shows each value of variables and method calls in the
expression. It is useful for testing, providing which value wasn't correct
when the condition is not satisfied.

%package -n rubygem-prime
Summary:        Prime numbers and factorization library
Version:        0.1.4
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/prime
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(singleton)
Requires:       rubygem(forwardable)
Provides:       rubygem(prime) = 0.1.4

%description -n rubygem-prime
Prime numbers and factorization library.

%package -n rubygem-pstore
Summary:        Transactional File Storage for Ruby Objects
Version:        0.2.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/pstore
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(pstore) = 0.2.1

%description -n rubygem-pstore
Transactional File Storage for Ruby Objects.

%package -n rubygem-racc
Summary:        Racc is an LALR(1) parser generator
Version:        1.8.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/racc
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(racc) = 1.8.1

%description -n rubygem-racc
Racc is an LALR(1) parser generator. It is written in Ruby itself, and
generates Ruby program. NOTE: Ruby 1.8.x comes with Racc runtime module. You
can run your parsers generated by racc 1.4.x out of the box.

%package -n rubygem-rake
Summary:        Rake is a Make-like program implemented in Ruby
Version:        13.3.1
License:        MIT
URL:            https://github.com/ruby/rake
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(rake) = 13.3.1

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax. Rake has the following features: *
Rakefiles (rake's version of Makefiles) are completely defined in standard
Ruby syntax. No XML files to edit. No quirky Makefile syntax to worry about
(is that a tab or a space?) * Users can specify tasks with prerequisites. *
Rake supports rule patterns to synthesize implicit tasks. * Flexible
FileLists that act like arrays but know about manipulating file names and
paths. * Supports parallel execution of tasks.

%package -n rubygem-rbs
Summary:        Type signature for Ruby
Version:        3.10.0
License:        BSD-2-Clause OR Ruby
URL:            https://github.com/ruby/rbs
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(logger)
Provides:       rubygem(rbs) = 3.10.0

%description -n rubygem-rbs
RBS is the language for type signatures for Ruby and standard library
definitions.

%package -n rubygem-rdoc
Summary:        RDoc produces HTML and command-line documentation for Ruby projects
Version:        7.0.4
License:        Ruby AND BSD-2-Clause AND MIT AND (Ruby OR BSD-2-Clause)
URL:            https://ruby.github.io/rdoc
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(psych) >= 4.0.0
Requires:       rubygem(erb)
Requires:       rubygem(tsort)
Provides:       rubygem(rdoc) = 7.0.4

%description -n rubygem-rdoc
RDoc produces HTML and command-line documentation for Ruby projects. RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying
documentation from the command-line.

%package -n rubygem-readline
Summary:        Loader for "readline"
Version:        0.0.4
License:        Ruby
URL:            https://github.com/ruby/readline
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(reline)
Provides:       rubygem(readline) = 0.0.4

%description -n rubygem-readline
This is just a loader for "readline". If Ruby has the "readline-ext" gem
that is a native extension, this gem will load it. If Ruby does not have the
"readline-ext" gem this gem will load "reline", a library that is compatible
with the "readline-ext" gem and implemented in pure Ruby.

%package -n rubygem-reline
Summary:        Alternative GNU Readline or Editline implementation by pure Ruby
Version:        0.6.3
License:        Ruby
URL:            https://github.com/ruby/reline
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(io-console) >= 0.5
Requires:       rubygem(io-console) < 1
Provides:       rubygem(reline) = 0.6.3

%description -n rubygem-reline
Alternative GNU Readline or Editline implementation by pure Ruby.

%package -n rubygem-repl_type_completor
Summary:        Type based completion for REPL
Version:        0.1.12
License:        MIT
URL:            https://github.com/ruby/repl_type_completor
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(prism) >= 1.0
Requires:       rubygem(prism) < 2
Requires:       rubygem(rbs) >= 2.7.0
Requires:       rubygem(rbs) < 4.0.0
Provides:       rubygem(repl_type_completor) = 0.1.12

%description -n rubygem-repl_type_completor
Type based completion for REPL.

%package -n rubygem-resolv-replace
Summary:        Replace Socket DNS with Resolv
Version:        0.1.1
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/resolv-replace
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(resolv)
Provides:       rubygem(resolv-replace) = 0.1.1

%description -n rubygem-resolv-replace
Replace Socket DNS with Resolv.

%package -n rubygem-rexml
Summary:        An XML toolkit for Ruby
Version:        3.4.4
License:        BSD-2-Clause
URL:            https://github.com/ruby/rexml
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(rexml) = 3.4.4

%description -n rubygem-rexml
An XML toolkit for Ruby.

%package -n rubygem-rinda
Summary:        The Linda distributed computing paradigm in Ruby
Version:        0.2.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/rinda
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(drb)
Requires:       rubygem(ipaddr)
Requires:       rubygem(forwardable)
Provides:       rubygem(rinda) = 0.2.0

%description -n rubygem-rinda
The Linda distributed computing paradigm in Ruby.

%package -n rubygem-rss
Summary:        Family of libraries that support various formats of XML "feeds"
Version:        0.3.2
License:        BSD-2-Clause
URL:            https://github.com/ruby/rss
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(rexml)
Provides:       rubygem(rss) = 0.3.2

%description -n rubygem-rss
Family of libraries that support various formats of XML "feeds".

%package -n rubygem-syslog
Summary:        Ruby interface for the POSIX system logging facility
Version:        0.3.0
License:        Ruby OR BSD-2-Clause
URL:            https://github.com/ruby/syslog
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(logger)
Provides:       rubygem(syslog) = 0.3.0

%description -n rubygem-syslog
Ruby interface for the POSIX system logging facility.

%package -n rubygem-test-unit
Summary:        An xUnit family unit testing framework for Ruby
Version:        3.7.5
License:        (Ruby OR BSD-2-Clause) AND PSF-2.0
URL:            https://test-unit.github.io/
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(power_assert)
Provides:       rubygem(test-unit) = 3.7.5

%description -n rubygem-test-unit
test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It
allows writing tests, checking results and automated testing in Ruby.

%package -n rubygem-typeprof
Summary:        TypeProf is a type analysis tool for Ruby code based on abstract interpretation
Version:        0.31.1
License:        MIT
URL:            https://github.com/ruby/typeprof
BuildArch:      noarch
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(prism) >= 1.4.0
Requires:       rubygem(rbs) >= 3.6.0
Provides:       rubygem(typeprof) = 0.31.1

%description -n rubygem-typeprof
TypeProf performs a type analysis of non-annotated Ruby code. It abstractly
executes input Ruby code in a level of types instead of values, gathers what
types are passed to and returned by methods, and prints the analysis result
in RBS format, a standard type description format for Ruby 3.0.

%prep
%oreon_sha256
%autosetup -n ruby-%{version}

%build
%configure \
        --with-baseruby=no \
        --with-ruby-pc=ruby.pc \
        --with-sitedir=%{ruby_sitedir} \
        --enable-shared \
        --enable-mkmf-verbose \
        --disable-rpath \
        --disable-dtrace
%make_build
%make_build html

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/ruby
cp -a .ext/html %{buildroot}%{_docdir}/ruby/html

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}
mv %{buildroot}%{ruby_default_gemdir}/extensions/*/*/* %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{ruby_default_gemdir}/extensions
cp -a %{buildroot}%{ruby_default_gemdir}/. %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{_libdir}/ruby/gems
mkdir -p %{buildroot}%{gem_dir}/{build_info,cache,doc,gems,plugins,specifications/default}

rm -rf %{buildroot}%{_prefix}/local

install -Dpm0644 %{SOURCE1} %{buildroot}%{ruby_vendorlibdir}/rubygems/defaults/operating_system.rb
mkdir -p %{buildroot}%{ruby_vendorarchdir}

install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.ruby
sed -i \
        -e 's|@@RUBY_VERSION@@|%{version}|' \
        -e 's|@@RUBY_ABI@@|%{ruby_abi}|' \
        -e 's|@@RUBY_ARCH@@|%{ruby_arch}|' \
        %{buildroot}%{_rpmmacrodir}/macros.ruby
install -Dpm0644 %{SOURCE3} %{buildroot}%{_rpmmacrodir}/macros.rubygems
install -Dpm0644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/fileattrs/rubygems.attr
install -Dpm0755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/rubygemsdeps.rb
install -Dpm0755 %{SOURCE6} %{buildroot}%{_rpmconfigdir}/rubygems.prov
install -Dpm0755 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/rubygems.req

: > %{_builddir}/%{name}-default-gems.files
for spec in %{buildroot}%{gem_dir}/specifications/default/*.gemspec; do
  full=$(basename "$spec" .gemspec)
  case "$full" in
    bundler-*) continue ;;
  esac
  echo "%{gem_dir}/specifications/default/$full.gemspec" >> %{_builddir}/%{name}-default-gems.files
  if [ -d "%{buildroot}%{gem_dir}/gems/$full" ]; then
    echo "%{gem_dir}/gems/$full" >> %{_builddir}/%{name}-default-gems.files
  fi
done

%check
export LANG=C.UTF-8
make check

%ldconfig_scriptlets libs

%files
%license BSDL COPYING GPL LEGAL
%doc README.md NEWS.md
%{_bindir}/ruby
%{_bindir}/erb
%{_mandir}/man1/ruby.1*
%{_mandir}/man1/erb.1*

%files libs
%license BSDL COPYING GPL LEGAL
%dir %{_libdir}/ruby
%{_libdir}/libruby.so.%{major_minor_version}*
%{ruby_libdir}
%exclude %{ruby_libdir}/mkmf.rb
%exclude %{ruby_libdir}/rubygems.rb
%exclude %{ruby_libdir}/rubygems
%exclude %{ruby_libdir}/bundler.rb
%exclude %{ruby_libdir}/bundler
%dir %{ruby_vendordir}
%dir %{ruby_vendorlibdir}
%dir %{ruby_vendorarchdir}
%dir %{_libdir}/gems
%dir %{gem_extdir_mri}

%files devel
%{_includedir}/ruby-%{ruby_abi}
%{_libdir}/libruby.so
%{_libdir}/pkgconfig/ruby.pc
%{ruby_libdir}/mkmf.rb
%{_rpmmacrodir}/macros.ruby

%files doc
%{_docdir}/ruby
%{_datadir}/ri

%files -n rubygems
%license BSDL COPYING GPL LEGAL
%{_bindir}/gem
%{ruby_libdir}/rubygems.rb
%{ruby_libdir}/rubygems
%dir %{ruby_vendorlibdir}/rubygems
%dir %{ruby_vendorlibdir}/rubygems/defaults
%{ruby_vendorlibdir}/rubygems/defaults/operating_system.rb
%dir %{gem_dir}
%dir %{gem_dir}/build_info
%dir %{gem_dir}/cache
%dir %{gem_dir}/doc
%dir %{gem_dir}/gems
%dir %{gem_dir}/plugins
%dir %{gem_dir}/specifications
%dir %{gem_dir}/specifications/default

%files -n rubygems-devel
%{_rpmmacrodir}/macros.rubygems
%{_rpmconfigdir}/fileattrs/rubygems.attr
%{_rpmconfigdir}/rubygems.prov
%{_rpmconfigdir}/rubygems.req
%{_rpmconfigdir}/rubygemsdeps.rb

%files default-gems -f %{_builddir}/%{name}-default-gems.files
%{_bindir}/syntax_suggest

%files -n rubygem-bundler
%{_bindir}/bundle
%{_bindir}/bundler
%{ruby_libdir}/bundler.rb
%{ruby_libdir}/bundler
%{gem_dir}/specifications/default/bundler-%{bundler_version}.gemspec
%{gem_dir}/gems/bundler-%{bundler_version}

%files -n rubygem-abbrev
%{gem_dir}/gems/abbrev-0.1.2
%{gem_dir}/specifications/abbrev-0.1.2.gemspec
%{gem_dir}/cache/abbrev-0.1.2.gem

%files -n rubygem-base64
%{gem_dir}/gems/base64-0.3.0
%{gem_dir}/specifications/base64-0.3.0.gemspec
%{gem_dir}/cache/base64-0.3.0.gem

%files -n rubygem-benchmark
%{gem_dir}/gems/benchmark-0.5.0
%{gem_dir}/specifications/benchmark-0.5.0.gemspec
%{gem_dir}/cache/benchmark-0.5.0.gem

%files -n rubygem-bigdecimal
%{gem_dir}/gems/bigdecimal-4.0.1
%{gem_dir}/specifications/bigdecimal-4.0.1.gemspec
%{gem_dir}/cache/bigdecimal-4.0.1.gem
%{gem_extdir_mri}/bigdecimal-4.0.1

%files -n rubygem-csv
%{gem_dir}/gems/csv-3.3.5
%{gem_dir}/specifications/csv-3.3.5.gemspec
%{gem_dir}/cache/csv-3.3.5.gem

%files -n rubygem-debug
%{gem_dir}/gems/debug-1.11.1
%{gem_dir}/specifications/debug-1.11.1.gemspec
%{gem_dir}/cache/debug-1.11.1.gem
%{gem_extdir_mri}/debug-1.11.1
%{_bindir}/rdbg

%files -n rubygem-drb
%{gem_dir}/gems/drb-2.2.3
%{gem_dir}/specifications/drb-2.2.3.gemspec
%{gem_dir}/cache/drb-2.2.3.gem

%files -n rubygem-fiddle
%{gem_dir}/gems/fiddle-1.1.8
%{gem_dir}/specifications/fiddle-1.1.8.gemspec
%{gem_dir}/cache/fiddle-1.1.8.gem
%{gem_extdir_mri}/fiddle-1.1.8

%files -n rubygem-getoptlong
%{gem_dir}/gems/getoptlong-0.2.1
%{gem_dir}/specifications/getoptlong-0.2.1.gemspec
%{gem_dir}/cache/getoptlong-0.2.1.gem

%files -n rubygem-irb
%{gem_dir}/gems/irb-1.16.0
%{gem_dir}/specifications/irb-1.16.0.gemspec
%{gem_dir}/cache/irb-1.16.0.gem
%{_bindir}/irb

%files -n rubygem-logger
%{gem_dir}/gems/logger-1.7.0
%{gem_dir}/specifications/logger-1.7.0.gemspec
%{gem_dir}/cache/logger-1.7.0.gem

%files -n rubygem-matrix
%{gem_dir}/gems/matrix-0.4.3
%{gem_dir}/specifications/matrix-0.4.3.gemspec
%{gem_dir}/cache/matrix-0.4.3.gem

%files -n rubygem-minitest
%{gem_dir}/gems/minitest-6.0.0
%{gem_dir}/specifications/minitest-6.0.0.gemspec
%{gem_dir}/cache/minitest-6.0.0.gem
%{_bindir}/minitest

%files -n rubygem-mutex_m
%{gem_dir}/gems/mutex_m-0.3.0
%{gem_dir}/specifications/mutex_m-0.3.0.gemspec
%{gem_dir}/cache/mutex_m-0.3.0.gem

%files -n rubygem-net-ftp
%{gem_dir}/gems/net-ftp-0.3.9
%{gem_dir}/specifications/net-ftp-0.3.9.gemspec
%{gem_dir}/cache/net-ftp-0.3.9.gem

%files -n rubygem-net-imap
%{gem_dir}/gems/net-imap-0.6.4.1
%{gem_dir}/specifications/net-imap-0.6.4.1.gemspec
%{gem_dir}/cache/net-imap-0.6.4.1.gem

%files -n rubygem-net-pop
%{gem_dir}/gems/net-pop-0.1.2
%{gem_dir}/specifications/net-pop-0.1.2.gemspec
%{gem_dir}/cache/net-pop-0.1.2.gem

%files -n rubygem-net-smtp
%{gem_dir}/gems/net-smtp-0.5.1
%{gem_dir}/specifications/net-smtp-0.5.1.gemspec
%{gem_dir}/cache/net-smtp-0.5.1.gem

%files -n rubygem-nkf
%{gem_dir}/gems/nkf-0.2.0
%{gem_dir}/specifications/nkf-0.2.0.gemspec
%{gem_dir}/cache/nkf-0.2.0.gem
%{gem_extdir_mri}/nkf-0.2.0

%files -n rubygem-observer
%{gem_dir}/gems/observer-0.1.2
%{gem_dir}/specifications/observer-0.1.2.gemspec
%{gem_dir}/cache/observer-0.1.2.gem

%files -n rubygem-ostruct
%{gem_dir}/gems/ostruct-0.6.3
%{gem_dir}/specifications/ostruct-0.6.3.gemspec
%{gem_dir}/cache/ostruct-0.6.3.gem

%files -n rubygem-power_assert
%{gem_dir}/gems/power_assert-3.0.1
%{gem_dir}/specifications/power_assert-3.0.1.gemspec
%{gem_dir}/cache/power_assert-3.0.1.gem

%files -n rubygem-prime
%{gem_dir}/gems/prime-0.1.4
%{gem_dir}/specifications/prime-0.1.4.gemspec
%{gem_dir}/cache/prime-0.1.4.gem

%files -n rubygem-pstore
%{gem_dir}/gems/pstore-0.2.1
%{gem_dir}/specifications/pstore-0.2.1.gemspec
%{gem_dir}/cache/pstore-0.2.1.gem

%files -n rubygem-racc
%{gem_dir}/gems/racc-1.8.1
%{gem_dir}/specifications/racc-1.8.1.gemspec
%{gem_dir}/cache/racc-1.8.1.gem
%{gem_extdir_mri}/racc-1.8.1
%{_bindir}/racc

%files -n rubygem-rake
%{gem_dir}/gems/rake-13.3.1
%{gem_dir}/specifications/rake-13.3.1.gemspec
%{gem_dir}/cache/rake-13.3.1.gem
%{_bindir}/rake

%files -n rubygem-rbs
%{gem_dir}/gems/rbs-3.10.0
%{gem_dir}/specifications/rbs-3.10.0.gemspec
%{gem_dir}/cache/rbs-3.10.0.gem
%{gem_extdir_mri}/rbs-3.10.0
%{_bindir}/rbs

%files -n rubygem-rdoc
%{gem_dir}/gems/rdoc-7.0.4
%{gem_dir}/specifications/rdoc-7.0.4.gemspec
%{gem_dir}/cache/rdoc-7.0.4.gem
%{_bindir}/rdoc
%{_bindir}/ri

%files -n rubygem-readline
%{gem_dir}/gems/readline-0.0.4
%{gem_dir}/specifications/readline-0.0.4.gemspec
%{gem_dir}/cache/readline-0.0.4.gem

%files -n rubygem-reline
%{gem_dir}/gems/reline-0.6.3
%{gem_dir}/specifications/reline-0.6.3.gemspec
%{gem_dir}/cache/reline-0.6.3.gem

%files -n rubygem-repl_type_completor
%{gem_dir}/gems/repl_type_completor-0.1.12
%{gem_dir}/specifications/repl_type_completor-0.1.12.gemspec
%{gem_dir}/cache/repl_type_completor-0.1.12.gem

%files -n rubygem-resolv-replace
%{gem_dir}/gems/resolv-replace-0.1.1
%{gem_dir}/specifications/resolv-replace-0.1.1.gemspec
%{gem_dir}/cache/resolv-replace-0.1.1.gem

%files -n rubygem-rexml
%{gem_dir}/gems/rexml-3.4.4
%{gem_dir}/specifications/rexml-3.4.4.gemspec
%{gem_dir}/cache/rexml-3.4.4.gem

%files -n rubygem-rinda
%{gem_dir}/gems/rinda-0.2.0
%{gem_dir}/specifications/rinda-0.2.0.gemspec
%{gem_dir}/cache/rinda-0.2.0.gem

%files -n rubygem-rss
%{gem_dir}/gems/rss-0.3.2
%{gem_dir}/specifications/rss-0.3.2.gemspec
%{gem_dir}/cache/rss-0.3.2.gem

%files -n rubygem-syslog
%{gem_dir}/gems/syslog-0.3.0
%{gem_dir}/specifications/syslog-0.3.0.gemspec
%{gem_dir}/cache/syslog-0.3.0.gem
%{gem_extdir_mri}/syslog-0.3.0

%files -n rubygem-test-unit
%{gem_dir}/gems/test-unit-3.7.5
%{gem_dir}/specifications/test-unit-3.7.5.gemspec
%{gem_dir}/cache/test-unit-3.7.5.gem
%{_bindir}/test-unit

%files -n rubygem-typeprof
%{gem_dir}/gems/typeprof-0.31.1
%{gem_dir}/specifications/typeprof-0.31.1.gemspec
%{gem_dir}/cache/typeprof-0.31.1.gem
%{_bindir}/typeprof

%changelog
%autochangelog
