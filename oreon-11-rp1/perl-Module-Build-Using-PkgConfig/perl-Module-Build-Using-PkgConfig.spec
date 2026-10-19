%global source0_hash 11774a6914bcfa0915f9f01c3041b16878d52ad86d83ecedbe62e68d4f41ecc1
Name:           perl-Module-Build-Using-PkgConfig
Version:        0.03
Release:        18%{?dist}
Summary:        Extend Module::Build to easily use platform libraries provided by pkg-config
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Build-Using-PkgConfig/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Module-Build-Using-PkgConfig-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This subclass of Module::Build provides some handy methods to assist the
Build.PL script of XS-based module distributions that make use of platform
libraries managed by pkg-config.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Build-Using-PkgConfig-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
