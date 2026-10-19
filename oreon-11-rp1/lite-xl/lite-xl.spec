%global source0_hash fcaffb946bc60583369cb040d533a4ac18075a6d474d49a2a5ff4bf87e2e9a10
Name:    lite-xl
Version: 2.1.8
Release:        1%{?dist}
%forgemeta
Summary:        A lightweight text editor written in Lua, adapted from lite
License: MIT and OFL
URL:     https://lite-xl.com/
Source0:        https://github.com/lite-xl/lite-xl/archive/refs/tags/v%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  (pkgconfig(lua) >= 5.4 with pkgconfig(lua) < 5.5)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(sdl3)
# /oreon:deps
%description
A lightweight, simple, fast, feature-filled, and extremely
extensible text editor written in C, and Lua, adapted from lite.
Lite XL is derived from lite. It is a lightweight text editor
written mostly in Lua — it aims to provide something practical,
pretty, small and fast easy to modify and extend, or to use
without doing either.
The aim of Lite XL compared to lite is to be more user friendly, 
improve the quality of font rendering, and reduce CPU usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lite-xl-%{version}
%oreon_prep
%build

%meson -Darch_tuple=%{_arch}-linux -Duse_system_lua=true
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/org.lite_xl.lite_xl.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
