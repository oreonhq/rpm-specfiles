# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b941aec9011864978dd7fdeb052b1943535824169d2aa2b0e7eae9ab807584ac
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:             gengetopt
Version:          2.23
Release:          1%{?dist}
Summary:          Tool to write command line option parsing code for C programs
License:          GPL-3.0-or-later
URL:              http://www.gnu.org/software/gengetopt/
Source0:          ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  texinfo
BuildRequires: make
Provides:         bundled(gnulib)

%description
Gengetopt is a tool to generate C code to parse the command line arguments
argc and argv that are part of every C or C++ program. The generated code uses
the C library function getopt_long to perform the actual command line parsing.

%prep
%oreon_sha256
%setup -q

chmod 644 ./AUTHORS
chmod 644 ./ChangeLog
chmod 644 ./COPYING
chmod 644 ./LICENSE
chmod 644 ./NEWS
chmod 644 ./README
chmod 644 ./THANKS
chmod 644 ./TODO
chmod 644 ./doc/README.example
chmod 644 ./doc/index.html
chmod 644 ./src/parser.yy
chmod 644 ./src/scanner.ll
find . -name '*.c' -exec chmod 644 {} ';'
find . -name '*.cc' -exec chmod 644 {} ';'
find . -name '*.cpp' -exec chmod 644 {} ';'
find . -name '*.h' -exec chmod 644 {} ';'
find . -name '*.ggo' -exec chmod 644 {} ';'

%build
%configure
make

%install
%make_install INSTALL="%{__install} -p"
rm -frv %{buildroot}%{_infodir}/dir
rm -frv %{buildroot}%{_docdir}/%{name}

mkdir ./examples
pushd ./doc
  cp -p README.example ../examples
  cp -p main1.cc sample1.ggo ../examples
  cp -p main2.c sample2.ggo ../examples
popd

%check
make check

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/index.html doc/%{name}.html
%doc examples/
%license COPYING LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_infodir}/*.info*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
