%global source0_hash 2f5298be5b4ba840a04f360c163849b34a31386ccd287657885e21268665f413
%global commit f341f5f237737594c1b024338f0a2fc04fabdff3
Name:           osmctools
Version:        0.9
Release:        1%{?dist}
Summary:        Tools to manipulate OpenStreetMap files
License:        AGPL-3.0-only AND GPL-2.0-or-later
URL:            https://gitlab.com/osm-c-tools/osmctools
Source0:        https://gitlab.com/osm-c-tools/osmctools/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        osmconvert.1
Source2:        osmfilter.1
Source3:        osmupdate.1
Patch0:         %{name}-0.9-gcc15.patch
Requires:       wget
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Small collection of basic OpenStreetMap tools, include converter, filter and
updater files.

Programs include:
* osmconvert - Converter of OSM files
* osmfilter - The experimental OSM filters data
* osmupdate - Update OSM files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -fvi
%configure
%make_build
%install
%make_install
install -d %{buildroot}%{_mandir}/man1/
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
  install -p -m 0644 ${i} %{buildroot}%{_mandir}/man1/
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
