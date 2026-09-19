%global source0_hash da3b81414c63f8d9218d116745a88b948c46c98b187634f629892e54001bc35a

Name:           perl-Text-RecordParser
Version:        1.6.5
Release:        34%{?dist}
Summary:        Read record-oriented files
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Text-RecordParser
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCLARK/Text-RecordParser-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::TabularDisplay)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This module is for reading record-oriented data in a delimited text file.
The most common example have records separated by newlines and fields
separated by commas or tabs, but this module aims to provide a consistent
interface for handling sequential records in a file however they may be
delimited. Typically this data lists the fields in the first line of the
file, in which case you should call bind_header to bind the field name (or
not, and it will be called implicitly). If the first line contains data,
you can still bind your own field names via bind_fields. Either way, you
can then use many methods to get at the data as arrays or hashes.

%package tools
Summary:        The %{name} command-line tools
Obsoletes:      %{name} < 1.6.5-21

%description tools
This package contains the directly-runnable tools from %{name}
(tab2graph, tablify etc.) They are packaged separately so things that
only need the %{name} modules do not also pull in dependencies
specific to the tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-RecordParser-%{version}
# Remove bundled modules
/usr/bin/rm -r ./inc/*
/usr/bin/perl -pi -e '/^inc\//d' MANIFEST
# Fix shebangs
/usr/bin/perl -pi -e 's|^#!perl|#!%{__perl}|' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man[13]/*

%files tools
%{_bindir}/*

%changelog
%autochangelog
