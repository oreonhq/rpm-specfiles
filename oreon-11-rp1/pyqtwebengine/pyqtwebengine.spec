%global source0_hash ae241ef2a61c782939c58b52c2aea53ad99b30f3934c8358d5e0a6ebb3fd0721

Summary: Python bindings for QtWebEngine
Name:    pyqtwebengine
Version: 5.15.6
Release: 11%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Url:     https://www.riverbankcomputing.com/software/pyqt/
Source0: %{pypi_source PyQtWebEngine}
ExclusiveArch: %{qt5_qtwebengine_arches}

## downstream patches
# may not be needed anymore? -- rdieter
#Patch100: PyQtWebEngine-Timeline.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5WebEngine)

BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-qt5
BuildRequires: python%{python3_pkgversion}-qt5-devel
BuildRequires: %{py3_dist sip} >= 5.3
BuildRequires: %{py3_dist PyQt-builder} >= 1

%description
%{summary}.

%package -n python%{python3_pkgversion}-qt5-webengine
Summary: Python3 bindings for Qt5 WebEngine
Requires:  python%{python3_pkgversion}-qt5%{?_isa}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}
%description -n python%{python3_pkgversion}-qt5-webengine
%{summary}.

%package devel
Summary: Development files for %{name}
Conflicts: python%{python3_pkgversion}-qt5-devel < 5.12.1
Requires: %{py3_dist sip} >= 5.3
%description devel
%{summary}.

%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PyQtWebEngine-%{version}

%build
PATH=%{_qt5_bindir}:$PATH ; export PATH

# Python 3 build:
sip-build \
  --no-make \
  --qmake=%{_qt5_qmake} \
  --api-dir=%{_qt5_datadir}/qsci/api/python \
  --verbose \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%make_build -C build

%install

%make_install INSTALL_ROOT=%{buildroot} -C build

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python3_sitearch}/PyQt5/*.so ; do
test -x $i  || chmod a+rx $i
done

%files -n python%{python3_pkgversion}-qt5-webengine
%doc README
%license LICENSE
%{python3_sitearch}/PyQtWebEngine-%{version}.dist-info/
%{python3_sitearch}/PyQt5/QtWebEngine.*
%{python3_sitearch}/PyQt5/QtWebEngineCore.*
%{python3_sitearch}/PyQt5/QtWebEngineWidgets.*

%files devel
%license LICENSE
%{python3_sitearch}/PyQt5/bindings/QtWebEngine*/

%files doc
# avoid dep on qscintilla-python, own %%_qt5_datadir/qsci/... here for now
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/PyQtWebEngine.api

%changelog
%autochangelog
