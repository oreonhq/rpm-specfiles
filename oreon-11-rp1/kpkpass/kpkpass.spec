%global source0_hash f916bdc37c11740cc527ee76a1326d3457ed9bf153d609cdb5ea7bb581885df9

Name:    kpkpass
Version: 25.12.3
Release: 1%{?dist}
Summary: Library to deal with Apple Wallet pass files

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Qml)

BuildRequires:  cmake(KF6Archive)

BuildRequires:  qt6-qtbase-devel

BuildRequires:  pkgconfig(shared-mime-info)
%if "%(pkg-config --modversion shared-mime-info 2> /dev/null || echo 2.1)" < "2.2"
%global mime 1
%endif

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Archive)
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

%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/org_kde_%{name}.*
%if 0%{?mime}
%{_kf6_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%endif
%{_kf6_libdir}/libKPim6PkPass.so.*
%{_kf6_qmldir}/org/kde/pkpass/
%{_datadir}/mime/packages/application-vnd-apple-pkpasses.xml

%files devel
%{_includedir}/KPim6/KPkPass/
%{_kf6_libdir}/libKPim6PkPass.so
%{_kf6_libdir}/cmake/KPim6PkPass/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
