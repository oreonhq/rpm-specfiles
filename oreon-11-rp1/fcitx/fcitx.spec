%global source0_hash 45aaf19f18774abcd7a18c2729538b63779b1a1883f1e636d364f87c2840a974
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx.conf
%{!?gtk2_binary_version: %global gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%{!?gtk3_binary_version: %global gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}
Name:			fcitx
Summary:        An input method framework
Version:		4.2.9.9
Release:        1%{?dist}
License:		GPL-2.0-or-later
URL:			https://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz
Source1:		xinput-%{name}
Patch0: fcitx-exports-for-fbterm.patch
Patch1: fcitx-gcc13.patch
Requires:		%{name}-data = %{version}-%{release}
Requires:		imsettings
Requires(post):		%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		%{name}-gtk3 = %{version}-%{release}
Requires:		%{name}-gtk2 = %{version}-%{release}
Conflicts: fcitx5
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  json-c-devel
BuildRequires:  libX11-devel
BuildRequires:  libicu
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  opencc
BuildRequires:  opencc-devel
BuildRequires:  pango-devel
BuildRequires:  qt4-devel
BuildRequires:  sysconftool
BuildRequires:  wget
BuildRequires:  xkeyboard-config-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
Fcitx is an input method framework with extension support. Currently it
supports Linux and Unix systems like FreeBSD.

Fcitx tries to provide a native feeling under all desktop as well as a light
weight core. You can easily customize it to fit your requirements.

%package data
Summary:		Data files of Fcitx
BuildArch:		noarch
Requires:		hicolor-icon-theme
Requires:		dbus
%description data
The %{name}-data package provides shared data for Fcitx.

%package libs
Summary:		Shared libraries for Fcitx
Provides:		%{name}-keyboard = %{version}-%{release}
Obsoletes:		%{name}-keyboard =< 4.2.3
%description libs
The %{name}-libs package provides shared libraries for Fcitx

%package devel
Summary:		Development files for Fcitx
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		libX11-devel%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx libraries.

%package table-chinese
Summary:		Chinese table of Fcitx
BuildArch:		noarch
Requires:		%{name}-table = %{version}-%{release}
%description table-chinese
The %{name}-table-chinese package provides other Chinese table for Fcitx.

%package gtk2
Summary:		Fcitx IM module for gtk2
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
%description gtk2
This package contains Fcitx IM module for gtk2.

%package gtk3
Summary:		Fcitx IM module for gtk3
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		imsettings-gnome
%description gtk3
This package contains Fcitx IM module for gtk3.

%package qt4
Summary:		Fcitx IM module for qt4
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
%description qt4
This package contains Fcitx IM module for qt4.

%package pinyin
Summary:		Pinyin Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Built-in_Pinyin
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}
%description pinyin
This package contains pinyin engine for Fcitx.

%package qw
Summary:		Quwei Engine for Fcitx
URL:			https://fcitx-im.org/wiki/QuWei
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}
%description qw
This package contains Quwei engine for Fcitx.

%package table
Summary:		Table Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Table
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}
Requires:		%{name}-pinyin = %{version}-%{release}
%description table
This package contains table engine for Fcitx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DENABLE_GTK3_IM_MODULE=On -DENABLE_QT_IM_MODULE=On -DENABLE_OPENCC=On -DENABLE_LUA=On -DENABLE_GIR=On -DENABLE_XDGAUTOSTART=Off
%cmake_build 
%install
%cmake_install 
find %{buildroot}%{_libdir} -name '*.la' -delete -print
install -pm 644 -D %{SOURCE1} %{buildroot}%{_xinputconf}
sed -i -e 's:%{_libdir}:`pkg-config --variable=libdir fcitx`:g' \
  %{buildroot}%{_bindir}/fcitx4-config
chmod +x %{buildroot}%{_datadir}/%{name}/data/env_setup.sh
%find_lang %{name}
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-skin-installer.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post 

%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :
%postun  

if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n fcitx-data -f %{oreon_filedir}/fcitx-data.list
%files -n fcitx-libs -f %{oreon_filedir}/fcitx-libs.list
%files -n fcitx-devel -f %{oreon_filedir}/fcitx-devel.list
%files -n fcitx-table-chinese -f %{oreon_filedir}/fcitx-table-chinese.list
%files -n fcitx-gtk2 -f %{oreon_filedir}/fcitx-gtk2.list
%files -n fcitx-gtk3 -f %{oreon_filedir}/fcitx-gtk3.list
%files -n fcitx-qt4 -f %{oreon_filedir}/fcitx-qt4.list
%files -n fcitx-pinyin -f %{oreon_filedir}/fcitx-pinyin.list
%files -n fcitx-qw -f %{oreon_filedir}/fcitx-qw.list
%files -n fcitx-table -f %{oreon_filedir}/fcitx-table.list

%changelog

%autochangelog
