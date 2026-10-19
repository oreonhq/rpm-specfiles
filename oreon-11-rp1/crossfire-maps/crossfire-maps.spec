%global source0_hash f6df5fd605dd3b83dce1aa730390443b09569e6fae93bef058cd8f52fedc17da
Name:           crossfire-maps
Version:        1.71.0
Release:        1%{?dist}
Summary:        Map files for the crossfire server
License:        GPL-2.0-or-later
URL:            http://crossfire.real-time.com
Source0:        http://downloads.sourceforge.net/crossfire/crossfire-%{version}.maps.tar.bz2
Patch0:		crossfire-maps-1.60.0-python.patch
BuildArch:      noarch
Requires:       crossfire
Obsoletes:      crossfire-maps-devel
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Map files for the crossfire server.

%prep

%setup -q -c -n %{name}-%{version}

%patch -P0 -p0

chmod -x maps/python/IPO/README
chmod -x maps/python/IPO/*.py
chmod -x maps/scorn/misc/beginners2
chmod -x maps/styles/monsterstyles/sylvan/*
chmod -x maps/planes/*
chmod -x maps/pup_land/s_f/*
chmod -x maps/pup_land/ancient/castle/*
chmod -x maps/pup_land/ancient/volcano/*
chmod -x maps/pup_land/ancient/mountain/*
chmod -x maps/pup_land/lone_town/cave/*
chmod -x maps/templates/keep/*.tpl
#chmod -x maps/templates/guild/bigchest
chmod -x maps/navar_city/troll_canyon/*
chmod -x maps/brest/sow/sow.1
chmod -x maps/lake_country/elven_moon/*
#chmod -x maps/unlinked/casino/casino_infernal
chmod -x maps/santo_dominion/shaft/*
chmod -x maps/santo_dominion/temple_naive/*
chmod -x maps/darcap/temple_justice/*
chmod -x maps/brest/sow/sow

%{__sed} -i 's/\r//' maps/templates/keep/keep1.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep2.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep3.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep_b.tpl
%{__sed} -i 's/\r//' maps/templates/keep/keep_roof.tpl

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crossfire
cp -a maps $RPM_BUILD_ROOT%{_datadir}/crossfire/
rm -f $RPM_BUILD_ROOT%{_datadir}/crossfire/maps/COPYING
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
