%global source0_hash 1bbc8893da69f2502483d9e5e2556494b2589d7595729a79c63689c6e1b17a87
Name:           perl-Data-Dumper-Names
Version:        0.03
Release:        1%{?dist}
Summary:        Data::Dumper like module for printing and eval data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dumper-Names
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/Data-Dumper-Names-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(PadWalker) >= 0.13
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PadWalker\\)$
Provides:       perl(Data::Dumper::Names)
# oreon:deps
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The essential module Data::Dumper is used for printing perl data structures or 
suitable for eval. Data::Dumper::Names dump variables with names and without
source filter. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Dumper-Names-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export PERL5LIB="$(pwd)/no-such-directory"
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
