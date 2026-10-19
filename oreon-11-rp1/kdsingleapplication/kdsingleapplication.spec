%global source0_hash none
%bcond qt5 1
%bcond qt6 1
%bcond docs %{undefined flatpak}
%bcond test 1
%global forgeurl https://github.com/KDAB/KDSingleApplication/
%global soversion 1.2
%global cmake_args -DKDSingleApplication_TESTS=true
%if %{with docs}
%global cmake_args %cmake_args -DKDSingleApplication_DOCS=true
%endif
Name:           kdsingleapplication
Version:        1.2.1
Release:        1%{?dist}
Summary:        KDAB's helper class for single-instance policy applications
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgeurl}archive/v%{version}/KDSingleApplication-%{version}.tar.gz
License:        MIT
%if %{with qt5}
%if %{with docs}
%endif
%endif
%if %{with qt6}
%if %{with docs}
%endif
%endif
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DocTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%if %{with qt5}
%global _vpath_builddir build-qt5
PATH=%{_qt5_libexecdir}":$PATH" %cmake %cmake_args -DKDSingleApplication_QT6=false \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%{_qt5_archdatadir}/mkspecs/modules
%cmake_build
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
PATH=%{_qt6_libexecdir}":$PATH" %cmake %cmake_args -DKDSingleApplication_QT6=true \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%{_qt6_archdatadir}/mkspecs/modules
%cmake_build
%endif
%install
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake_install
%if %{with docs}
install -d %{buildroot}%{_qt5_docdir}
pushd %{buildroot}%{_docdir}
for file in KDSingleApplication/*.{qch,tags}; do
    ln -s "../$file" %{buildroot}%{_qt5_docdir}
done
popd
%endif
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake_install
%if %{with docs}
install -d %{buildroot}%{_qt6_docdir}
pushd %{buildroot}%{_docdir}
for file in KDSingleApplication-qt6/*.{qch,tags}; do
    ln -s "../$file" %{buildroot}%{_qt6_docdir}
done
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%endif
%if %{with test}
%check

%if %{with qt5}
%global _vpath_builddir build-qt5
%ctest
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
%ctest
%endif
%endif
%if %{with qt5}
%package qt5
Summary:      KDAB's helper class for single-instance policy applications (Qt5)
%description qt5

%package qt5-devel
Summary:      Development files for %{name}-qt5
Requires:     %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt5Core)
Requires:     cmake(Qt5Network)
Requires:     cmake(Qt5Widgets)
%if %{with docs}
Recommends:   %{name}-qt5-doc
%endif
%description qt5-devel
The %{name}-qt5-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt5.

%package qt5-doc
Summary:      Developer Documentation files for %{name}-qt5
BuildArch:    noarch
%description qt5-doc
Developer Documentation files for %{name}-qt5 for use
with KDevelop or QtCreator.

%package qt6
Summary:      KDAB's helper class for single-instance policy applications (Qt6)
%description qt6

%package qt6-devel
Summary:      Development files for %{name}-qt6
Requires:     %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt6Core)
Requires:     cmake(Qt6Network)
Requires:     cmake(Qt6Widgets)
%if %{with docs}
Recommends:   %{name}-qt6-doc
%endif
%description qt6-devel
The %{name}-qt6-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt6.

%package qt6-doc
Summary:      Developer Documentation files for %{name}-qt6
BuildArch:    noarch
%description qt6-doc
Developer Documentation files for %{name}-qt6 for use
with KDevelop or QtCreator.

%files -f %{oreon_filedir}/main.list
%files -n kdsingleapplication-qt5 -f %{oreon_filedir}/kdsingleapplication-qt5.list
%files -n kdsingleapplication-qt5-devel -f %{oreon_filedir}/kdsingleapplication-qt5-devel.list
%files -n kdsingleapplication-qt5-doc -f %{oreon_filedir}/kdsingleapplication-qt5-doc.list
%files -n kdsingleapplication-qt6 -f %{oreon_filedir}/kdsingleapplication-qt6.list
%files -n kdsingleapplication-qt6-devel -f %{oreon_filedir}/kdsingleapplication-qt6-devel.list
%files -n kdsingleapplication-qt6-doc -f %{oreon_filedir}/kdsingleapplication-qt6-doc.list

%changelog

%autochangelog
%endif
