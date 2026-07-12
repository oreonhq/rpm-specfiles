%global source0_hash 319601feec17fae344988a5ee91cfc6a0bcfe742af77dba254724c3268b2a60f

Name:           perl-Time-Piece-MySQL
Version:        0.06
Release:        29%{?dist}
Summary:        MySQL-specific methods for Time::Piece
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-Piece-MySQL
Source0:        https://cpan.metacpan.org/modules/by-module/Time/Time-Piece-MySQL-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Time::Piece) >= 1.03
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(warnings)
# Dependencies:
Requires:       perl(Time::Piece) >= 1.03

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Time::Piece\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::Piece\\)\s*$

Provides:       perl(Time::Piece::MySQL)
Provides:       perl(Time::Piece::MySQL)
%description
The Time::Piece::MySQL module can be used instead of, or in addition to,
Time::Piece to add MySQL-specific date-time methods to Time::Piece objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Time-Piece-MySQL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Time/
%{_mandir}/man3/Time::Piece::MySQL.3*

%changelog
%autochangelog
