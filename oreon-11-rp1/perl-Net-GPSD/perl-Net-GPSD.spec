%global source0_hash 7a24fd111c17f20d337bdebaac39664834a9ad5ec00aa43108de91f56d86de82

Name:           perl-Net-GPSD
Version:        0.39
Release:        43%{?dist}
Summary:        Provides an object client interface to the gpsd server daemon

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-GPSD
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Net-GPSD-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Geo::Forward) => 0.09
BuildRequires:  perl(Geo::Functions) => 0.06
BuildRequires:  perl(Geo::Inverse) => 0.02
BuildRequires:  perl(GPS::OID)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Net::GPSD provides an object client interface to the gpsd server daemon.
gpsd is an open source GPS daemon from http://gpsd.berlios.de/.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-GPSD-%{version}
chmod -c a-x bin/example-* doc/*.cgi

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES LICENSE README
%doc doc/ bin/example-*
%{perl_vendorlib}/Net/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
