%global source0_hash a24737b31ec016189a16c7f0e4de2ff0cbd705ccaef7066387195139c5bc2439
Name:           perl-Test-utf8
Version:        1.03
Release:        1%{?dist}
Summary:        Handy utf8 tests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-utf8
Source0:        https://www.cpan.org/modules/by-module/Test/Test-utf8-%{version}.tar.gz
Patch0:         Test-utf8-1.02-Drop-useless-build-time-dependencies.patch
Patch1:         Test-utf8-1.02-Do-no-regenerate-README.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
