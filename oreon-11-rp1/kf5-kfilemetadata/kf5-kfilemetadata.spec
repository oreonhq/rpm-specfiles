%global source0_hash 195c2c8c4a18a24552fd1c020335f7e1e564c3acfaec4e918319d62c8067ce8f

%undefine __cmake_in_source_build
%global framework kfilemetadata

# Define to 1 to enable ffmpeg extractor
%global         ffmpeg 1

%if 0%{?fedora}
%global         catdoc 1
%global         ebook 1
%global         poppler 1
%global         taglib 1
%endif

%if 0%{?rhel}
%global         poppler 1
%global         taglib 1
%endif

Name:           kf5-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        5.116.0
Release:        11%{?dist}

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://cgit.kde.org/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
# optional
BuildRequires:  kf5-kconfig-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel

BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20

## optional deps
%if 0%{?catdoc}
# not strictly required at build-time, satisfying runtime dep check only
BuildRequires:  catdoc
Recommends:     catdoc
%endif
%if 0%{?ebook}
BuildRequires:  ebook-tools-devel
%endif
%if 0%{?ffmpeg}
BuildRequires:  ffmpeg-free-devel
%endif
%if 0%{?poppler}
BuildRequires:  pkgconfig(poppler-qt5)
%endif
%if 0%{?taglib}
BuildRequires:  pkgconfig(taglib) >= 1.9
%endif

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

mkdir -p %{buildroot}%{_kf5_plugindir}/kfilemetadata/writers/

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_libdir}/libKF5FileMetaData.so.*

# consider putting these into some subpkg ?
%dir %{_kf5_plugindir}/kfilemetadata/
%{_kf5_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf5_plugindir}/kfilemetadata/writers/
%if 0%{?taglib}
%{_kf5_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so
%endif

%files devel
%{_kf5_libdir}/libKF5FileMetaData.so
%{_kf5_libdir}/cmake/KF5FileMetaData
%{_kf5_includedir}/KFileMetaData/
%{_kf5_archdatadir}/mkspecs/modules/qt_KFileMetaData.pri

%changelog
%autochangelog
