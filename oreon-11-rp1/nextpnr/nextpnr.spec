%global source0_hash 089f15e51ccb6c64445945cfb366af6c031dfe983434adfed40f26c8d97bc272

%global commit 8c40db213a99b68ffb1d48628fb68eb040b8dab0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global snapdate 20260304

Name:		nextpnr
Version:	1
Release:	64.%{snapdate}git%{shortcommit}%{?dist}
Summary:	FPGA place and route tool

# Automatically converted from old format: ISC and BSD and MIT and (MIT or Public Domain) - review is highly recommended.
License:	ISC AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND (LicenseRef-Callaway-MIT OR LicenseRef-Callaway-Public-Domain)
URL:		https://github.com/YosysHQ/nextpnr
Source0:	https://github.com/YosysHQ/nextpnr/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	libglvnd-devel
BuildRequires:	boost-filesystem
BuildRequires:	boost-thread
BuildRequires:	boost-program-options
BuildRequires:	boost-iostreams
BuildRequires:	qt5-qtconfiguration-devel
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	boost-python3-devel
BuildRequires:	eigen3-devel
BuildRequires:	pybind11-devel
# NOTE: remember to update icestorm & trellis before rebuilding nextpnr!!!
BuildRequires:	icestorm >= 0-0.40
BuildRequires:	trellis-devel >= 1.2.1-35

# License: ISC
Provides:	bundled(qtimgui)

# Qt5 enabled fork of QtPropertyBrowser
# License: BSD
Provides:	bundled(QtPropertyBrowser)

# License: MIT
Provides:	bundled(python-console)

# License: (MIT or Public Domain)
Provides:	bundled(imgui) = 1.66-wip

%description
nextpnr aims to be a vendor neutral, timing driven, FOSS FPGA place and
route tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
cp 3rdparty/imgui/LICENSE.txt LICENSE-imgui.txt
cp 3rdparty/qtimgui/LICENSE LICENSE-qtimgui.txt
cp 3rdparty/python-console/LICENSE LICENSE-python-console.txt

%build
%cmake  -DARCH=all \
	-DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
	-DICEBOX_DATADIR=%{_datadir}/icestorm \
	-DTRELLIS_LIBDIR=%{_libdir}/trellis \
	-DBUILD_GUI=ON \
	-DUSE_OPENMP=ON
%cmake_build
# prepare examples doc. directory:
mkdir -p examples/ice40
cp -r ice40/examples/* examples/ice40

%install
%cmake_install

%files
%{_bindir}/nextpnr-generic
%{_bindir}/nextpnr-ice40
%{_bindir}/nextpnr-ecp5
%doc README.md docs examples
%license COPYING
%license LICENSE-imgui.txt
%license LICENSE-qtimgui.txt
%license LICENSE-python-console.txt

%changelog
%autochangelog
