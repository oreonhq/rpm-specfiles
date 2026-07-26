%global source0_hash 3e971567b72dae4b08b710fd1471bff34f58814df2aa74e97ed386590df3c5db

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3

Name:       ibus-pinyin
Version:    1.5.1
Release:    7%{?dist}
Summary:    The Chinese Pinyin and Bopomofo engines for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus-pinyin
Source0:    https://github.com/ibus/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  ibus-devel >= 1.5.4
BuildRequires:  lua-devel >= 5.1
BuildRequires:  opencc-devel
BuildRequires:  pyzy-devel
BuildRequires:  python3-devel
BuildRequires: make

# Requires(post): sqlite

Requires:   ibus >= 1.5.4

%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure --disable-static --enable-db-open-phrase \
           --enable-opencc \
           --disable-boost

# make -C po update-gmo
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-pinyin/setup

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-pinyin
%{_libexecdir}/ibus-setup-pinyin
%{_datadir}/ibus-pinyin/phrases.txt
%{_datadir}/ibus-pinyin/icons
%{_datadir}/ibus-pinyin/setup
%{_datadir}/applications/ibus-setup-bopomofo.desktop
%{_datadir}/applications/ibus-setup-pinyin.desktop
%dir %{_datadir}/ibus-pinyin
%dir %{_datadir}/ibus-pinyin/db
%{_datadir}/ibus/component/*
%{_datadir}/ibus-pinyin/base.lua
%{_datadir}/ibus-pinyin/db/english.db

%changelog
%autochangelog
