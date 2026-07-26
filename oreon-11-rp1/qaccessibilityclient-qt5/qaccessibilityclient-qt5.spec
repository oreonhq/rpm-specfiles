%global source0_hash 1e3261a9c90af466fb1835749ff6ea94052e829d71b421bbbccd5fd2efcd022c

Name:           qaccessibilityclient-qt5
Summary:        Accessibility client library for Qt5
Version:        0.6.0
Release:        %autorelease
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/libraries/libqaccessibilityclient
Source0:        %{url}/-/archive/v%{version}/libqaccessibilityclient-v%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libqaccessibilityclient-v%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README.md
%license LICENSES/*
%{_libdir}/libqaccessibilityclient-qt5.so.0*
%{_datadir}/qlogging-categories5/libqaccessibilityclient.categories

%files devel
%{_includedir}/QAccessibilityClient/
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient-qt5.so

%changelog
%autochangelog
