%global source1_hash 4650b5c20914cebf4bc0455e880daacd7b73986ec106682cfaa7e3a938ab77e9

%global source0_hash 2d44e45b05766d342d3fe19e92d2b039c916a7a83f9e4dff0f9fa15860e140ee

%global framework syndication

%global stable_kf6 stable
%global majmin_ver_kf6 6.30

Name:    kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary: The Syndication Library

# Qt-Commercial-exception-1.0 is also found in the LICENSES folder, but is unused except for tests which we don't use anyway
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Codecs) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6KIO) >= %{version}
Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Syndication.so.*

%files devel
%{_kf6_includedir}/Syndication/
%{_kf6_libdir}/cmake/KF6Syndication/
%{_kf6_libdir}/libKF6Syndication.so


%changelog
%autochangelog
