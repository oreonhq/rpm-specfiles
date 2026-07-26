%global source0_hash 35e8a8bbfcdb35d86dd4852a9cd32cfb455a9b42e22669186e920c8aca017aef

Name:		perl-Time-Clock
Version:	1.03
Release:	34%{?dist}
Summary:	Twenty-four hour clock object with nanosecond precision
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Time-Clock
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Time-Clock-%{version}.tar.gz
BuildArch:	noarch
BuildRequires: make
BuildRequires:	perl-generators
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Time::HiRes)
Requires:	perl(Time::HiRes)

%description
A Time::Clock object is a twenty-four hour clock with nanosecond precision
and wrap-around. It is a clock only; it has absolutely no concept of dates.
Vagaries of date/time such as leap seconds and daylight savings time are
unsupported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Clock-%{version}

%build
find . -type f -executable -exec chmod -x {} \;
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Time/
%{_mandir}/man3/Time::Clock.3pm*

%changelog
%autochangelog
