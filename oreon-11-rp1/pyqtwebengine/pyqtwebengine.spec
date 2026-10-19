%global source0_hash f121ac6e4a2f96ac289619bcfc37f64e68362f24a346553f5d6c42efa4228a4d
Summary:        Python bindings for QtWebEngine
Name:    pyqtwebengine
Version: 5.15.7
Release:        1%{?dist}
License: GPL-3.0-only
Url:     https://www.riverbankcomputing.com/software/pyqt/
Source0:        https://files.pythonhosted.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
ExclusiveArch: %{qt5_qtwebengine_arches}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-qt5
BuildRequires:  python3-qt5-devel
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(sip)
# /oreon:deps
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
for i in %{buildroot}%{python3_sitearch}/PyQt5/*.so ; do
test -x $i  || chmod a+rx $i
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-qt5-webengine -f %{oreon_filedir}/python3-qt5-webengine.list
%files -n pyqtwebengine-devel -f %{oreon_filedir}/pyqtwebengine-devel.list
%files -n pyqtwebengine-doc -f %{oreon_filedir}/pyqtwebengine-doc.list

%changelog

%autochangelog
