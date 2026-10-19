%global source0_hash c21a3e1d7a8d9e6357f5ed0e3246111868b3fda04fcbb8cc726dab2d6363f265
Name:       ibus-libzhuyin
Version:    1.10.4
Release:        1%{?dist}
Summary:        New Zhuyin engine based on libzhuyin for IBus
License:    GPL-2.0-or-later
URL:        https://github.com/libzhuyin/ibus-libzhuyin
Source0:        https://downloads.sourceforge.net/libzhuyin/ibus-libzhuyin/%{name}-%{version}.tar.gz
Requires:   ibus >= 1.3.0
Provides:   libzhuyin-data = 1.1.2
Obsoletes:  libzhuyin-data < 1.1.2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libpinyin-devel
BuildRequires:  libpinyin-tools
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
It includes a Chinese Zhuyin (Bopomofo) input method
based on libzhuyin for IBus.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static \
           --disable-boost \
           --with-python=python3
%make_build
%install
%make_install
%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-libzhuyin/setup
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.4-2
- Prepare for Oreon 11 (RP1)
