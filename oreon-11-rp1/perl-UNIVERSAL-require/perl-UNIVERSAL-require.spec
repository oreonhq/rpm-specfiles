%global source0_hash d467cd26e06c8c3b203fd3bc0796ae6c837ac5e310093c82267ff5df850f1a03
Name:           perl-UNIVERSAL-require
Version:        0.19
Release:        1%{?dist}
Summary:        Require() modules from a variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-require
Source0:        https://cpan.metacpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-require-%{version}.tar.gz
Patch0:         UNIVERSAL-require-0.18-provides.patch
BuildArch:      noarch
Requires:       perl(UNIVERSAL)
Provides:       perl(UNIVERSAL::require)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n UNIVERSAL-require-%{version}

# Hide "package UNIVERSAL" from rpm to avoid bogus provide
%patch -P 0

%build

perl Makefile.PL INSTALLDIRS=vendor
make
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19-14
- Prepare for Oreon 11 (RP1)
