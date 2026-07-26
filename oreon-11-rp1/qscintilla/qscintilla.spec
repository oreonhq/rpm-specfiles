%global source0_hash dfe13c6acc9d85dfcba76ccc8061e71a223957a6c02f3c343b30a9d43a4cdd4d

%global scintilla_ver 3.10.1

%bcond_without qt5
%bcond_without qt6

Summary: A Scintilla port to Qt
Name:    qscintilla
Version: 2.14.1
Release: 7%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Url:     http://www.riverbankcomputing.com/software/qscintilla/
%if 0%{?snap:1}
Source0: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_gpl-%{version}-snapshot-%{snap}.tar.gz
%else
Source0: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires: gcc-c++

Provides: bundled(scintilla) = %{scintilla_ver}

%description
QScintilla is a port of Scintilla to the Qt GUI toolkit.

%{?scintilla_ver:This version of QScintilla is based on Scintilla v%{scintilla_ver}.}

%if %{with qt5}
%package qt5
Summary: A Scintilla port to Qt5
Provides: bundled(scintilla) = %{scintilla_ver}
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)

%description qt5
%{summary}.

%package qt5-devel
Summary:  QScintilla Development Files
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel

%description qt5-devel
%{summary}.

# EPEL 10 does not have python3-qt5 yet
%if %{defined fedora}
%package -n python3-qscintilla-qt5
Summary:  QScintilla-qt5 python3 bindings
BuildRequires: python3-devel
BuildRequires: python3-qt5
BuildRequires: python3-qt5-devel
BuildRequires: %{py3_dist sip} >= 5.3
BuildRequires: %{py3_dist PyQt-builder} >= 1
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: python3-qt5%{?pyqt5_version: >= %{pyqt5_version}}

%description -n python3-qscintilla-qt5
%{summary}.

%package -n python3-qscintilla-qt5-devel
Summary:  Development files for QScintilla-qt5 python3 bindings
Requires: python3-qt5-devel

%description -n python3-qscintilla-qt5-devel
%{summary}.
%endif
%endif

%if %{with qt6}
%package qt6
Summary: A Scintilla port to Qt6
Provides: bundled(scintilla) = %{scintilla_ver}
BuildRequires: pkgconfig(Qt6Designer)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)

%description qt6
%{summary}.

%package qt6-devel
Summary:  QScintilla Development Files
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel

%description qt6-devel
%{summary}.

%package -n python3-qscintilla-qt6
Summary:  QScintilla-qt6 python3 bindings
BuildRequires: python3-devel
BuildRequires: python3-pyqt6
BuildRequires: python3-pyqt6-devel
BuildRequires: %{py3_dist sip} >= 5.3
BuildRequires: %{py3_dist PyQt-builder} >= 1
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: python3-pyqt6%{?pyqt6_version: >= %{pyqt6_version}}

%description -n python3-qscintilla-qt6
%{summary}.

%package -n python3-qscintilla-qt6-devel
Summary:  Development files for QScintilla-qt6 python3 bindings
Requires: python3-pyqt6-devel

%description -n python3-qscintilla-qt6-devel
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n QScintilla_src-%{version}%{?snap:-snapshot-%{snap}}

%build
export QMAKEFEATURES=$PWD/src/features;

%if %{with qt5}
cp -a src src-qt5
pushd src-qt5
%qmake_qt5 qscintilla.pro
%make_build
popd

cp -a designer designer-qt5
pushd designer-qt5
%qmake_qt5 designer.pro INCLUDEPATH+=../src-qt5 LIBS+=-L../src-qt5
%make_build
popd

%if %{defined fedora}
cp -a Python Python-qt5
pushd Python-qt5
ln -s pyproject-qt5.toml pyproject.toml
LD_LIBRARY_PATH=$PWD/../src-qt5 sip-build --no-make   --qmake=%{_qt5_qmake} --api-dir=%{_qt5_datadir}/qsci/api/python --verbose \
    --qmake-setting 'QMAKE_CXXFLAGS+="%{build_cxxflags}"' --qmake-setting 'QMAKE_LDFLAGS+="%{build_ldflags}"' \
    --qsci-include-dir=../src-qt5 --qsci-library-dir=../src-qt5/ --qsci-features-dir=../src-qt5/features
%make_build -C build
popd
%endif
%endif

%if %{with qt6}
cp -a src src-qt6
pushd src-qt6
%qmake_qt6 qscintilla.pro
%make_build
popd

cp -a designer designer-qt6
pushd designer-qt6
%qmake_qt6 designer.pro INCLUDEPATH+=../src-qt6 LIBS+=-L../src-qt6
%make_build
popd

cp -a Python Python-qt6
pushd Python-qt6
ln -s pyproject-qt6.toml pyproject.toml
LD_LIBRARY_PATH=$PWD/../src-qt6 sip-build --no-make   --qmake=%{_qt6_qmake} --api-dir=%{_qt6_datadir}/qsci/api/python --verbose \
    --qmake-setting 'QMAKE_CXXFLAGS+="%{build_cxxflags}"' --qmake-setting 'QMAKE_LDFLAGS+="%{build_ldflags}"' \
    --qsci-include-dir=../src-qt6 --qsci-library-dir=../src-qt6/ --qsci-features-dir=../src-qt6/features
%make_build -C build
popd
%endif

%install
%if %{with qt5}
%make_install -C src-qt5 INSTALL_ROOT=%{buildroot}
%make_install -C designer-qt5 INSTALL_ROOT=%{buildroot}
%if %{defined fedora}
%make_install -C Python-qt5/build INSTALL_ROOT=%{buildroot}
%endif

# Drop Python api files
rm -f %{buildroot}%{_qt5_datadir}/qsci/api/python/Python*.api
%endif

%if %{with qt6}
%make_install -C src-qt6 INSTALL_ROOT=%{buildroot}
%make_install -C designer-qt6 INSTALL_ROOT=%{buildroot}
%make_install -C Python-qt6/build INSTALL_ROOT=%{buildroot}

# Drop Python api files
rm -f %{buildroot}%{_qt6_datadir}/qsci/api/python/Python*.api
%endif

%if 0%{?flatpak}
# prefix is not configurable at build time
mv %{buildroot}/usr/include %{buildroot}/usr/%{_lib} %{buildroot}%{_prefix}/
mv %{buildroot}/usr/share/qt5/translations %{buildroot}%{_qt5_datadir}
mv %{buildroot}/usr/share/qt6/translations %{buildroot}%{_qt6_datadir}
rm -f %{buildroot}/usr/share/qt*/qsci/api/python/Python*.api
%endif

%find_lang qscintilla --with-qt
%if %{with qt5}
grep "%{_qt5_translationdir}" qscintilla.lang > qscintilla-qt5.lang
%endif
%if %{with qt6}
grep "%{_qt6_translationdir}" qscintilla.lang > qscintilla-qt6.lang
%endif

%if %{with qt5}
%files qt5 -f qscintilla-qt5.lang
%doc NEWS
%license LICENSE
%{_qt5_libdir}/libqscintilla2_qt5.so.15*
%{_qt5_plugindir}/designer/libqscintillaplugin.so

%files qt5-devel
%doc doc/html doc/Scintilla example
%{_qt5_headerdir}/Qsci/
%{_qt5_libdir}/libqscintilla2_qt5.so
%{_qt5_archdatadir}/mkspecs/features/qscintilla2.prf

%if %{defined fedora}
%files -n python3-qscintilla-qt5
%{python3_sitearch}/PyQt5/Qsci.*
%{_qt5_datadir}/qsci/
%{python3_sitearch}/qscintilla-%{version}.dist-info/

%files -n python3-qscintilla-qt5-devel
%{python3_sitearch}/PyQt5/bindings/Qsci/
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/QScintilla.api
%endif
%endif

%if %{with qt6}
%files qt6 -f qscintilla-qt6.lang
%doc NEWS
%license LICENSE
%{_qt6_libdir}/libqscintilla2_qt6.so.15*
%{_qt6_plugindir}/designer/libqscintillaplugin.so

%files qt6-devel
%doc doc/html doc/Scintilla example
%{_qt6_headerdir}/Qsci/
%{_qt6_libdir}/libqscintilla2_qt6.so
%{_qt6_archdatadir}/mkspecs/features/qscintilla2.prf

%files -n python3-qscintilla-qt6
%{python3_sitearch}/PyQt6/Qsci.*
%{_qt6_datadir}/qsci/
%{python3_sitearch}/pyqt6_qscintilla-%{version}.dist-info/

%files -n python3-qscintilla-qt6-devel
%{python3_sitearch}/PyQt6/bindings/Qsci/
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python/
%doc %{_qt6_datadir}/qsci/api/python/PyQt6-QScintilla.api
%endif

%changelog
%autochangelog
