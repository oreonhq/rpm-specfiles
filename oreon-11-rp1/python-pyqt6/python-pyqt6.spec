%global source0_hash 45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889
%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python3_sitearch}/dbus/mainloop")
%endif
Summary:        PyQt6 is Python bindings for Qt6
Name:    python-pyqt6
Version: 6.11.0
Release:        1%{?dist}
License: gpl-3.0-only
Url:     http://www.riverbankcomputing.com/software/pyqt/
Source0:        https://pypi.python.org/packages/source/P/PyQt6/pyqt6-%{version}.tar.gz
Source1:        macros.pyqt6
Patch:   py315.patch
%if 0%{?fedora} || 0%{?epel} || (0%{?oreon} >= 11)
%ifarch %{qt6_qtwebengine_arches}
%endif
%endif
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Nfc)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6Quick3DRuntimeRender)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  python3
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(sip)
# /oreon:deps
%description
%{summary}.

%global __provides_exclude_from ^(%{_qt6_plugindir}/.*\\.so)$

%package rpm-macros
Summary: RPM macros %{name}
BuildArch: noarch
%description rpm-macros
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6
Summary: Python 3 bindings for Qt6
Provides: PyQt6 = %{version}-%{release}
Provides: PyQt6%{?_isa} = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6 = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6%{?_isa} = %{version}-%{release}
Requires: python%{python3_pkgversion}-pyqt6-base%{?_isa} = %{version}-%{release}
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6}
%description -n python%{python3_pkgversion}-pyqt6
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-base
Summary: Python 3 bindings for Qt6 base
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Provides: python%{python3_pkgversion}-PyQt6-base = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6-base%{?_isa} = %{version}-%{release}
Requires: %{name}-rpm-macros = %{version}-%{release}
Requires: python%{python3_pkgversion}-dbus
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6-base}
%description -n python%{python3_pkgversion}-pyqt6-base
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-devel
Summary: Development files for python3-qt6
Requires: python%{python3_pkgversion}-pyqt6%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Provides: python%{python3_pkgversion}-PyQt6-devel = %{version}-%{release}
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6-devel}
%description -n python%{python3_pkgversion}-pyqt6-devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt6 classes.

%package doc
Summary: Developer documentation for %{name}
Provides: PyQt6-doc = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pyqt6-%{version}%{?snap:.%{snap}} -p1

%build

PATH=%{_qt6_bindir}:$PATH ; export PATH
sip-build \
  --no-make \
  --qt-shared \
  --confirm-license \
  --qmake=%{_qt6_qmake} \
  --api-dir=%{_qt6_datadir}/qsci/api/python \
  --verbose \
  --dbus=%{_includedir}/dbus-1.0/ \
  --pep484-pyi \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags} `pkg-config --cflags dbus-python` -DQT_NO_INT128 -std=c++17"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'
%make_build -C build
%install
%make_install INSTALL_ROOT=%{buildroot} -C build
if [ "%{_prefix}" != "/usr" ]; then
  cp -ru %{buildroot}/usr/* %{buildroot}%{_prefix}/ || echo "Nothing to copy"
  rm -rf %{buildroot}/usr/*
fi
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/PyQt6
find %{buildroot} -type f -name '*.so' | xargs chmod a+rx
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python-pyqt6-rpm-macros -f %{oreon_filedir}/python-pyqt6-rpm-macros.list
%files -n python3-pyqt6 -f %{oreon_filedir}/python3-pyqt6.list
%files -n python3-pyqt6-base -f %{oreon_filedir}/python3-pyqt6-base.list
%files -n python3-pyqt6-devel -f %{oreon_filedir}/python3-pyqt6-devel.list
%files -n python-pyqt6-doc -f %{oreon_filedir}/python-pyqt6-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.11.0-4
- Import
