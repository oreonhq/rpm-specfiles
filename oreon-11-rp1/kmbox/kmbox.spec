%global source0_hash 088e88b85686374da855215351e0e5248464921c8b546531d91b8dcef952ff93

Name:    kmbox
Version: 25.12.3
Release: 1%{?dist}
Summary: The KMbox Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(KF6Codecs)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Mbox.so.*

%files devel
%{_includedir}/KPim6/KMbox
%{_kf6_libdir}/cmake/KPim6Mbox/
%{_kf6_libdir}/libKPim6Mbox.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
