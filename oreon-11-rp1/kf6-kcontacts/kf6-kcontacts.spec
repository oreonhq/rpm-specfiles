%global source1_hash 678365120333d2eb1c19b77e609e486a53d7d06868936184e15e1dc0cd9b0c12
%global source0_hash 170b51a41ac132968ea03d5f1ce8c585777155bbdc57e819a0562b1f8d03b7a5
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
%global framework kcontacts
Name:    kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        The KContacts Library
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6Codecs)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%cmake_build_kf6
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kcontacts-devel -f %{oreon_filedir}/kf6-kcontacts-devel.list
%files -n kf6-kcontacts-doc -f %{oreon_filedir}/kf6-kcontacts-doc.list
%files -n kf6-kcontacts-html -f %{oreon_filedir}/kf6-kcontacts-html.list

%changelog

%autochangelog
