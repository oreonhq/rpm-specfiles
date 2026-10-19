%global source0_hash 69fc067bea968ce7c2861aa64426d8d3a3c26bfb302a3b0c315b797fc7c60065
Name:          libtypec
Version:       0.6.1
Release:        1%{?dist}
Summary:        A generic user space library for USB-C port management
License:       MIT and GPL-2.0-only
URL:           https://github.com/libtypec/libtypec
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  meson
BuildRequires:  systemd-devel
# /oreon:deps
%description
“libtypec” is aimed to provide a generic interface abstracting all
platform complexity for user space to develop tools for efficient
USB-C port management. The library can also enable development of
diagnostic and debug tools to debug system issues around USB-C/USB
PD topology.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package utils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities for USB Type-C.

%package guiutils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description guiutils
Utilities for USB Type-C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%meson -Dutils=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libtypec-devel -f %{oreon_filedir}/libtypec-devel.list
%files -n libtypec-utils -f %{oreon_filedir}/libtypec-utils.list
%files -n libtypec-guiutils -f %{oreon_filedir}/libtypec-guiutils.list

%changelog

%autochangelog
