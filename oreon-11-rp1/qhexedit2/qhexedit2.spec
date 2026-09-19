%global source0_hash 1e5803988207e9ab2c776698f68408bc6cbf5d25ef3d79a955b4122d3ff27422

%if 0%{?rhel} || 0%{?flatpak}
%bcond_with python
%else
%bcond_without python
%endif

Name:           qhexedit2
# Remember to also update version in qhexedit2_build.patch in the setup.py hunk
Version:        0.9.0
Release:        2%{?dist}
Summary:        Binary Editor for Qt

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/Simsys/qhexedit2
Source0:        https://github.com/Simsys/qhexedit2/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        qhexedit.desktop

# Add qt version suffix to libraries
Patch0:         qhexedit_qtver.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-pyqt6-sip
BuildRequires:  python3-pyqt6-devel
BuildRequires:  %{py3_dist PyQt-builder}
BuildRequires:  %{py3_dist sip} >= 5
%endif

Requires:       %{name}-qt6-libs%{?_isa} = %{version}-%{release}

%description
QHexEdit is a hex editor widget written in C++ for the Qt framework.
It is a simple editor for binary data, just like QPlainTextEdit is for text
data.

###############################################################################

%package qt5-libs
Summary:        %{name} Qt5 library

%description qt5-libs
%{name} Qt5 library.

%package        qt5-devel
Summary:        Development files for %{name} Qt5
Requires:       %{name}-qt5-libs%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name} Qt5.

%package qt6-libs
Summary:        %{name} Qt6 library

%description qt6-libs
%{name} Qt6 library.

%package        qt6-devel
Summary:        Development files for %{name} Qt5
Requires:       %{name}-qt6-libs%{?_isa} = %{version}-%{release}

%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name} Qt5.

###############################################################################

%package        doc
Summary:        Documentation and examples for %{name}
Provides:       bundled(jquery)
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation and examples for %{name}.

###############################################################################

%if %{with python}
%package -n python3-%{name}-qt5
Summary:        %{name} Qt5 Python3 bindings
Requires:       %{name}-qt5-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-qt5
%{name} Qt5 Python3 bindings.

%package -n python3-%{name}-qt5-devel
Summary:        Development files for the %{name} Qt5 Python3 bindings
Requires:       python3-%{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{py3_dist sip} >= 5

%description -n python3-%{name}-qt5-devel
Development files for the %{name} Qt5 Python3 bindings

%package -n python3-%{name}-qt6
Summary:        %{name} Qt6 Python3 bindings
Requires:       %{name}-qt6-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-qt6
%{name} Qt6 Python3 bindings.

%package -n python3-%{name}-qt6-devel
Summary:        Development files for the %{name} Qt6 Python3 bindings
Requires:       python3-%{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       %{py3_dist sip} >= 5

%description -n python3-%{name}-qt6-devel
Development files for the %{name} Qt6 Python3 bindings
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%if %{with python}
# Prepare python build trees
for qtver in Qt5 Qt6; do
mkdir Python-$qtver
pushd Python-$qtver
cp -r ../src .
cp ../license.txt .
cp ../readme.md .
cp ../python/py$(echo "$qtver" | tr '[:upper:]' '[:lower:]')-pyproject.toml pyproject.toml
cp ../python/QHexEdit.sip .
sed -i "s|%Module(name=QHexEdit)|%Module(name=Py${qtver}.QHexEdit)|" QHexEdit.sip
popd
done
%endif

%build
# Build library
mkdir build-lib-qt5
pushd build-lib-qt5
QT_VER=qt5 %qmake_qt5 ../src/qhexedit.pro
%make_build
popd
mkdir build-lib-qt6
pushd build-lib-qt6
QT_VER=qt6 %qmake_qt6 ../src/qhexedit.pro
%make_build
popd

%if %{with python}
pushd Python-Qt5
sip-build --qmake=%{_qt5_qmake} --verbose --build-dir=build --no-make
%make_build -C build
popd
pushd Python-Qt6
sip-build --qmake=%{_qt6_qmake} --verbose --build-dir=build --no-make
%make_build -C build
popd
%endif

# Build application
mkdir build-example
pushd build-example
%qmake_qt6 ../example/qhexedit.pro
%make_build
popd

%install
# Library and headers
for qtver in qt5 qt6; do
install -d %{buildroot}%{_includedir}/%{name}-${qtver}
install -d %{buildroot}%{_libdir}
cp -a src/*.h %{buildroot}%{_includedir}/%{name}-${qtver}
chmod 0755 build-lib-${qtver}/*.so.*.*
cp -a build-lib-${qtver}/*.so* %{buildroot}%{_libdir}

install -d %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}-${qtver}.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}/%{name}-${qtver}

Name: %{name}-${qtver}
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqhexedit-${qtver}
EOF
done

# Python bindings
%if %{with python}
%make_install INSTALL_ROOT=%{buildroot} -C Python-Qt5/build
%make_install INSTALL_ROOT=%{buildroot} -C Python-Qt6/build
%endif

# Application
install -Dpm 0755 build-example/qhexedit %{buildroot}%{_bindir}/qhexedit
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}

%files
%{_bindir}/qhexedit
%{_datadir}/applications/qhexedit.desktop

%files qt5-libs
%license license.txt
%{_libdir}/libqhexedit-qt5.so.0*

%files qt5-devel
%{_includedir}/%{name}-qt5/
%{_libdir}/libqhexedit-qt5.so
%{_libdir}/pkgconfig/%{name}-qt5.pc

%files qt6-libs
%license license.txt
%{_libdir}/libqhexedit-qt6.so.0*

%files qt6-devel
%{_includedir}/%{name}-qt6/
%{_libdir}/libqhexedit-qt6.so
%{_libdir}/pkgconfig/%{name}-qt6.pc

%files doc
%license license.txt
%doc doc/html

%if %{with python}
%files -n python3-%{name}-qt5
%{python3_sitearch}/PyQt5/QHexEdit.*.so
%{python3_sitearch}/pyqt5_qhexedit-%{version}.dist-info/

%files -n python3-%{name}-qt5-devel
%{python3_sitearch}/PyQt5/bindings/QHexEdit/

%files -n python3-%{name}-qt6
%{python3_sitearch}/PyQt6/QHexEdit.*.so
%{python3_sitearch}/pyqt6_qhexedit-%{version}.dist-info/

%files -n python3-%{name}-qt6-devel
%{python3_sitearch}/PyQt6/bindings/QHexEdit/
%endif

%changelog
%autochangelog
