%global source0_hash none

%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python3_sitearch}/dbus/mainloop")
%endif

# enable/disable individual modules
# drop power64, it's not supported yet (than)
%if 0
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
%global webengine 1
%endif
%endif

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# see also https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/JQQ66XJSIT2FGTK2YQY7AXMEH5IXMPUX/
%undefine _strict_symbol_defs_build

%global snap dev2507081429

Summary: PyQt5 is Python bindings for Qt5
Name:    python-qt5
Version: 5.15.12
Release: 0.2%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Url:     http://www.riverbankcomputing.com/software/pyqt/
Source0:        https://www.riverbankcomputing.com/static/Downloads/PyQt5/%{version}/pyqt5-%{version}%{?snap:.%{snap}}.tar.gz
#Source0: https://pypi.python.org/packages/source/P/PyQt5/PyQt5-{version}.tar.gz

Source1: macros.pyqt5

## upstream patches

## upstreamable patches
# support newer Qt5 releases, but may not be needed anymore?  -- rdieter
#Patch0: PyQt5-Timeline.patch

BuildRequires: make
BuildRequires: chrpath
BuildRequires: findutils
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-python)
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires: pkgconfig(phonon4qt5)
%endif
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: pkgconfig(Qt5Core) >= 5.5
%if 0%{?enginio}
BuildRequires: pkgconfig(Enginio)
%endif
BuildRequires: pkgconfig(Qt5Bluetooth)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: pkgconfig(Qt5Multimedia) pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(Qt5Nfc)
BuildRequires: pkgconfig(Qt5Network) pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Positioning)
BuildRequires: pkgconfig(Qt5Quick) pkgconfig(Qt5QuickWidgets)
#BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: pkgconfig(Qt5Sql) pkgconfig(Qt5Svg) pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml) pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5WebChannel)
BuildRequires: pkgconfig(Qt5WebSockets)
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-dbus
BuildRequires: %{py3_dist PyQt-builder} >= 1.1.0
BuildRequires: %{py3_dist sip} >= 5.3

# when split out
%if 0%{?webengine}
Obsoletes: python-qt5 < 5.5.1-10
%endif

%description
%{summary}.

%global __provides_exclude_from ^(%{_qt5_plugindir}/.*\\.so)$

%package rpm-macros
Summary: RPM macros %{name}
# when split out
Conflicts: python-qt5 < 5.6
Conflicts: python3-qt5 < 5.6
BuildArch: noarch
%description rpm-macros
%{summary}.

%package -n python%{python3_pkgversion}-qt5
Summary: Python 3 bindings for Qt5
# when split out
%if 0%{?webengine}
Obsoletes: python3-qt5 < 5.5.1-10
%endif
Provides: PyQt5 = %{version}-%{release}
Provides: PyQt5%{?_isa} = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt5 = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt5%{?_isa} = %{version}-%{release}
Requires: python%{python3_pkgversion}-qt5-base%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5}
# When python-qt5-webkit was dropped
Obsoletes: python%{python3_pkgversion}-qt5-webkit < 5.15.11-4
%description -n python%{python3_pkgversion}-qt5
%{summary}.

%package -n python%{python3_pkgversion}-qt5-base
Summary: Python 3 bindings for Qt5 base
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Provides: python%{python3_pkgversion}-PyQt5-base = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt5-base%{?_isa} = %{version}-%{release}
Requires: %{name}-rpm-macros = %{version}-%{release}
Requires: python%{python3_pkgversion}-dbus
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-base}
%description -n python%{python3_pkgversion}-qt5-base
%{summary}.

%package -n python%{python3_pkgversion}-qt5-devel
Summary: Development files for python3-qt5
Requires: python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Provides: python%{python3_pkgversion}-PyQt5-devel = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-devel}
%description -n python%{python3_pkgversion}-qt5-devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt5 classes

%package doc
Summary: Developer documentation for %{name}
Provides: PyQt5-doc = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%if 0%{?webengine}
%package -n python%{python3_pkgversion}-qt5-webengine
Summary: Python3 bindings for Qt5 WebEngine
BuildRequires: pkgconfig(Qt5WebEngine)
Obsoletes: python3-webengine < 5.5.1-13
Obsoletes: python3-qt5 < 5.5.1-10
Requires:  python%{python3_pkgversion}-qt5%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}
%description -n python%{python3_pkgversion}-qt5-webengine
%{summary}.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n pyqt5-%{version}%{?snap:.%{snap}}

#patch0 -p1


%build
## see also https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html

PATH=%{_qt5_bindir}:$PATH ; export PATH

# Python 3 build:
sip-build \
  --no-make \
  --qt-shared \
  --confirm-license \
  --qmake=%{_qt5_qmake} \
  --api-dir=%{_qt5_datadir}/qsci/api/python \
  --verbose \
  --dbus=%{_includedir}/dbus-1.0/ \
  --pep484-pyi \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{optflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{optflags} `pkg-config --cflags dbus-python`"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"'

%make_build -C build


%install

# Python 3 build:
%make_install INSTALL_ROOT=%{buildroot} -C build
if [ "%{_prefix}" != "/usr" ]; then
  cp -ru %{buildroot}/usr/* %{buildroot}%{_prefix}/ || echo "Nothing to copy"
  rm -rf %{buildroot}/usr/*
fi

# Explicitly byte compile as the automagic byte compilation doesn't work for
# /app prefix in flatpak builds
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/PyQt5

# ensure .so modules are executable for proper -debuginfo extraction
find %{buildroot} -type f -name '*.so' | xargs chmod a+rx

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.pyqt5
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.pyqt5


%files rpm-macros
%{rpm_macros_dir}/macros.pyqt5

%files -n python%{python3_pkgversion}-qt5
%if 0%{?enginio}
%{python3_sitearch}/PyQt5/Enginio.*
%endif
%{python3_sitearch}/PyQt5/QtBluetooth.*
%{python3_sitearch}/PyQt5/QtDesigner.*
%{python3_sitearch}/PyQt5/QtHelp.*
%{python3_sitearch}/PyQt5/QtLocation.*
%{python3_sitearch}/PyQt5/QtMultimedia.*
%{python3_sitearch}/PyQt5/QtMultimediaWidgets.*
%{python3_sitearch}/PyQt5/QtNfc.*
%{python3_sitearch}/PyQt5/QtPositioning.*
%{python3_sitearch}/PyQt5/QtQml.*
%{python3_sitearch}/PyQt5/QtQuick.*
%{python3_sitearch}/PyQt5/QtQuickWidgets.*
%{python3_sitearch}/PyQt5/QtSensors.*
%{python3_sitearch}/PyQt5/QtSerialPort.*
%{python3_sitearch}/PyQt5/QtSvg.*
%{python3_sitearch}/PyQt5/QtWebChannel.*
%{python3_sitearch}/PyQt5/QtWebSockets.*
%{python3_sitearch}/PyQt5/QtX11Extras.*
%{python3_sitearch}/PyQt5/QtXmlPatterns.*

%files -n python%{python3_pkgversion}-qt5-base
%doc NEWS README.md
%license LICENSE
%{python3_dbus_dir}/pyqt5.abi3.so
%dir %{python3_sitearch}/PyQt5/
%{python3_sitearch}/pyqt5-%{version}%{?snap:.%{snap}}.dist-info
%{python3_sitearch}/PyQt5/__pycache__/__init__.*
%{python3_sitearch}/PyQt5/__init__.py*
%{python3_sitearch}/PyQt5/Qt.*
%{python3_sitearch}/PyQt5/QtCore.*
%{python3_sitearch}/PyQt5/QtDBus.*
%{python3_sitearch}/PyQt5/QtGui.*
%{python3_sitearch}/PyQt5/QtNetwork.*
%{python3_sitearch}/PyQt5/QtOpenGL.*
%{python3_sitearch}/PyQt5/QtPrintSupport.*
%{python3_sitearch}/PyQt5/QtSql.*
%{python3_sitearch}/PyQt5/QtTest.*
%{python3_sitearch}/PyQt5/QtWidgets.*
%{python3_sitearch}/PyQt5/QtXml.*
%{python3_sitearch}/PyQt5/_QOpenGLFunctions_2_0.*
%{python3_sitearch}/PyQt5/_QOpenGLFunctions_2_1.*
%{python3_sitearch}/PyQt5/_QOpenGLFunctions_4_1_Core.*
# plugins
%{_qt5_plugindir}/PyQt5/
%{_qt5_plugindir}/designer/libpyqt5.so
%{python3_sitearch}/PyQt5/uic/
# *was* in python3-qt5-devel
%{_bindir}/pylupdate5
%{_bindir}/pyrcc5
%{_bindir}/pyuic5
%{python3_sitearch}/PyQt5/pylupdate.abi3.so
%{python3_sitearch}/PyQt5/pylupdate_main.py*
%{python3_sitearch}/PyQt5/__pycache__/pylupdate_main*
%{python3_sitearch}/PyQt5/pyrcc.abi3.so
%{python3_sitearch}/PyQt5/pyrcc_main.py*
%{python3_sitearch}/PyQt5/__pycache__/pyrcc_main*
%{python3_sitearch}/PyQt5/py.typed
%{python3_sitearch}/PyQt5/sip.pyi

%if 0%{?webengine}
%files -n python%{python3_pkgversion}-qt5-webengine
%{python3_sitearch}/PyQt5/QtWebEngine.*
%{python3_sitearch}/PyQt5/QtWebEngineCore.*
%{python3_sitearch}/PyQt5/QtWebEngineWidgets.*
%endif

%files -n python%{python3_pkgversion}-qt5-devel
%{python3_sitearch}/PyQt5/bindings/

%files doc
#doc doc/*
%doc examples/
# avoid dep on qscintilla-python, own %%_qt5_datadir/qsci/... here for now
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/PyQt5.api


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.12-0.2
- Import
