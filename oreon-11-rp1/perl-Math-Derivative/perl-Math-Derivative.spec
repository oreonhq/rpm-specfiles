%global source0_hash 14c0b3fa05dcb74a44a9de6b4b08c3e58e672826b5f8e47535325b64f6ee69e6

Name:           perl-Math-Derivative
Version:        1.01
Release:        24%{?dist}
Summary:        Numeric 1st and 2nd order differentiation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Derivative
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Derivative-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Math::Utils) >= 1.10
BuildRequires:  perl(Test::More)
# Optional tests
# Test::CheckManifest not used
BuildRequires:  perl(Test::Pod) >= 1.22

%description
This Perl package exports functions for performing numerical first
(Derivative1) and second Derivative2) order differentiation on vectors of
data. They both take references to two arrays containing the x and y
ordinates of the data and return an array of the 1st or 2nd derivative at
the given x ordinates. Derivative2 may optionally be given values to use
for the first derivative at the start and end points of the data -
otherwise 'natural' values are used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Derivative-%{version}
# Convert EOL
sed -i 's/\r//' README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
