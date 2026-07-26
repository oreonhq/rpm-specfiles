%global source0_hash cfd7044483f34e6fa64080bf7c4bc10ff6173410c350066fe65e090c3b81b6e9

Name:           perl-Math-Spline
Version:        0.02
Release:        29%{?dist}
Summary:        Cubic Spline Interpolation of data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Spline
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Spline-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Derivative)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This package provides cubic spline interpolation of numeric data. The data
is passed as references to two arrays containing the x and y ordinates. It
may be used as an exporter of the numerical functions or, more easily as a
class module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Spline-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Release
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
