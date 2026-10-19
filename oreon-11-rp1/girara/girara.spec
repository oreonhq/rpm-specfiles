%global source0_hash d7255635776a45d42d1e555aa425ab96caf23755442474cf240cbac966d8502f
Name:               girara
Version:            2026.07.18
Release:        1%{?dist}
Summary:        Simple user interface library
License:            Zlib
URL:                https://pwmt.org/projects/%{name}/
Source0:        https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
%global girara_locales  lib%{name}-gtk3-4
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Girara is a library that implements a user interface that focuses on simplicity
and minimalism.

%package      devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson -Ddocs=disabled -Dtests=enabled
%meson_build
%install
%meson_install
%find_lang %{girara_locales}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n girara-devel -f %{oreon_filedir}/girara-devel.list

%changelog

%autochangelog
