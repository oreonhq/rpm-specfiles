%global source0_hash da3b81414c63f8d9218d116745a88b948c46c98b187634f629892e54001bc35a
Name:           perl-Text-RecordParser
Version:        1.6.5
Release:        1%{?dist}
Summary:        Read record-oriented files
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Text-RecordParser
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCLARK/Text-RecordParser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(GraphViz)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::TabularDisplay)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list
%files -n perl-Text-RecordParser-tools -f %{oreon_filedir}/perl-Text-RecordParser-tools.list

%changelog

%autochangelog
