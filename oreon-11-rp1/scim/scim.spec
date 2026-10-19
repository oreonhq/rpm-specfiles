%global source0_hash 072d79dc3c7277b8e8fcb1caf1a83225c3bf113d590f314b85ae38024427a228
Name:      scim
Version:   1.4.18
Release:        1%{?dist}
Summary:        Smart Common Input Method platform
License:   LGPL-2.1-or-later
URL:       https://github.com/scim-im/scim/
Source0:        https://github.com/scim-im/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:   xinput-scim
Source2:   scim-icons-0.7.tar.gz
Source3:   scim-system-config
Source4:   scim-system-global
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
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  qt-devel
BuildRequires:  qt3-devel
# /oreon:deps
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
Requires: gtk2 >= 2.11.6-7.fc8
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
find ${RPM_BUILD_ROOT} -name '*.la' | xargs rm
rm ${RPM_BUILD_ROOT}/%{_datadir}/applications/scim-setup.desktop
rm ${RPM_BUILD_ROOT}/%{_datadir}/control-center-2.0/capplets/scim-setup.desktop
rm -f docs/html/FreeSans.ttf
mkdir -pm 755 ${RPM_BUILD_ROOT}/%{_sysconfdir}/X11/xinit/xinput.d
install -pm 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_xinputconf}
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%define cjk_langs ja_JP ko_KR zh_CN zh_HK zh_TW
%define indic_langs as_IN bn_IN gu_IN hi_IN kn_IN ml_IN or_IN pa_IN ta_IN te_IN
%define supported_langs %{cjk_langs} %{indic_langs} ne_NE si_LK th_TH vi_VN
for llcc in %{supported_langs}; do
   %{_sbindir}/alternatives --remove xinput-$llcc %{_sysconfdir}/X11/xinit/xinput.d/scim &>/dev/null || :
   [ -L %{_sysconfdir}/alternatives/xinput-$llcc -a "`readlink %{_sysconfdir}/alternatives/xinput-$llcc`" = "%{_sysconfdir}/X11/xinit/xinput.d/scim" ] && %{_sbindir}/alternatives --auto xinput-$llcc &>/dev/null || :
done
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 82 || :
%post gtk

%{_bindir}/update-gtk-immodules %{_host} || :
%ldconfig_scriptlets libs
%postun

if [ "$1" = "0" ]; then
   %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
   [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi
%postun gtk

%{_bindir}/update-gtk-immodules %{_host} || :
%files -f %{oreon_filedir}/main.list
%files -n scim-devel -f %{oreon_filedir}/scim-devel.list
%files -n scim-gtk -f %{oreon_filedir}/scim-gtk.list
%files -n scim-qt -f %{oreon_filedir}/scim-qt.list
%files -n scim-libs -f %{oreon_filedir}/scim-libs.list
%files -n scim-rawcode -f %{oreon_filedir}/scim-rawcode.list

%changelog

%autochangelog
