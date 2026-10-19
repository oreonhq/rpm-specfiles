%global source0_hash 3e971567b72dae4b08b710fd1471bff34f58814df2aa74e97ed386590df3c5db
Name:       ibus-pinyin
Version:    1.5.1
Release:        1%{?dist}
Summary:        The Chinese Pinyin and Bopomofo engines for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus-pinyin
Source0:        https://github.com/ibus/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:   ibus >= 1.5.4
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  opencc-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pyzy-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --disable-static --enable-db-open-phrase \
           --enable-opencc \
           --disable-boost
make %{?_smp_mflags}
%install
make DESTDIR=${RPM_BUILD_ROOT} install
%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-pinyin/setup
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
