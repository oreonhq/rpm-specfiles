%global source0_hash 0b06d1434a750b5e4981be9696a9f65bfd7b38fe2d8d24199d92f11394bb8459

Name:           libtsm
Version:        4.5.0
Release:        1%{?dist}
Summary:        DEC-VT terminal emulator state machine
License:        MIT AND LGPL-2.1-or-later
URL:            https://github.com/kmscon/libtsm
Source0:        https://github.com/kmscon/libtsm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(check)

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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING LICENSE_htable
%{_libdir}/libtsm.so.4{,.*}

%files devel
%doc README.md
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/*.pc
