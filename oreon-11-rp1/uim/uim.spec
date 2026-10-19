%global source0_hash 67f0e5fa4292a533edc6f98b842df60c531a89cf82d0336a4e1ab72202ab8c83
%global inst_xinput %{_sbindir}/update-alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf 50
%global uninst_xinput %{_sbindir}/update-alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf
%global srcver	1.9.6
%bcond_with	canna
Name:		uim
Version:	1.9.6
Release:        1%{?dist}
License:	BSD-3-Clause AND LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.1-or-later)
URL:		https://github.com/uim/uim/
%if %{with canna}
%endif
Source0:        https://github.com/uim/uim/releases/download/%{version}/uim-%{version}.tar.bz2
Source1:	xinput.d-uim
Source2:	uim-init.el
Patch1:		uim-emacs-utf8.patch
Summary:        A multilingual input method library
Requires(post): %{_sbindir}/update-alternatives /sbin/ldconfig
Requires(postun): %{_sbindir}/update-alternatives /sbin/ldconfig
Requires:	imsettings im-chooser
Requires:	emacs-filesystem >= %{_emacs_version}
Provides:	emacs-common-%{name} <= 1.8.6-7
Obsoletes:	emacs-common-%{name} <= 1.8.6-7
Provides:	emacs-%{name} <= 1.8.6-7, emacs-%{name}-el <= 1.8.6-7
Obsoletes:	emacs-%{name} <= 1.8.6-7, emacs-%{name}-el <= 1.8.6-7
Provides:	xemacs-%{name} <= 1.8.6-7, xemacs-%{name}-el <= 1.8.6-7
Obsoletes:	xemacs-%{name} <= 1.8.6-7, xemacs-%{name}-el <= 1.8.6-7
%if %{without canna}
Obsoletes:	%{name}-canna < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  anthy-unicode-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  eb-devel
BuildRequires:  emacs
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  libgcroots-devel
BuildRequires:  libtool
BuildRequires:  m17n-db
BuildRequires:  m17n-db-devel
BuildRequires:  m17n-db-extras
BuildRequires:  m17n-lib-devel
BuildRequires:  ncurses-devel
BuildRequires:  qt-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%package	devel
Summary:	Development files for the Uim library
Requires:	uim = %{version}-%{release}
%package	gtk3
Summary:	GTK+3 support for Uim
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3
Requires(postun): gtk3
Obsoletes:	%{name}-gnome < 1.8.5-4
Obsoletes:	%{name}-gtk2 < 1.9.5-1
%package	qt
Summary:	Qt4 support for Uim
Provides:	uim-qt3 = %{version}-%{release}
Obsoletes:	uim-qt3 < 1.8.6-11
%package	anthy
Summary:	Anthy support for Uim
Requires:	anthy-unicode
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager
%if %{with canna}
%package	canna
Summary:	Canna support for Uim
Requires:	Canna
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager
%endif # with canna
%package	skk
Summary:	SKK support for Uim
Requires:	skkdic
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager
%package	m17n
Summary:	m17n-lib support for Uim
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager
%description
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages. Currently, it can input to applications which
support Gtk+'s immodule, Qt's immodule and XIM.

This package provides the input method library, the XIM
bridge and most of the input methods.

For the Japanese input methods you need to install
- uim-anthy for Anthy Unicode
- uim-canna for Canna
- uim-skk for SKK.

%description	devel
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package contains the header files and the libraries which is
needed for developing Uim applications.

%description	gtk3
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package provides the Gtk IM module and helper program.

%description	qt
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package provides the Qt4 IM module and helper programs.

%description	anthy
This package provides support for Anthy, a Japanese input method.

%if %{with canna}
%description	canna
This package provides support for Canna, a Japanese input method.
%endif

%description	skk
This package provides support for SKK, a Japanese input method.

%description	m17n
This package provides support for m17n-lib, which allows input of
many languages using the input table map from m17n-db.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n uim-%{srcver}
autoconf

%build

%configure --with-x --with-xft \
	--with-libgcroots=installed \
%if %{with canna}
	--with-canna \
%endif
	--without-anthy \
	--with-anthy-utf8 \
	--with-m17nlib \
	--with-eb --with-eb-conf=%{_libdir}/eb.conf \
	--without-scim \
	--with-gtk3 --enable-gnome3-applet \
	--with-qt4 --with-qt4-immodule \
	--enable-kde4-applet \
	--with-curl \
	--with-expat \
	--disable-openssl \
	--with-sqlite3 \
	--with-lispdir=%{_datadir}/emacs/site-lisp \
	--enable-pref \
	--enable-default-toolkit=gtk3
sed -i -e 's/^\(hardcode_direct=\)$/\1no/' -e 's/^\(hardcode_minus_L=\)$/\1no/' -e 's/^\(libext=\)$/\1"a"/' libtool
make
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/uim.desktop
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/uim/plugin/*la
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/immodules/im-uim.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.*/immodules/im-uim.*a
rm -rf $RPM_BUILD_ROOT%{_includedir}/sigscheme
rm -rf $RPM_BUILD_ROOT%{_docdir}/sigscheme
rm -rf $RPM_BUILD_ROOT%{_datadir}/uim/{installed-modules,loader}.scm
rm $RPM_BUILD_ROOT%{_datadir}/uim/scim.scm || :
rm $RPM_BUILD_ROOT%{_datadir}/uim/pixmaps/scim.{svg,png} || :
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/uim.conf
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d/
cp -a fep/README fep/README.fep
cp -a fep/README.ja fep/README.fep.ja
cp -a fep/README.key fep/README.fep.key
cp -a xim/README xim/README.xim
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/uim
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/uim/{installed-modules,loader}.scm
ln -sf %{_localstatedir}/lib/uim/installed-modules.scm $RPM_BUILD_ROOT%{_datadir}/uim/
ln -sf %{_localstatedir}/lib/uim/loader.scm $RPM_BUILD_ROOT%{_datadir}/uim/
touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinputrc
%find_lang %{name}
find $RPM_BUILD_ROOT -name "*.scm" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn|installed-modules|loader)" > scm.list
cat scm.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.png" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn)" > png.list
cat png.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.svg" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn)" > svg.list
cat svg.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/ldconfig
%{inst_xinput}
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :
%postun

/sbin/ldconfig
if [ "$1" = "0" ]; then
	%{uninst_xinput}
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :
fi
%post anthy

/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister anthy > /dev/null 2>&1 || :
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register anthy-utf8 > /dev/null 2>&1 || :
%postun anthy

if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister anthy-utf8 > /dev/null 2>&1 || :
fi
%if %{with canna}
%post canna

/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register canna > /dev/null 2>&1 || :
%postun canna

if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister canna > /dev/null 2>&1 || :
fi
%endif
%post skk

/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register skk > /dev/null 2>&1 || :
%postun skk

if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister skk > /dev/null 2>&1 || :
fi
%post m17n

/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register m17nlib > /dev/null 2>&1 || :
%postun m17n

if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister m17nlib > /dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n uim-devel -f %{oreon_filedir}/uim-devel.list
%files -n uim-gtk3 -f %{oreon_filedir}/uim-gtk3.list
%files -n uim-qt -f %{oreon_filedir}/uim-qt.list
%files -n uim-anthy -f %{oreon_filedir}/uim-anthy.list
%files -n uim-skk -f %{oreon_filedir}/uim-skk.list
%files -n uim-m17n -f %{oreon_filedir}/uim-m17n.list

%changelog

%autochangelog
