%global source0_hash 45aaf19f18774abcd7a18c2729538b63779b1a1883f1e636d364f87c2840a974

%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx.conf
%{!?gtk2_binary_version: %global gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%{!?gtk3_binary_version: %global gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}

Name:			fcitx
Summary:		An input method framework
Version:		4.2.9.9
Release:		11%{?dist}
License:		GPL-2.0-or-later
URL:			https://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz
Source1:		xinput-%{name}
Patch0: fcitx-exports-for-fbterm.patch
Patch1: fcitx-gcc13.patch
BuildRequires:		gcc-c++
BuildRequires:		pango-devel, dbus-devel, opencc-devel
BuildRequires:		wget, intltool, chrpath, sysconftool, opencc
BuildRequires:		cmake, libtool, doxygen, libicu-devel
BuildRequires:		qt4-devel, gtk3-devel, gtk2-devel, libicu
BuildRequires:		xorg-x11-proto-devel, xorg-x11-xtrans-devel
BuildRequires:		gobject-introspection-devel, libxkbfile-devel
BuildRequires:		enchant-devel, iso-codes-devel, libicu-devel
BuildRequires:		libX11-devel, dbus-glib-devel, dbus-x11
BuildRequires:		desktop-file-utils, libxml2-devel
BuildRequires:		lua-devel, extra-cmake-modules
BuildRequires:		xkeyboard-config-devel
BuildRequires:		libuuid-devel
BuildRequires:		json-c-devel
Requires:		%{name}-data = %{version}-%{release}
Requires:		imsettings
Requires(post):		%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
Requires:		%{name}-gtk3 = %{version}-%{release}
Requires:		%{name}-gtk2 = %{version}-%{release}

# conflict to fcitx5 due to a icon file conflict
Conflicts: fcitx5

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

%autosetup -p1

%build
%cmake -DENABLE_GTK3_IM_MODULE=On -DENABLE_QT_IM_MODULE=On -DENABLE_OPENCC=On -DENABLE_LUA=On -DENABLE_GIR=On -DENABLE_XDGAUTOSTART=Off
%cmake_build 

%install
%cmake_install 

find %{buildroot}%{_libdir} -name '*.la' -delete -print

install -pm 644 -D %{SOURCE1} %{buildroot}%{_xinputconf}

# patch fcitx4-config to use pkg-config to solve libdir to avoid multiarch
# confilict
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

%post 
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :

%postun  
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%ldconfig_scriptlets libs

%files -f %{name}.lang
%doc AUTHORS ChangeLog THANKS TODO
%license COPYING
%config %{_xinputconf}
%{_bindir}/fcitx-*
%{_bindir}/fcitx
%{_bindir}/createPYMB
%{_bindir}/mb2org
%{_bindir}/mb2txt
%{_bindir}/readPYBase
%{_bindir}/readPYMB
%{_bindir}/scel2org
%{_bindir}/txt2mb
%{_datadir}/applications/%{name}-skin-installer.desktop
%dir %{_datadir}/%{name}/dbus/
%{_datadir}/%{name}/dbus/daemon.conf
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-fskin.xml
%{_mandir}/man1/createPYMB.1*
%{_mandir}/man1/fcitx-remote.1*
%{_mandir}/man1/fcitx.1*
%{_mandir}/man1/mb2org.1*
%{_mandir}/man1/mb2txt.1*
%{_mandir}/man1/readPYBase.1*
%{_mandir}/man1/readPYMB.1*
%{_mandir}/man1/scel2org.1*
%{_mandir}/man1/txt2mb.1*

%files libs
%license COPYING
%{_libdir}/libfcitx*.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}-[!pqt]*.so
%{_libdir}/%{name}/%{name}-punc.so
%{_libdir}/%{name}/%{name}-quickphrase.so
%{_libdir}/%{name}/libexec/
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Fcitx-1.0.typelib

%files data
%license COPYING
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/24x24/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/skin/
%dir %{_datadir}/%{name}/addon
%{_datadir}/%{name}/addon/%{name}-[!pqt]*.conf
%{_datadir}/%{name}/addon/%{name}-punc.conf
%{_datadir}/%{name}/addon/%{name}-quickphrase.conf
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/spell/
%dir %{_datadir}/%{name}/imicon/
%dir %{_datadir}/%{name}/inputmethod/
%dir %{_datadir}/%{name}/configdesc/
%dir %{_datadir}/%{name}/table/
%{_datadir}/%{name}/configdesc/[!ft]*.desc
%{_datadir}/%{name}/configdesc/fcitx-[!p]*.desc
%{_datadir}/dbus-1/services/org.fcitx.Fcitx.service

%files devel
%license COPYING
%{_bindir}/fcitx4-config
%{_libdir}/libfcitx*.so
%{_libdir}/pkgconfig/fcitx*.pc
%{_includedir}/fcitx*
%{_datadir}/cmake/%{name}/
%{_docdir}/%{name}/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Fcitx-1.0.gir

%files table-chinese
%doc
%{_datadir}/%{name}/table/*
%{_datadir}/%{name}/imicon/[!ps]*.png

%files pinyin
%doc
%{_datadir}/%{name}/inputmethod/pinyin.conf
%{_datadir}/%{name}/inputmethod/shuangpin.conf
%{_datadir}/%{name}/pinyin/
%{_datadir}/%{name}/configdesc/fcitx-pinyin.desc
%{_datadir}/%{name}/configdesc/fcitx-pinyin-enhance.desc
%{_datadir}/%{name}/addon/fcitx-pinyin.conf
%{_datadir}/%{name}/addon/fcitx-pinyin-enhance.conf
%{_datadir}/%{name}/imicon/pinyin.png
%{_datadir}/%{name}/imicon/shuangpin.png
%{_libdir}/%{name}/%{name}-pinyin.so
%{_libdir}/%{name}/%{name}-pinyin-enhance.so
%{_datadir}/%{name}/py-enhance/

%files qw
%doc
%{_datadir}/%{name}/inputmethod/qw.conf
%{_libdir}/%{name}/%{name}-qw.so
%{_datadir}/%{name}/addon/fcitx-qw.conf

%files table
%doc
%{_datadir}/%{name}/configdesc/table.desc
%{_libdir}/%{name}/%{name}-table.so
%{_datadir}/%{name}/addon/fcitx-table.conf

%files gtk2
%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/im-fcitx.so

%files gtk3
%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/im-fcitx.so

%files qt4
%{_libdir}/qt4/plugins/inputmethods/qtim-fcitx.so

%changelog
%autochangelog
