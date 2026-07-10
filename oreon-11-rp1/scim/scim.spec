%global source0_hash 072d79dc3c7277b8e8fcb1caf1a83225c3bf113d590f314b85ae38024427a228

Name:      scim
Version:   1.4.18
Release:   14%{?dist}
Summary:   Smart Common Input Method platform

License:   LGPL-2.1-or-later
URL:       https://github.com/scim-im/scim/
Source0:   https://github.com/scim-im/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:   xinput-scim
Source2:   scim-icons-0.7.tar.gz
Source3:   scim-system-config
Source4:   scim-system-global

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: gtk2-devel, libXt-devel, gtk3-devel
BuildRequires: qt-devel, qt3-devel
# for autoreconf
Buildrequires: autoconf automake gettext libtool intltool
# for system ltdl
Buildrequires: libtool-ltdl-devel
# for autogen.sh
Buildrequires: gnome-common
Requires:  %{name}-libs = %{version}-%{release}
Requires:  imsettings, im-chooser
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
Obsoletes: iiimf-gtk <= 1:12.2, iiimf-gnome-im-switcher <= 1:12.2, iiimf-server <= 1:12.2, iiimf-x <= 1:12.2
Obsoletes:  iiimf-libs-devel <= 1:12.2
Obsoletes:  iiimf-docs <= 1:12.2
Obsoletes:  iiimf-libs <= 1:12.2, iiimf-csconv <= 1:12.2
Obsoletes:  scim-lang-assamese
Obsoletes:  scim-lang-bengali
Obsoletes:  scim-lang-chinese
Obsoletes:  scim-lang-dhivehi
Obsoletes:  scim-lang-farsi
Obsoletes:  scim-lang-gujarati
Obsoletes:  scim-lang-hindi
Obsoletes:  scim-lang-japanese
Obsoletes:  scim-lang-kannada
Obsoletes:  scim-lang-korean
Obsoletes:  scim-lang-latin
Obsoletes:  scim-lang-malayalam
Obsoletes:  scim-lang-marathi
Obsoletes:  scim-lang-nepali
Obsoletes:  scim-lang-oriya
Obsoletes:  scim-lang-punjabi
Obsoletes:  scim-lang-sinhalese
Obsoletes:  scim-lang-tamil
Obsoletes:  scim-lang-telugu
Obsoletes:  scim-lang-thai
Obsoletes:  scim-lang-tibetan
Obsoletes:  scim-python
Obsoletes:  scim-python-chinese
Obsoletes:  scim-python-english
Obsoletes:  scim-python-pinyin
Obsoletes:  scim-python-xingma
Obsoletes:  scim-python-xingma-cangjie
Obsoletes:  scim-python-xingma-erbi
Obsoletes:  scim-python-xingma-wubi
Obsoletes:  scim-python-xingma-zhengma
Obsoletes:  scim-bridge-qtimm < 0.4.2
Obsoletes:  scim-bridge-qt4 < 0.4.15-3
Provides:   scim-bridge = 0.4.17
Obsoletes:  scim-bridge < 0.4.17
Patch7:     scim_panel_gtk-emacs-cc-style.patch
Patch9:     scim-fixes-compile.patch

%description
SCIM is a user friendly and full featured input method user interface and
also a development platform to make life easier for Input Method developers.


%package devel
Summary:    Smart Common Input Method platform
Requires:   %{name}-libs = %{version}-%{release}
Requires:   gtk2-devel
Requires:   pkgconfig
Obsoletes:  iiimf-libs-devel <= 1:12.2

%description devel
The scim-devel package includes the header files for the scim package.
Install scim-devel if you want to develop programs which will use scim.


%package gtk
Summary:    Smart Common Input Method Gtk IM module
# for %{_libdir}/gtk-2.0/immodules
Requires: gtk2 >= 2.11.6-7.fc8
# for update-gtk-immodules
Requires(post): gtk2 >= 2.9.1-2
Requires(postun): gtk2 >= 2.9.1-2
Provides:   scim-bridge-gtk = 0.4.17
Obsoletes:  scim-bridge-gtk < 0.4.17

%description gtk
This package provides a GTK input method module for SCIM.


%package qt
Summary:    Smart Common Input Method Qt IM module
Provides:   scim-qtimm
Obsoletes:  scim-qtimm
Provides:   scim-bridge-qt = 0.4.17
Obsoletes:  scim-bridge-qt < 0.4.17
Provides:   scim-bridge-qt3 = 0.4.17
Obsoletes:  scim-bridge-qt3 < 0.4.17

%description qt
This package provides a Qt input method module for SCIM.


%package libs
Summary:    Smart Common Input Method libraries
Obsoletes:  iiimf-libs <= 1:12.2, iiimf-csconv <= 1:12.2

%description libs
This package provides the libraries for SCIM.


%package rawcode
Summary:    SCIM Unicode Input Method Engine
Requires:   %{name} = %{version}-%{release}

%description rawcode
This package provides an Input Method Engine for inputting unicode characters
but their unicode codepoints.


%define scim_api 1.4.0

%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/scim.conf


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -a2 -p1

cp -p scim-icons/icons/*.png data/icons
cp -p scim-icons/pixmaps/*.png data/pixmaps

# use our system config & global file
mv configs/config{,.orig} 
cp -p %{SOURCE3} configs/config
mv configs/global{,.orig} 
cp -p %{SOURCE4} configs/global

./bootstrap


%build
%configure --disable-static --enable-ld-version-script --with-gtk-version=2
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="%{__install} -p"

# remove .la files
find ${RPM_BUILD_ROOT} -name '*.la' | xargs rm

# remove scim-setup.desktop file since it is confusing with im-chooser
rm ${RPM_BUILD_ROOT}/%{_datadir}/applications/scim-setup.desktop
# remove capplet
rm ${RPM_BUILD_ROOT}/%{_datadir}/control-center-2.0/capplets/scim-setup.desktop

# don't need this
rm -f docs/html/FreeSans.ttf

# install xinput config file
mkdir -pm 755 ${RPM_BUILD_ROOT}/%{_sysconfdir}/X11/xinit/xinput.d
install -pm 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_xinputconf}

%find_lang %{name}



%post
# remove old xinput.d alternatives
%define cjk_langs ja_JP ko_KR zh_CN zh_HK zh_TW
%define indic_langs as_IN bn_IN gu_IN hi_IN kn_IN ml_IN or_IN pa_IN ta_IN te_IN
%define supported_langs %{cjk_langs} %{indic_langs} ne_NE si_LK th_TH vi_VN
for llcc in %{supported_langs}; do
   %{_sbindir}/alternatives --remove xinput-$llcc %{_sysconfdir}/X11/xinit/xinput.d/scim &>/dev/null || :
   # if alternative was set to manual scim, reset to auto
   [ -L %{_sysconfdir}/alternatives/xinput-$llcc -a "`readlink %{_sysconfdir}/alternatives/xinput-$llcc`" = "%{_sysconfdir}/X11/xinit/xinput.d/scim" ] && %{_sbindir}/alternatives --auto xinput-$llcc &>/dev/null || :
done

# xinputrc alternative
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 82 || :


%post gtk
%{_bindir}/update-gtk-immodules %{_host} || :


%ldconfig_scriptlets libs


%postun
if [ "$1" = "0" ]; then
   %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
   # if alternative was set to manual scim, reset to auto
   [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi


%postun gtk
%{_bindir}/update-gtk-immodules %{_host} || :


%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog TODO
%dir %{_sysconfdir}/scim
%config(noreplace) %{_sysconfdir}/scim/*
%{_bindir}/*
%dir %{_libdir}/scim-1.0
%{_libdir}/scim-1.0/scim-helper-launcher
%{_libdir}/scim-1.0/scim-helper-manager
%{_libdir}/scim-1.0/scim-launcher
%{_libdir}/scim-1.0/scim-panel-gtk
%dir %{_libdir}/scim-1.0/%{scim_api}
%{_libdir}/scim-1.0/%{scim_api}/Filter
%{_libdir}/scim-1.0/%{scim_api}/FrontEnd
%{_libdir}/scim-1.0/%{scim_api}/Helper
%dir %{_libdir}/scim-1.0/%{scim_api}/IMEngine
%{_libdir}/scim-1.0/%{scim_api}/SetupUI
%{_datadir}/scim
%{_datadir}/pixmaps/*
%config(noreplace) %{_xinputconf}

%files devel
%doc docs/developers
%{_includedir}/scim-1.0
%{_libdir}/libscim*.so
%{_libdir}/pkgconfig/*.pc

%files gtk
%{_libdir}/gtk-2.0/*/immodules/im-scim.so
%{_libdir}/gtk-3.0/*/immodules/im-scim.so

%files qt
%{_libdir}/qt4/plugins/inputmethods/*.so
%{_libdir}/qt-3.3/lib/qt3/plugins/inputmethods/*.so


%files libs
%{_libdir}/libscim-*.so.*
%dir %{_libdir}/scim-1.0
%dir %{_libdir}/scim-1.0/%{scim_api}
%{_libdir}/scim-1.0/%{scim_api}/Config
%dir %{_libdir}/scim-1.0/%{scim_api}/IMEngine
%{_libdir}/scim-1.0/%{scim_api}/IMEngine/socket.so


%files rawcode
%{_libdir}/scim-1.0/%{scim_api}/IMEngine/rawcode.so


%changelog
%autochangelog
