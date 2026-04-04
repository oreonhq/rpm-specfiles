%global framework kfilemetadata
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        6.24.0
Release:	5%{?dist}

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20
# catdoc is dead upstream and will not be in epel10
# https://bugzilla.redhat.com/show_bug.cgi?id=2313773
%if %[!(0%{?rhel} >= 10)]
BuildRequires:  catdoc
Recommends:     catdoc
%endif
BuildRequires:  ebook-tools-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name
mkdir -p %{buildroot}%{_kf6_plugindir}/kfilemetadata/writers/

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/kfilemetadata_dump6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6FileMetaData.so.*
%dir %{_kf6_plugindir}/kfilemetadata/
%{_kf6_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf6_plugindir}/kfilemetadata/writers/
%{_kf6_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files devel
%{_kf6_libdir}/libKF6FileMetaData.so
%{_kf6_libdir}/cmake/KF6FileMetaData
%{_kf6_includedir}/KFileMetaData/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

