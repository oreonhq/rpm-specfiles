%global source0_hash cc652d48e68b8b03afc5e9e08509676aee89f9d492b9a3897cd028bcc800ce31

Name:       ibus-libpinyin
Version:    1.16.5
Release:    4%{?dist}
Summary:    Intelligent Pinyin engine based on libpinyin for IBus
License:    GPL-3.0-or-later
URL:        https://github.com/libpinyin/ibus-libpinyin
Source0:        http://downloads.sourceforge.net/libpinyin/ibus-libpinyin/%{name}-%{version}.tar.gz

Requires:       python3-gobject
Requires:       ibus >= 1.5.11
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  lua-devel
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ibus-devel >= 1.5.11
BuildRequires:  libpinyin-devel >= 2.1.0
BuildRequires:  libnotify-devel
BuildRequires:  make

# Requires(post): sqlite

Requires:   libpinyin-data%{?_isa} >= 1.5.91

Obsoletes: ibus-pinyin < 1.4.0-17

%description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) 
input method based on libpinyin for IBus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure --disable-static \
           --with-python=python3 \
           --disable-boost

# make -C po update-gmo
%make_build

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-libpinyin.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-libbopomofo.desktop

%install
%make_install

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-libpinyin/setup

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/applications/ibus-setup-libpinyin.desktop
%{_datadir}/applications/ibus-setup-libbopomofo.desktop
%{_libexecdir}/ibus-engine-libpinyin
%{_libexecdir}/ibus-setup-libpinyin
%{_datadir}/ibus-libpinyin/icons
%{_datadir}/ibus-libpinyin/setup
%{_datadir}/ibus-libpinyin/base.lua
%{_datadir}/ibus-libpinyin/user.lua
%{_datadir}/ibus-libpinyin/network.txt
%{_datadir}/ibus-libpinyin/db/english.db
%{_datadir}/ibus-libpinyin/db/table.db
%dir %{_datadir}/ibus-libpinyin
%dir %{_datadir}/ibus-libpinyin/db
%{_datadir}/ibus/component/*
%{_datadir}/ibus-libpinyin/default.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.5-4
- Prepare for Oreon 11 (RP1)
