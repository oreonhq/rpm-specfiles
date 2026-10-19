%global source0_hash 209b41d38ee228760ebe50fce0ecaab42aabbdd22872e0437c32799736eab2b2
Name:		qdmr
Version:	0.15.1
Release:        1%{?dist}
Summary:        A GUI application for configuring and programming DMR radios
License:	GPL-3.0-or-later
URL:		https://dm3mat.darc.de/qdmr/
Source0:        https://github.com/hmatuschek/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:	dot_autodetect.png
Requires:	hicolor-icon-theme
Requires:	systemd-udev
Patch:		qdmr-0.13.2-fix-docbook-xsl-path.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook5-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  libusbx-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  systemd-rpm-macros
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
A Qt5 application to program DMR radios. DMR is a digital modulation
standard used in amateur and commercial radio. To this end, qdmr is an
alternative codeplug programming software (CPS) that supports several radios
across several manufacturers.

%package -n libdmrconf
Summary:	Library for configuring DMR radios
%description -n libdmrconf
This library is built from the qdmr SRPM.

%package -n libdmrconf-doc
Summary:	Documentation for libdmrconf
Requires:	libdmrconf = %{version}-%{release}
BuildArch:	noarch
%description -n libdmrconf-doc
Documentation for libdmrconf.

%package devel
Summary:	Development files for dmrconf
Requires:	libdmrconf%{?_isa} = %{version}-%{release}
%description devel
Libraries and header files for developing applications using libdmrconf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DBUILD_MAN=ON \
  -DBUILD_DOCS=ON \
  -DBUILD_TESTS=ON \
  -DINSTALL_APPSTREAM_DATA=ON \
  -DINSTALL_UDEV_RULES=ON \
  -DINSTALL_UDEV_PATH=%{_udevrulesdir} \
  -DDOCBOOK2MAN_XSLT=docbook_man.fedora.xsl
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_docdir}/qdmr/libdmrconf %{buildroot}%{_docdir}
mv %{SOURCE1} %{buildroot}%{_docdir}/libdmrconf/html/dot_autodetect.png
%oreon_autofiles libdmrconf usr/*/lib*.so.*
%oreon_autofiles libdmrconf-doc usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n libdmrconf -f %{oreon_filedir}/libdmrconf.list
%files -n libdmrconf-doc -f %{oreon_filedir}/libdmrconf-doc.list
%files -n qdmr-devel -f %{oreon_filedir}/qdmr-devel.list

%changelog

%autochangelog
