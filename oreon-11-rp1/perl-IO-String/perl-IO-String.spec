# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2a3f4ad8442d9070780e58ef43722d19d1ee21a803bf7c8206877a10482de5a0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-IO-String
Version:        1.08
Release:        1%{?dist}
Summary:        Emulate file interface for in-core strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-String
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/IO-String-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(Test)
Requires:       perl(Data::Dumper)
Requires:       perl(IO::Handle)

%description
The "IO::String" module provides the "IO::File" interface for in-core
strings.  An "IO::String" object can be attached to a string, and
makes it possible to use the normal file operations for reading or
writing data, as well as for seeking to various locations of the
string.  This is useful when you want to use a library module that
only provides an interface to file handles on data that you have in a
string variable.

Note that perl-5.8 and better has built-in support for "in memory"
files, which are set up by passing a reference instead of a filename
to the open() call. The reason for using this module is that it makes
the code backwards compatible with older versions of Perl.

%prep
%oreon_sha256
%setup -q -n IO-String-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
