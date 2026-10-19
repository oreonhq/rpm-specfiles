%global source14_hash b7d02f17586602f8a3f5cf7a122c06695736cb477e0d8db0af0bf02ded12b741
%global source13_hash 45c890e182d387c0e1af986d7b8a441168c9341fd66dfe00542c79b1834b0c52
%global source12_hash 1123be350a193a7b3209625ef1cb56868884af4f594e89150819743ddc9610f7
%global source11_hash 4f3c944dd18a814a48720d064362eb4065153acef3a90c3750e365b89cec7e75
%global source10_hash e0d9dc7c131ff581b90d64f2e1ca25b0d7b3cdb40b81319e6c225a43d7cd100c
%global source9_hash 6a71a6d424b4718eaa700009e5ea904117b93807a0d50d0e495ca11373948af7
%global source8_hash a42b2d3d3b4b937ed3429f7ee9d98448344b4342eb491fc72414885cb71dc93e
%global source7_hash e55598d3630ae6105c1bff93ee4f0e4fa544e2e8b695b18f82d08e55f4ca84c4
%global source6_hash fcf3475da1469e060d6126f14adad230d77c8829730477569f50ce0ddc7b96cc
%global source5_hash 1ad81c3749ec6820a2375c2da3567e7dbbd9f4ec1d8a144683d077f7a3790fc0
%global source4_hash 1591660c87eeec7ea3f34c24727c9a2958aa1493cb877d4c89c6101f60c0550e
%global source3_hash c5de89a1b2d1ba7c5f4fa9bf5ffa8b456c2fdc7e00d48db440f4a1dcff230044
%global source2_hash 6af3e926ef8be4d8cb76ad66b087f4724fb366fe282c6f3f79da4ab3a52c0418
%global source0_hash 6a71a6d424b4718eaa700009e5ea904117b93807a0d50d0e495ca11373948af7
%global svnversion 4974
%global date 20250303
%global maj_ver 4.3
Name:       skychart
Version:    %{maj_ver}^%{date}.svn%{svnversion}
Release:        1%{?dist}
Summary:        Planetarium software for the advanced amateur astronomer
License:    GPL-2.0-or-later AND LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:        http://www.ap-i.net/skychart/
Source0:        %{name}-%{maj_ver}-%{svnversion}-src-nopatents.tar.xz
Source1:    generate-tarball.sh
Source2:    http://sourceforge.net/projects/skychart/files/4-source_data/data_spicesun.tgz
Source3:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcvs.tgz
Source4:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_tycho2.tgz
Source5:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_wds.tgz
Source6:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_idx.tgz
Source7:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_leda.tgz
Source8:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_barnard.tgz
Source9:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcm.tgz
Source10:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gpn.tgz
Source11:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_lbn.tgz
Source12:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_ocl.tgz
Source13:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_sh2.tgz
Source14:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_vdb.tgz
Patch:      skychart-4.3-nostrip.patch
Patch:      skychart-4.1-wgetdata.patch
Patch:      skychart-4.3-satmessage.patch
Patch:      skychart-4.3-noupdatemenu.patch
Patch:      skychart-4.3-fpc-3.2.4.patch
ExclusiveArch: %{fpc_arches}
ExcludeArch: %{ix86}
Requires: libpasastro
Requires: tzdata
Requires: xdg-utils
Requires: xplanet
Recommends: openssl-libs
Recommends: calceph-libs
Recommends: chealpix
Recommends: skychart-catgen = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  gtk2-devel
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-tools
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
This program enables you to draw sky charts, making use of the data in 16
catalogs of stars and nebulae. In addition the position of planets,
asteroids and comets are shown.

The purpose of this program is to prepare different sky maps for a
particular observation. A large number of parameters help you to choose
specifically or automatically which catalogs to use, the colour and the
dimension of stars and nebulae, the representation of planets, the display
of labels and coordinate grids, the superposition of pictures, the
condition of visibility and more. All these features make this celestial
atlas more complete than a conventional planetarium.

%package doc
Summary:        Documentation files for Skychart
License:        CC-BY-SA-3.0 OR GFDL-1.3-no-invariants-or-later
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation files from the official Skychart wiki provided
within the program as an offline copy.

%package data-stars
Summary:        Additional star catalogs for Skychart
License:        LicenseRef-Fedora-Public-Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description data-stars
Additional star catalogs for Skychart. This package install all the standard
stars catalog down to magnitude 12, variable and double stars:
Tycho 2; General Catalogue of Variable Stars; Washington Double Stars.

%package data-dso
Summary:        Additional Deep Sky Object catalogs for Skychart
License:        LicenseRef-Fedora-Public-Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description data-dso
Additional DSO catalogs for Skychart. This package install all the standard
nebulae catalogs: LEDA Catalogue; Lynds Bright Nebulae; Open Cluster Data;
Globular Clusters in the Milky Way; Galactic Planetary Nebulae;
Barnard Catalogue of Dark Nebulae; Sharpless Catalog.

%package catgen
Summary:        Custom catalog builder for Skychart
License:        GPL-2.0-or-later
Provides:       catgen = %{version}-%{release}
%description catgen
Custom catalog builder for Skychart.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{maj_ver}-%{svnversion}-src

%autopatch -p1

# Fix executable bit set on sources
find skychart -type f -print0 | xargs -0 chmod -x

# Put additional catalogs files where are required for installation

cp -p %SOURCE2 ./BaseData
cp -p %SOURCE3 ./BaseData
cp -p %SOURCE4 ./BaseData
cp -p %SOURCE5 ./BaseData
cp -p %SOURCE6 ./BaseData
cp -p %SOURCE7 ./BaseData
cp -p %SOURCE8 ./BaseData
cp -p %SOURCE9 ./BaseData
cp -p %SOURCE10 ./BaseData
cp -p %SOURCE11 ./BaseData
cp -p %SOURCE12 ./BaseData
cp -p %SOURCE13 ./BaseData
cp -p %SOURCE14 ./BaseData

%build

./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}
make fpcopts="-O2 -gw4 -Cg"
%install
make install PREFIX=%{buildroot}%{_prefix}
make install install_data PREFIX=%{buildroot}%{_prefix}
make install install_doc PREFIX=%{buildroot}%{_prefix}
make install install_cat1 PREFIX=%{buildroot}%{_prefix}
make install install_cat2 PREFIX=%{buildroot}%{_prefix}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/net.ap_i.*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n skychart-doc -f %{oreon_filedir}/skychart-doc.list
%files -n skychart-data-stars -f %{oreon_filedir}/skychart-data-stars.list
%files -n skychart-data-dso -f %{oreon_filedir}/skychart-data-dso.list
%files -n skychart-catgen -f %{oreon_filedir}/skychart-catgen.list

%changelog

%autochangelog
