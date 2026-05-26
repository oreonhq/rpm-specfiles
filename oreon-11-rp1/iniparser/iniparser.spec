# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 67575ed032a544d5359610e5f697af786371bbc3eb01311218ef8adfd3e5e329
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:          iniparser
Version:       4.2.6
Release:       4%{?dist}
Summary:       C library for parsing "INI-style" files

License:       MIT
URL:           https://gitlab.com/%{name}/%{name}
Source0:       https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen

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
%oreon_verify_sources
%autosetup -n %{name}-v%{version}

%build
%cmake -DBUILD_TESTS=ON -DBUILD_EXAMPLES=ON
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_bindir}/testrun
rm -rf %{buildroot}%{_bindir}/ressources
rm -rf %{buildroot}%{_docdir}/%{name}/examples

%check
%ctest
%{_vpath_builddir}/iniexample
%{_vpath_builddir}/parse test/ressources/good_ini/twisted.ini

%ldconfig_scriptlets

%files
%doc AUTHORS FAQ*md INSTALL README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libiniparser.so.*

%files devel
%{_libdir}/libiniparser.a
%{_libdir}/libiniparser.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.6-4
- Prepare for Oreon 11 (RP1)
