%global source0_hash 163020315d5c5441836ac79e08a77b428f277fd090bea4fa80da7077b2436aba
Name:             perl-Geo-IP
Summary:        Efficient Perl bindings for the GeoIP location database
Version:          1.51
Release:        1%{?dist}
URL:              https://metacpan.org/release/Geo-IP
License:          GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Geo-IP-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  GeoIP-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
This package contains Perl bindings for the GeoIP IP/host-name to
country/location/organization database.

This package requires Maxmind's GeoIP libraries but is often faster than other,
similar modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Geo-IP-%{version}
sed -i -e '1s,#!.*perl,#!%{__perl},' example/netspeed.pl example/netspeedcell.pl

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}
find example/ -type f | xargs chmod -x
%install
make pure_install DESTDIR=%{buildroot}
chmod -R u+w %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
