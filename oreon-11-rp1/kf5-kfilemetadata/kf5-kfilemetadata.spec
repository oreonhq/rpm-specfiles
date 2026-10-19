%global source0_hash 195c2c8c4a18a24552fd1c020335f7e1e564c3acfaec4e918319d62c8067ce8f
%undefine __cmake_in_source_build
%global framework kfilemetadata
%global         ffmpeg 1
Name:           kf5-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        5.116.0
Release:        11%{?dist}
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://cgit.kde.org/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$
%if 0%{?catdoc}
Recommends:     catdoc
%endif
%if 0%{?ebook}
%endif
%if 0%{?ffmpeg}
%endif
%if 0%{?poppler}
%endif
%if 0%{?taglib}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  ffmpeg-free-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kfilemetadata-devel -f %{oreon_filedir}/kf5-kfilemetadata-devel.list

%changelog

%autochangelog
