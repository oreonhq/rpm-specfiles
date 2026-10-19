%global source0_hash 50811e9e94fc798eb5dcbaff20f81067c942ec47f329f91bbe4caeb35a61ff05
Name:           libtsm
Version:        4.8.0
Release:        1%{?dist}
Summary:        DEC-VT terminal emulator state machine
License:        MIT AND LGPL-2.1-or-later
URL:            https://github.com/kmscon/libtsm
Source0:        https://github.com/kmscon/libtsm/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  xz
# /oreon:deps
%description
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators.

%package devel
Summary:        Development files for the DEC-VT terminal state machine library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libtsm-devel -f %{oreon_filedir}/libtsm-devel.list

%changelog

%autochangelog
