%global source0_hash d951a3115f686956f5c6b839b390ffb50bb443f7711fe35f57a07f4d0667277f
Name:           xnvme
Version:        0.7.5
Release:        1%{?dist}
Summary:        Unified API and tools for traditional and emerging I/O interfaces
License:        BSD-3-Clause
URL:            https://github.com/xnvme/xnvme
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1: 0001-remove-rpath.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  liburing-devel
BuildRequires:  meson
# /oreon:deps
%description
%{summary}.
Minimal-overhead libraries and tools for cross-platform storage I/O and
NVMe-native development. A unified API encapsulating traditional block-I/O via
psync, libaio, and io_uring as well as user-space NVMe drivers.

%package devel
Summary:        Development library and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This contains the headers and libraries for developing against %{name}.

%package static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%package tools
Summary:        Command-line tools for storage I/O and NVMe-native development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dforce_completions=true -Dwith-libvfn=disabled -Dwith-isal=disabled -Dwith-spdk=disabled -Dexamples=false -Dtests=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test --num-processes 1
%files -f %{oreon_filedir}/main.list
%files -n xnvme-devel -f %{oreon_filedir}/xnvme-devel.list
%files -n xnvme-static -f %{oreon_filedir}/xnvme-static.list
%files -n xnvme-tools -f %{oreon_filedir}/xnvme-tools.list

%changelog

%autochangelog
