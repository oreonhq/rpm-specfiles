%global source0_hash 94ce27a546cd57cb52e080a8f2533a7cc2350028388582485bd1039a37871f9c

Name:           perl-UNIVERSAL-moniker
Version:        0.08
Release:        55%{?dist}
Summary:        Real world naming for classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-moniker
Source0:        https://cpan.metacpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-moniker-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
# (nothing)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Lingua::EN::Inflect)
# Dependencies
# (nothing)

# Filter bogus provide for perl(UNIVERSAL)
%global __provides_exclude ^perl\\(UNIVERSAL\\)

Provides:       perl(UNIVERSAL::moniker)
Provides:       perl(UNIVERSAL::moniker)
%description
UNIVERSAL::moniker enables classes to make a good 
guess at what they would be called in the real world.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n UNIVERSAL-moniker-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::moniker.3*

%changelog
%autochangelog
