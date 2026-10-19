%global source0_hash 4ab122508d2fb86d171a15f4006e5cf896d5facfa65219c0b243a89906258e59
Name:           perl-Data-Stag
Version:        0.14
Release:        29%{?dist}
Summary:        Perl package for Structured Tags datastructures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Stag
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Stag-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(GD)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Graph)
BuildRequires:  perl(Graph::Directed)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(Test)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Label)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is for manipulating data as hierarchical tag/value pairs
(Structured TAGs or Simple Tree AGgreggates). These datastructures can be
represented as nested arrays, which have the advantage of being native to
Perl. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Stag-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
