%global source0_hash 8c4297c2bab22b72bb4fce9df26c6360d4a4166a0a97b29a58465a2592dbd01c

Name: 		perl-Date-Pcalc
Version:	6.1
Release:	49%{?dist}
Summary:	Gregorian calendar date calculations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Date-Pcalc
Source0: 	https://cpan.metacpan.org/authors/id/S/ST/STBEY/Date-Pcalc-%{version}.tar.gz
# Perl 5.16 compatibility, CPAN RT #76442
Patch0:		Date-Pcalc-6.1-boolean.patch
# Related: rt#101232
Patch1:         Date-Pcalc-6.1-century.patch
# Fixed error "Unescaped left brace in regex is deprecated"
Patch2:         Date-Pcalc-6.1-Fix-unescaped-left-brace-in-regex.patch
# bool, true and false are keywords in modern C
Patch3:         0001-Fix-bool-detection.patch

BuildRequires:  %{_bindir}/iconv
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Bit::Vector) >= 7.1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp::Clan) >= 5.3
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(vars)
# Tests only
# nothing
Requires:       perl(bytes)
Requires:       perl(Bit::Vector) >= 7.1
Requires:       perl(Carp::Clan) >= 5.3

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Bit::Vector\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Clan\\)$

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

%check
make test

# Interactive build, prompts if binary of PP version should be built
# Defaults to binary if gcc is found (default Fedora buildroot contains gcc)
# There's No option available to specify explicitly
%files
%license GNU_GPL.txt Artistic.txt
%doc CHANGES.txt README.txt EXAMPLES.txt CREDITS.txt
%{perl_vendorarch}/auto/Date
%{perl_vendorarch}/Date
%{_mandir}/man3/*

%changelog
%autochangelog
