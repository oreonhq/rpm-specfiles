%global source0_hash none

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name:		zbar
Version:	0.23.93
Release:	11%{?dist}
Summary:	Bar code reader

License:	LGPL-2.1-or-later
URL:		http://zbar.sourceforge.net/
Source0:	https://linuxtv.org/downloads/%{name}/%{name}-%{version}.tar.bz2
Patch0:		use_python3_on_python_script.patch
Patch1:		fix_qt_overlinking.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	GraphicsMagick-devel
BuildRequires:	gtk3-devel
BuildRequires:	libSM-devel
BuildRequires:	libtool
BuildRequires:	libv4l-devel
BuildRequires:	libXv-devel
BuildRequires:	make
BuildRequires:	python3-gobject-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	xmlto
%if %{JAVA}
BuildRequires:	java-devel
%endif
BuildRequires:	python3-devel
BuildRequires:  python3-setuptools

%description
ZBar Bar Code Reader is an open source software suite for reading bar
codes from various sources, such as video streams, image files and raw
intensity sensors. It supports EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 93, Code 39, Codabar, Interleaved 2 of 5, QR Code and SQ Code.

%package devel
Summary: Bar code reader library extra development files
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
This package contains header files and additional libraries used for
developing applications that read bar codes with this library.

%package libs
Summary: Bar code reader library

%description libs
This package contains the ZBar Bar Code Reader library.

%package gtk
Summary: Bar code reader GTK widget
Requires: %{name}-libs%{_isa} = %{version}-%{release}
# Obsoleted in F37
Obsoletes: %{name}-gi < %{version}-%{release}

%description gtk
This package contains a bar code scanning widget for use with GUI
applications based on GTK 3.

%package gtk-devel
Summary: Bar code reader GTK widget extra development files
Requires: %{name}-devel%{_isa} = %{version}-%{release}
Requires: %{name}-gtk%{_isa} = %{version}-%{release}

%description gtk-devel
This package contains header files and additional libraries used for
developing GUI applications based on GTK 3 that include a bar code
scanning widget.

%package qt
Summary: Bar code reader Qt widget
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description qt
This package contains a bar code scanning widget for use with GUI
applications based on Qt4.

%package qt-devel
Summary: Bar code reader Qt widget extra development files
Requires: %{name}-devel%{_isa} = %{version}-%{release}
Requires: %{name}-qt%{_isa} = %{version}-%{release}

%description qt-devel
This package contains header files and additional libraries used for
developing GUI applications based on Qt5 that include a bar code
scanning widget.

%package -n python3-zbar
Summary: Bar code reader PyGTK widget
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: python3-pillow
# Renamed in F37
Obsoletes: %{name}-python3 < %{version}-%{release}

%description -n python3-zbar
This package contains a bar code scanning widget for use on
python applications that work with images.

%if %{JAVA}
%package java
Summary: Bar code reader Java library
Requires: %{name}-devel%{_isa} = %{version}-%{release}
Requires: %{name}-gtk%{_isa} = %{version}-%{release}

%description java
This package contains header files and additional libraries used for
on Java Native Interface (JNI) applications using ZBar.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1
%patch 1 -p1

%build
autoreconf -fiv
%configure --with-python=python3 --with-gtk=auto --with-dbusconfdir=%{_sysconfdir} --docdir=%{_docdir}/%{name}-%{version} --with-graphicsmagick --without-xshm --without-xv --enable-codes=ean,databar,code128,code93,code39,codabar,i25,qrcode,sqcode,pdf417

# rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
%if %{JAVA}
install -d %{buildroot}%{_jnidir}
mv %{buildroot}%{_datadir}/zbar/lib/zbar.jar %{buildroot}%{_jnidir}
mv %{buildroot}%{_datadir}/zbar/lib/libzbarjni.so* %{buildroot}%{_libdir}
%endif
cp test/test_python.py %{buildroot}%{_docdir}

#Remove .la and .a files
find ${RPM_BUILD_ROOT} -name '*.la' -or -name '*.a' | xargs rm -f

# Remove installed doc
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%ldconfig_scriptlets

%ldconfig_scriptlets devel

%ldconfig_scriptlets gtk

%ldconfig_scriptlets qt

%find_lang zbar

%files
%doc NEWS.md README.md INSTALL.md
%{_bindir}/zbarimg
%{_bindir}/zbarcam
%{_mandir}/man1/*
%{_sysconfdir}/dbus-1/system.d/org.linuxtv.Zbar.conf

%files libs -f zbar.lang
%license COPYING LICENSE.md
%{_libdir}/libzbar.so.0*

%files devel
%doc HACKING.md TODO.md
%{_libdir}/libzbar.so
%{_libdir}/pkgconfig/zbar.pc
%dir %{_includedir}/zbar
%{_includedir}/zbar.h
%{_includedir}/zbar/Exception.h
%{_includedir}/zbar/Symbol.h
%{_includedir}/zbar/Image.h
%{_includedir}/zbar/Scanner.h
%{_includedir}/zbar/Decoder.h
%{_includedir}/zbar/ImageScanner.h
%{_includedir}/zbar/Video.h
%{_includedir}/zbar/Window.h
%{_includedir}/zbar/Processor.h

%files gtk
%{_libdir}/libzbargtk.so.*
%{_bindir}/zbarcam-gtk

%files gtk-devel
%{_libdir}/libzbargtk.so
%{_libdir}/pkgconfig/zbar-gtk.pc
%{_includedir}/zbar/zbargtk.h

%files qt
%{_libdir}/libzbarqt.so.*
%{_bindir}/zbarcam-qt

%files qt-devel
%{_libdir}/libzbarqt.so
%{_libdir}/pkgconfig/zbar-qt.pc
%{_includedir}/zbar/QZBar*.h

%if %{JAVA}
%files java
%{_jnidir}/zbar.jar
%{_libdir}/libzbarjni.so*
%endif

%files -n python3-zbar
%{python3_sitearch}/zbar.so
%{_docdir}/test_python.py

%changelog
%autochangelog

