%global source0_hash 7a24fd111c17f20d337bdebaac39664834a9ad5ec00aa43108de91f56d86de82
Name:           perl-Net-GPSD
Version:        0.39
Release:        1%{?dist}
Summary:        Provides an object client interface to the gpsd server daemon
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-GPSD
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Net-GPSD-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GPS::OID)
BuildRequires:  perl(Geo::Forward)
BuildRequires:  perl(Geo::Functions)
BuildRequires:  perl(Geo::Inverse)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
