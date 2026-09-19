%global source0_hash b4f02933a2ab1421615e9d5954d7174f86afec3d16f7fdb515e8c1a861f0fcbf

Name:           netcdf-perl
Version:        1.2.4
Release:        58%{?dist}
Summary:        Perl extension module for scientific data access via the netCDF API

# Automatically converted from old format: NetCDF - review is highly recommended.
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf-perl/
Source0:        ftp://ftp.unidata.ucar.edu/pub/netcdf-perl/netcdf-perl-%{version}.tar.gz
Source1:        netcdf-2.3
BuildRequires: make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)
BuildRequires:  netcdf-devel
Provides:  perl-NetCDF = %{version}-%{release}

%description
The netCDF Perl package is a perl extension module for scientific data access
via the netCDF API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e '1s,/usr/local/bin/perl,%{_bindir}/perl,' src/perl/test.pl

%build
cd src
export PERL_MANDIR=%{_mandir}
export CPP_NETCDF=-I%{_includedir}/netcdf
export LD_NETCDF="-lnetcdf"
%configure
cd perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
cd src
# use the top-level Makefile only for manpage installation
make installed_manuals MANDIR=$RPM_BUILD_ROOT%{_mandir}
cd perl
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

# install netcdf-2 man page
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man3
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man3

%check
cd src
make test

%files
%license src/COPYRIGHT
%doc src/HISTORY src/README src/perl/test.pl
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/NetCDF.pm
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
