%global source0_hash 3309218c3137a70faada653690802b514e4e46d9b38e7d9d5948ffcc4831f3b1
Name:           libliftoff
Version:        0.5.0
Release:        1%{?dist}
Summary:        Lightweight KMS plane library
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff
Source0:        https://gitlab.freedesktop.org/emersion/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libdrm)
# /oreon:deps
%description
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libliftoff-devel -f %{oreon_filedir}/libliftoff-devel.list

%changelog

%autochangelog
