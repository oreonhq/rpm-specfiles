%global source0_hash 4dcd17afce0955ee6b2a9bdd6e06669b9fa1daca161e11b4808f0e33a0ce0c99
Name:           perl-Array-IntSpan
Version:        2.004
Release:        17%{?dist}
Summary:        Handles arrays of scalars or objects using integer ranges
License:        Artistic-2.0
URL:            https://metacpan.org/release/Array-IntSpan
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Array-IntSpan-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Array::IntSpan brings the speed advantages of Set::IntSpan to arrays. Uses
include manipulating grades, routing tables, or any other situation where you
have mutually exclusive ranges of integers that map to given values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Array-IntSpan-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
