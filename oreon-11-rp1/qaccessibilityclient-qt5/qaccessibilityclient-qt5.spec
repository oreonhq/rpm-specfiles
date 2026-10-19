%global source0_hash 1e3261a9c90af466fb1835749ff6ea94052e829d71b421bbbccd5fd2efcd022c
Name:           qaccessibilityclient-qt5
Summary:        Accessibility client library for Qt5
Version:        0.6.0
Release:        1%{?dist}
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/libraries/libqaccessibilityclient
Source0:        https://invent.kde.org/libraries/libqaccessibilityclient/-/archive/v%{version}/libqaccessibilityclient-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libqaccessibilityclient-v%{version}
%oreon_prep
%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qaccessibilityclient-qt5-devel -f %{oreon_filedir}/qaccessibilityclient-qt5-devel.list

%changelog

%autochangelog
