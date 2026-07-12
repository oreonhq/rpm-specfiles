%global source0_hash fcb2b424844bb13bcad46b1c7aa239b5a09bab2556f53bd1f27fad90c260d33d

Name:		perl-DateTime-Calendar-Julian
Version:	0.107
Release:	12%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:	Julian Calendar support for DateTime.pm
Url:		https://metacpan.org/release/DateTime-Calendar-Julian
Source:		https://cpan.metacpan.org/authors/id/W/WY/WYANT/DateTime-Calendar-Julian-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-generators, perl-interpreter, make
BuildRequires:	perl(DateTime) >= 1.48
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

Provides:       perl(DateTime::Calendar::Julian)
%description
DateTime object in the Julian calendar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Calendar-Julian-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Calendar::Julian.3pm*

%changelog
%autochangelog
