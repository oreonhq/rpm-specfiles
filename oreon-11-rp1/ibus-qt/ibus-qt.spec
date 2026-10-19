%global source0_hash 1e7b0ccb88bc36c702545176f0870e6760685e8cd97d9cd7938084f5cedb2ff1
Name:       ibus-qt
Version:    1.3.4
Release:        1%{?dist}
Summary:        Qt IBus library and Qt input method plugin
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus/wiki
Source0:        https://github.com/ibus/ibus-qt/releases/download/%{version}/%{name}-%{version}-Source.tar.gz
Patch0:     %{name}-HEAD.patch
Requires:       ibus
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ibus-devel
BuildRequires:  libicu-devel
BuildRequires:  qt4-devel
# /oreon:deps
%description
Qt IBus library and Qt input method plugin.

%package devel
Summary:    Development tools for ibus qt
Requires:   %{name} = %{version}-%{release}
%description devel
The ibus-qt-devel package contains the header files for ibus qt library.

%package docs
Summary:    Development documents for ibus qt
Requires:   %{name} = %{version}-%{release}
%description docs
The ibus-qt-docs package contains developer documentation for ibus qt library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}-Source
%oreon_prep
%build

%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_usr} \
    -DLIBDIR=%{_libdir}
%cmake_build
%cmake_build -- docs
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ibus-qt-devel -f %{oreon_filedir}/ibus-qt-devel.list
%files -n ibus-qt-docs -f %{oreon_filedir}/ibus-qt-docs.list

%changelog

%autochangelog
