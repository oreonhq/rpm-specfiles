%global source0_hash d04cdc3c09c2be102a7199d73dd24c7f3cd709f95af7e51804f2668663422cfd

%global app_id  org.kde.markdownpart

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           markdownpart
Summary:        Markdown KPart
Version:        25.12.3
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/categories/utilities/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib

%description
A Markdown viewer KParts plugin, which allows KParts-using applications to
display files in Markdown format in the target format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_plugindir}/parts/markdownpart.so
%{_kf6_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
