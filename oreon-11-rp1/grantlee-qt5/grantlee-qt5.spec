%global source0_hash ba288ae9ed37ec0c3622ceb40ae1f7e1e6b2ea89216ad8587f0863d64be24f06
%define apidocs 1
Name:    grantlee-qt5
Summary:        Qt5 string template engine based on the Django template system
Version: 5.3.1
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/steveire/grantlee
Source0:        https://github.com/steveire/grantlee/archive/v%{version}.tar.gz#/grantlee-%{version}.tar.gz
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Source1: macros.grantlee5
Patch0: grantlee-qt5-cpp20-ctor.patch
%global grantlee5_plugins 5.3
%global grantlee5_plugindir %{_libdir}/grantlee/%{grantlee5_plugins}/
Provides: %{name}(%{grantlee5_plugins}) = %{version}-%{release}
%if 0%{?apidocs}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Grantlee is a plug-in based String Template system written
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system,
and the design of Django is reused in Grantlee.

Part of the design of both is that application developers can extend
the syntax by implementing their own tags and filters. For details of
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details of
how to write templates, see the documentation.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: grantlee-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package apidocs
Summary: Grantlee API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir grantlee-%{version}
%oreon_prep
%build

%cmake \
  -DBUILD_TESTS:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=release
%cmake_build
%if 0%{?apidocs}
%cmake_build --target docs
%endif
%install
%cmake_install
%if 0%{?apidocs}
mkdir -p %{buildroot}%{_docdir}/HTML/en/Grantlee5/
cp -prf %{__cmake_builddir}/apidox/* %{buildroot}%{_docdir}/HTML/en/Grantlee5/
%endif
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.grantlee5
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  -e "s|@@GRANTLEE5_PLUGINS@@|%{grantlee5_plugins}|g" \
  -e "s|@@GRANTLEE5_PLUGINDIR@@|%{grantlee5_plugindir}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.grantlee5
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n grantlee-qt5-devel -f %{oreon_filedir}/grantlee-qt5-devel.list
%files -n grantlee-qt5-apidocs -f %{oreon_filedir}/grantlee-qt5-apidocs.list

%changelog

%autochangelog
