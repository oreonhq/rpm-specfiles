%global source0_hash b6654928bd423f92e6da39eb1f40f10000ae2cc6247247fc1882dcff6acbdfc8
Name:           libsixel
Version:        1.10.5
Release:        1%{?dist}
Summary:        SIXEL encoding and decoding
License:        MIT
URL:            https://github.com/libsixel/libsixel
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          libsixel-fix-bash-completions.patch
Patch:          libsixel-fix-cve-2025-9300.patch
Patch:          libsixel-fix-cve-2025-61146.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
# /oreon:deps
%description
An encoder/decoder implementation for DEC SIXEL graphics.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package utils
Summary:        SIXEL encoder and decoder utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description utils
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dtests=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libsixel-devel -f %{oreon_filedir}/libsixel-devel.list
%files -n libsixel-utils -f %{oreon_filedir}/libsixel-utils.list

%changelog

%autochangelog
