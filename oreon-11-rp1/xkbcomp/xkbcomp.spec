%global source0_hash 2ac31f26600776db6d9cd79b3fcd272263faebac7eb85fb2f33c7141b8486060
Name:       xkbcomp
Version:    1.5.0
Release:        2%{?dist}
Summary:        XKB keymap compiler
License:    MIT-open-group AND HPND-DEC
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.xz
Obsoletes:  xorg-x11-xkb-utils < 7.8
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxkbfile-devel
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
X.Org XKB keymap compiler

%package devel
Summary:    XKB keymap compiler development package
Requires:   pkgconfig
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
X.Org XKB keymap compiler development files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xkbcomp-devel -f %{oreon_filedir}/xkbcomp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-2
- Prepare for Oreon 11 (RP1)
