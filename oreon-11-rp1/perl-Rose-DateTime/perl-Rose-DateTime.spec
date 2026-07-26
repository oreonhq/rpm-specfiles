%global source0_hash 1e42802d0944e9669599b7d0dea1e77a0d17a42123f8ca555180db4e7218e34a

Name:		perl-Rose-DateTime
Version:	0.540
Release:	35%{?dist}
Summary:	DateTime helper functions and objects
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-DateTime
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DateTime-%{version}.tar.gz
BuildArch:	noarch
BuildRequires: make
BuildRequires:	perl-generators
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Rose::Object)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Exporter)

%filter_from_requires /perl(Rose::DateTime::Util)/d
%filter_setup

%description
The Rose::DateTime::* modules provide a few convenience functions and
objects for use with DateTime dates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Rose-DateTime-%{version}
find . -type f -executable -exec chmod -x {} \;

%build
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
%{perl_vendorlib}/Rose/DateTime.pm
%{perl_vendorlib}/Rose/DateTime/
%{_mandir}/man3/Rose::DateTime*.3pm*

%changelog
%autochangelog
