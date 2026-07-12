%global source0_hash abcb3610fca06d9a1d9916ab6980743a61d85af55f9fd376bea6712a89a69c78

Name:           perl-Data-Taxi
Version:        0.96
Release:        43%{?dist}
Summary:        Taint-aware, XML-ish data serialization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Taxi
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKO/Data-Taxi-%{version}.tar.gz
Patch0:         no-debug-showstuff.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test)

Provides:       perl(Data::Taxi)
Provides:       perl(Data::Taxi)
%description
Taxi (Taint-Aware XML-Ish) is a data serializer with several handy
features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Taxi-%{version}
%patch -P0 -p1
perl -pi -e 's/\r//go' README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data::Taxi*

%changelog
%autochangelog
