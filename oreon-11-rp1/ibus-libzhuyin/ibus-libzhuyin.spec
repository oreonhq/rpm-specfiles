Name:       ibus-libzhuyin
Version:    1.10.4
Release:    2%{?dist}
Summary:    New Zhuyin engine based on libzhuyin for IBus
License:    GPL-2.0-or-later
URL:        https://github.com/libzhuyin/ibus-libzhuyin
Source0:    http://downloads.sourceforge.net/libzhuyin/ibus-libzhuyin/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 c21a3e1d7a8d9e6357f5ed0e3246111868b3fda04fcbb8cc726dab2d6363f265
%global source0_file ibus-libzhuyin-1.10.4.tar.gz
# oreon url source checksums end

BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  ibus-devel >= 1.3
BuildRequires:  libpinyin-devel >= 2.0.91
BuildRequires:  python3-devel
BuildRequires:  libpinyin-tools
BuildRequires:  make

# Requires(post): sqlite

Requires:   ibus >= 1.3.0
Provides:   libzhuyin-data = 1.1.2
Obsoletes:  libzhuyin-data < 1.1.2

%description
It includes a Chinese Zhuyin (Bopomofo) input method
based on libzhuyin for IBus.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ibus-libzhuyin-1.10.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c21a3e1d7a8d9e6357f5ed0e3246111868b3fda04fcbb8cc726dab2d6363f265" || { echo "oreon: Source0 SHA256 mismatch for ibus-libzhuyin-1.10.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static \
           --disable-boost \
           --with-python=python3

# make -C po update-gmo
%make_build

%install
%make_install

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-libzhuyin/setup

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog INSTALL NEWS
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/applications/ibus-setup-libzhuyin.desktop
%{_libexecdir}/ibus-engine-libzhuyin
%{_libexecdir}/ibus-setup-libzhuyin
%{_datadir}/ibus-libzhuyin/setup
%dir %{_datadir}/ibus-libzhuyin
%{_datadir}/ibus/component/*
%{_datadir}/ibus-libzhuyin/icons
%{_datadir}/ibus-libzhuyin/*symbol.txt
%{_libdir}/ibus-libzhuyin/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.4-2
- Prepare for Oreon 11 (RP1)
