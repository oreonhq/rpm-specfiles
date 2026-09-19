%global source0_hash 8090cfbb61123437eefec3e3bed86005d1f7c5a529fb6fda2ebebc6564b9aa10

Name:           perl-Module-Compile
Version:        0.38
Release:        18%{?dist}
Summary:        Perl Module Compilation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Compile
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Compile-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::SHA1) >= 2.13
BuildRequires:  perl(Filter::Util::Call)
# Tests only
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML)
Requires:       perl(Digest::SHA1) >= 2.13
Requires:       perl(Filter::Util::Call)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Digest::SHA1\\)$

%description
This module provides a system for writing modules that compile other
Perl modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Compile-%{version}
rm -rf inc/ && sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
