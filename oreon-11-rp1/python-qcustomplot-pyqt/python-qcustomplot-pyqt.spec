%global source0_hash f16609c7653d07de2518e405e266b5ca12752b447072967d2ef64f54824a2390

%global QCP_VER 2.1.1
Name:          python-qcustomplot-pyqt
Version:       2.1.1.2
Release:       3%{?dist}
Summary:       Python bindings for QCustomPlot2
# https://github.com/salsergey/QCustomPlot-PyQt/issues/7
License:       MIT and GPLv3
Url:           https://github.com/salsergey/QCustomPlot-PyQt
Source0:       %{url}/releases/download/v%{version}/QCustomPlot-PyQt-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: python3-devel
# sip6
BuildRequires: %{py3_dist sip}
BuildRequires: %{py3_dist PyQt-builder}

%description
This is Python bindings for QCustomPlot - Qt C++ library for plotting and data
visualization.

%package -n python3-qcustomplot-pyqt5
Summary:       PyQt5 binding for QCustomPlot2
License:       MIT
BuildRequires: qt5-qtbase-devel
# qcustomplot-qt5-devel
BuildRequires: pkgconfig(qcustomplot-qt5) == %{QCP_VER}
BuildRequires: python3-qt5-devel
Requires:      python3-qt5
Requires:      qcustomplot-qt5 == %{QCP_VER}

%description -n python3-qcustomplot-pyqt5
This is Python-PyQt5 binding for QCustomPlot - Qt C++ library for plotting and
data visualization.

%package -n python3-qcustomplot-pyqt6
Summary:       PyQt6 binding for QCustomPlot2
License:       MIT and GPLv3
BuildRequires: qt6-qtbase-devel
# qcustomplot-qt6-devel
BuildRequires: pkgconfig(qcustomplot-qt6) == %{QCP_VER}
BuildRequires: python3-pyqt6-devel
Requires:      python3-pyqt6
Requires:      qcustomplot-qt6 == %{QCP_VER}

%description -n python3-qcustomplot-pyqt6
This is Python-PyQt6 binding for QCustomPlot - Qt C++ library for plotting and
data visualization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n QCustomPlot-PyQt-%{version}
rm -rf src

%build
# qt5
sip-build \
  --build-dir build-qt5 \
  --qmake %{_qt5_qmake} \
  --qcustomplot-lib qcustomplot-qt5 \
  --no-static-qcustomplot \
  --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'
%make_build -C build-qt5
# qt6
sip-build \
  --build-dir build-qt6 \
  --qmake %{_qt6_qmake} \
  --qcustomplot-lib qcustomplot-qt6 \
  --no-static-qcustomplot \
  --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'
%make_build -C build-qt6

%install
pushd build-qt5
%make_install INSTALL_ROOT=%{buildroot}
popd
pushd build-qt6
%make_install INSTALL_ROOT=%{buildroot}
# small hack
chmod a+rx %{buildroot}%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt*.so

%files -n python3-qcustomplot-pyqt5
%doc README.md examples/
%license LICENSE-MIT.txt LICENSE-gpl-3.0.txt
%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt5*

%files -n python3-qcustomplot-pyqt6
%doc README.md
%license LICENSE-MIT.txt LICENSE-gpl-3.0.txt
%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt6*

%changelog
%autochangelog
