%global source0_hash 43da83f0c6357c391bd3180ea4712e286f92a3af185d31871b21341cbbf59352
Name:           kdsoap
Version:        2.3.0
Release:        1%{?dist}
Summary:        A Qt-based client-side and server-side SOAP component
License:        MIT
URL:            https://github.com/KDAB/KDSoap
Source0:        https://codeload.github.com/KDAB/KDSoap/tar.gz/refs/tags/kdsoap-%{version}#/kdsoap-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  qt6-doc-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
%description

For more information, see
https://www.kdab.com/development-resources/qt-tools/kd-soap/

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-common%{?_isa} = %{version}-%{release}
%description    devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%package     -n kdsoap6
Summary:        Qt 6 version of %{name}
%description -n kdsoap6
KDSoap can be used to create client applications for web services
and also provides the means to create web services without the need
for any further component such as a dedicated web server.

%package     -n kdsoap6-devel
Summary:        Development files for kdsoap6
Requires:       kdsoap6%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-common%{?_isa} = %{version}-%{release}
%description -n kdsoap6-devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%package        devel-common
Summary:        Header files and other common development files for kdsoap and kdsoap6
%description    devel-common
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir KDSoap-kdsoap-%{version}
%oreon_prep
%build

%global _vpath_builddir %{_target_platform}-qt5
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DKDSoap_EXAMPLES=false -DKDSoap_QT6=OFF
%cmake_build
%global _vpath_builddir %{_target_platform}-qt6
export PATH=%{_qt6_libexecdir}:$PATH
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DKDSoap_EXAMPLES=false -DKDSoap_QT6=ON -DKDSoap_DOCS=ON
%cmake_build
%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
mkdir -p %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_docdir}/KDSoap-qt6/*.qch %{buildroot}%{_qt6_docdir}/
mv %{buildroot}%{_docdir}/KDSoap-qt6/*.tags %{buildroot}%{_qt6_docdir}/
rm -rf %{buildroot}%{_datarootdir}/doc/KDSoap{,-qt6}
%oreon_autofiles kdsoap6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles kdsoap6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%global _vpath_builddir %{_target_platform}-qt5
%ctest
%global _vpath_builddir %{_target_platform}-qt6
%ctest
%files -f %{oreon_filedir}/main.list
%files -n kdsoap-devel -f %{oreon_filedir}/kdsoap-devel.list
%files -n kdsoap6 -f %{oreon_filedir}/kdsoap6.list
%files -n kdsoap6-devel -f %{oreon_filedir}/kdsoap6-devel.list
%files -n kdsoap-devel-common -f %{oreon_filedir}/kdsoap-devel-common.list
%files -n kdsoap-doc -f %{oreon_filedir}/kdsoap-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0-1
- Import
