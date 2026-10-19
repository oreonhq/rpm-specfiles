%global source0_hash a5ff8a4352a547da6b01add3cf46c3d926afac1b455aa8effc08beba7c2da2c1
Name:           molsketch
Version:        0.8.4
Release:        2%{?dist}
Summary:        Molecular Structures Editor
License:        GPL-2.0-or-later
URL:            http://molsketch.sourceforge.net
Source0:        https://downloads.sourceforge.net/molsketch/Molsketch-%{version}-src.tar.gz
Requires:       hicolor-icon-theme
Requires:       openbabel%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  openbabel-devel
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Molsketch is a 2D molecular editing tool. Its goal is to help you draw
molecules quickly and easily. Of course your creation can be exported
afterwards in high quality, in a number of vector and bitmap formats.

%package doc
Summary:        Documentation files for %{name}
License:        GPL-2.0-or-later
BuildArch:      noarch
%description doc
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qttools-devel
%description 	devel
2D molecular structures editor.

This package contains header files and libraries needed to develop
applications that use %{name}.

# Regular builds:
#%%setup -q -n Molsketch-%%{version}
# Test buids:
#%%setup -q -n Molsketch-latest (or Molsketch-master)
# "-c" needed in v0.7.3 because of missing top-level dir
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Molsketch-%{version}

%build

%cmake -DMSK_PREFIX=%{_prefix} -DMSK_QT6=true
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n molsketch-doc -f %{oreon_filedir}/molsketch-doc.list
%files -n molsketch-devel -f %{oreon_filedir}/molsketch-devel.list

%changelog

%autochangelog
