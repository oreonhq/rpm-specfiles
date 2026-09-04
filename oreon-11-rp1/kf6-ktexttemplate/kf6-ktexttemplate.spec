%global source0_hash a184163f7d5d2ac4cd4a71d04bee830020332552bfa9eb5159ced57b20edd527

%global		framework ktexttemplate

%global stable_kf6 stable
%global majmin_ver_kf6 6.28

Name:		kf6-%{framework}
Version:	6.29.0
Release:        1%{?dist}
Summary:	Separates the structure of documents from their data
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)

%description
The goal of KTextTemplate is to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming and advanced generation of other text such as code.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version}

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%license LICENSES/*.txt
%{_libdir}/libKF6TextTemplate.so.*
%{_kf6_plugindir}/ktexttemplate
%{_kf6_datadir}/qlogging-categories6/ktexttemplate.categories

%files devel
%{_kf6_includedir}/KTextTemplate
%{_libdir}/cmake/KF6TextTemplate
%{_libdir}/libKF6TextTemplate.so


%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.29.0-1
- Latest upstream release

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

