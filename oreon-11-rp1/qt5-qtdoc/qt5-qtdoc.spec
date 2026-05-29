%global source0_hash none

%global qt_module qtdoc

Summary: Main Qt5 Reference Documentation
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

License: GFDL-1.3-no-invariants-or-later
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/official_releases/qt/%{qt5_version}/submodules/qtdoc-everywhere-opensource-src-%{qt5_version}.tar.xz
## upstream patches
## repo: https://invent.kde.org/qt/qt/qtdoc
## branch: kde/5.15
## git format-patch v5.15.17-lts-lgpl
Patch1:  0001-Android-keep-only-mandatory-arguments-for-configure-.patch
Patch2:  0002-Android-update-linux-package-dependencies.patch
Patch3:  0003-Remove-unneeded-italic-decoration.patch
Patch4:  0004-Doc-update-some-packages-for-Linux.patch
Patch5:  0005-Linux-Fix-library-xcb-spelling-errors.patch


BuildArch: noarch
%global _qt5_qmake %{_bindir}/qmake-qt5

# recently made unversioned, could re-add >= %%majmin if needed -- rex
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-doctools
BuildRequires: qt5-qtbase-doc

Obsoletes: qt5-qtdoc-doc < 5.9.3
Provides:  qt5-qtdoc-doc = %{version}-%{release}

%description
QtDoc contains the main Qt Reference Documentation, which includes
overviews, Qt topics, and examples not specific to any Qt module.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5}

%make_build docs


%install
make install_docs INSTALL_ROOT=%{buildroot}


%files
%doc LICENSE.FDL
%{_qt5_docdir}/qtdoc.qch
%{_qt5_docdir}/qtdoc/
%{_qt5_docdir}/qtcmake.qch
%{_qt5_docdir}/qtcmake/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
