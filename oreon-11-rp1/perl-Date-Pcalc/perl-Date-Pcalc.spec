%global source0_hash 8c4297c2bab22b72bb4fce9df26c6360d4a4166a0a97b29a58465a2592dbd01c
Name: 		perl-Date-Pcalc
Version:	6.1
Release:        1%{?dist}
Summary:        Gregorian calendar date calculations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Date-Pcalc
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STBEY/Date-Pcalc-%{version}.tar.gz
Patch0:		Date-Pcalc-6.1-boolean.patch
Patch1:         Date-Pcalc-6.1-century.patch
Patch2:         Date-Pcalc-6.1-Fix-unescaped-left-brace-in-regex.patch
Patch3:         0001-Fix-bool-detection.patch
Requires:       perl(bytes)
Requires:       perl(Bit::Vector) >= 7.1
Requires:       perl(Carp::Clan) >= 5.3
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Bit::Vector\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Clan\\)$
# oreon:deps
BuildRequires:  //bin/iconv
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(bytes)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package consists of a Perl module for all kinds of date calculations based
on the Gregorian calendar (the one used in all western countries today), 
thereby complying with all relevant norms and standards: ISO/R 2015-1971, 
DIN 1355 and, to some extent, ISO 8601 (where applicable).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Pcalc-%{version}
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 </dev/null
make %{?_smp_mflags}
%install
%{_bindir}/iconv --from-code=ISO-8859-1 --to-code=UTF-8 blib/man3/Date::Pcalc.3pm -o blib/man3/Date::Pcalc.3pm-utf8
mv blib/man3/Date::Pcalc.3pm-utf8 blib/man3/Date::Pcalc.3pm 
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
