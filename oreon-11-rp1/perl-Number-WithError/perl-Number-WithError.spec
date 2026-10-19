%global source0_hash dff6a0727e7844ea67837bdfadd552b86f6b216d18ee8ee46842b22ccef0f554
Name:           perl-Number-WithError
Version:        1.01
Release:        1%{?dist}
Summary:        Numbers with error propagation and scientific rounding
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-WithError
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Number-WithError-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Math::BigFloat) >= 1.40
Requires:       perl(overload)
Requires:       perl(Params::Util) >= 0.10
Requires:       perl(prefork) >= 1.00
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Params::Util|prefork)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::LectroTest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(prefork)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This class is a container class for numbers with a number of associated
symmetric and asymmetric errors. It overloads practically all common
arithmetic operations and trigonometric functions to propagate the errors.
It can do proper scientific rounding.

You can use Math::BigFloat objects as the internal representation of numbers
in order to support arbitrary precision calculations.

Errors are propagated using Gaussian error propagation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Number-WithError-%{version}
# Remove bundled modules
rm -rf inc/*
sed -i -e '/^inc\//d' MANIFEST
# Correct encoding
sed -i -e 's/\r//' Changes

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
