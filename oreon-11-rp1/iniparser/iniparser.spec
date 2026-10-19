%global source0_hash 7a339779ddb37fafbacbf73b176ce968ef9dc5146831b87aba80a18b68355ed4
Name:          iniparser
Version:       4.3.0
Release:        1%{?dist}
Summary:        C library for parsing "INI-style" files
License:       MIT
URL:           https://gitlab.com/%{name}/%{name}
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
iniParser is an ANSI C library to parse "INI-style" files, often used to
hold application configuration information.

%package devel
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake -DBUILD_TESTS=ON -DBUILD_EXAMPLES=ON
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_bindir}/testrun
rm -rf %{buildroot}%{_bindir}/ressources
rm -rf %{buildroot}%{_docdir}/%{name}/examples
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%{_vpath_builddir}/iniexample
%{_vpath_builddir}/parse test/ressources/good_ini/twisted.ini
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n iniparser-devel -f %{oreon_filedir}/iniparser-devel.list

%changelog

%autochangelog
