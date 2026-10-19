%global source0_hash 7d7015bee0803f4b8257eefc5e1d7f437d581c6dcc0cd48628acf9896f0bc491
Name:           opencity
Version:        0.0.6.5
Release:        28%{?dist}
Summary:        Full 3D city simulator game project
License:        GPL-2.0-only
URL:            http://www.opencity.info
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}stable.tar.bz2
Source1:        %{name}.appdata.xml
Patch0:        %{name}.remove_bundled_libraries.patch
Patch1:        %{name}.remove_binreloc_references.patch
Requires: %{name}-data
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxpath-devel
# /oreon:deps
%description
This is just another city simulation.
The idea is simple: you have to build a city with 3 types of "zones":
Residential, Commercial and Industrial.
They depend on each other during their development.
Try to give them what they need and watch your city growing up.

%package data
Summary: Data files for opencity
BuildArch: noarch
%description data
Data files for opencity.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}stable
%patch -P0

%patch -P1
rm -rf src/tinyxml/
rm -rf src/tinyxpath/
rm -rf src/binreloc/

# Replace obsolete macro
sed -i 's+AC_PROG_LIBTOOL+LT_INIT+g' configure.ac

#Fix bad include
sed -i 's+#include "tinyxml/tinyxml.h"+#include "tinyxml.h"+g' src/zen.cpp 

#Fix some paths (only sDataDir and sConfigDir, because sSaveDir is detected without binreloc)
sed -i 's+static string sDataDir\t\t= "";+static string sDataDir\t\t= "%{_datadir}/%{name}/";+g' src/main.cpp
sed -i 's+static string sConfigDir\t= "";+static string sConfigDir\t= "%{_sysconfdir}/%{name}/";+g' src/main.cpp
sed -i 's+static string sDataDir\t\t= "";+static string sDataDir\t\t= "%{_datadir}/%{name}/";+g' src/zen.cpp
sed -i 's+static string sConfigDir\t= "";+static string sConfigDir\t= "%{_sysconfdir}/%{name}/";+g' src/zen.cpp

for f in COPYRIGHT AUTHORS docs/FAQ_it.txt docs/README_es.txt docs/README_it.txt
do
iconv -f iso8859-1 -t utf-8 $f > $f.conv && mv -f $f.conv $f
done

#Fix some bad ending lines
sed -i 's/\r$//' docs/*_it.txt

%build

aclocal
libtoolize -c
autoconf
autoheader
automake -a -c
%configure CXXFLAGS="-I%{_includedir}/tinyxpath \
-DWITHOUT_BINRELOC %{optflags}" LDFLAGS="-ltinyxml -ltinyxpath"
make %{?_smp_mflags}
%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
rm -rfv %{buildroot}%{_defaultdocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n opencity-data -f %{oreon_filedir}/opencity-data.list

%changelog

%autochangelog
