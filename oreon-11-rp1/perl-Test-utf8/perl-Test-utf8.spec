%global source0_hash a24737b31ec016189a16c7f0e4de2ff0cbd705ccaef7066387195139c5bc2439

Name:           perl-Test-utf8
Version:        1.03
Release:        4%{?dist}
Summary:        Handy utf8 tests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-utf8
Source0:        https://www.cpan.org/modules/by-module/Test/Test-utf8-%{version}.tar.gz
# Do not require author's dependencies
Patch0:         Test-utf8-1.02-Drop-useless-build-time-dependencies.patch
# Until the POD has changed, there is no point in regenerating README. This
# saves from a dependency on Module::Install::ReadmeFromPod.
Patch1:         Test-utf8-1.02-Do-no-regenerate-README.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::Builder::Tester) >= 0.09
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
This module is a collection of tests that's useful when dealing with utf8
strings in Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-utf8-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -rf ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::utf8.3*

%changelog
%autochangelog
