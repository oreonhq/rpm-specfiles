%global source0_hash e5625757913caf66a9d702ba102ae92cb165d8dde17759b6de9fdea84a1f857f
%global qt_module qttranslations
Summary:        Qt5 - QtTranslations module
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        2%{?dist}
License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
BuildArch: noarch
%global _qt5_qmake %{_bindir}/qmake-qt5
%if 0%{?_qt5:1}
Provides: %{_qt5}-ar = %{version}-%{release}
Provides: %{_qt5}-ca = %{version}-%{release}
Provides: %{_qt5}-cs = %{version}-%{release}
Provides: %{_qt5}-da = %{version}-%{release}
Provides: %{_qt5}-de = %{version}-%{release}
Provides: %{_qt5}-es = %{version}-%{release}
Provides: %{_qt5}-fa = %{version}-%{release}
Provides: %{_qt5}-fi = %{version}-%{release}
Provides: %{_qt5}-fr = %{version}-%{release}
Provides: %{_qt5}-gl = %{version}-%{release}
Provides: %{_qt5}-gd = %{version}-%{release}
Provides: %{_qt5}-he = %{version}-%{release}
Provides: %{_qt5}-hu = %{version}-%{release}
Provides: %{_qt5}-hr = %{version}-%{release}
Provides: %{_qt5}-it = %{version}-%{release}
Provides: %{_qt5}-ja = %{version}-%{release}
Provides: %{_qt5}-ko = %{version}-%{release}
Provides: %{_qt5}-lt = %{version}-%{release}
Provides: %{_qt5}-lv = %{version}-%{release}
Provides: %{_qt5}-nl = %{version}-%{release}
Provides: %{_qt5}-nn = %{version}-%{release}
Provides: %{_qt5}-pl = %{version}-%{release}
Provides: %{_qt5}-pt = %{version}-%{release}
Provides: %{_qt5}-pt_BR = %{version}-%{release}
Provides: %{_qt5}-ru = %{version}-%{release}
Provides: %{_qt5}-sk = %{version}-%{release}
Provides: %{_qt5}-sl = %{version}-%{release}
Provides: %{_qt5}-sv = %{version}-%{release}
Provides: %{_qt5}-uk = %{version}-%{release}
Provides: %{_qt5}-zh_CN = %{version}-%{release}
Provides: %{_qt5}-zh_TW = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{version}

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
