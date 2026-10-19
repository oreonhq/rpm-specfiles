%global source0_hash be8a89df72d01cf062cc9815dd64c9576b4d20910d6d7aee7f0ea26484dc5e76
Name: svgpp
Summary:        SVG handling library for C++
%global debug_package %{nil}
License: BSL-1.0
Version: 1.3.1
Release:        1%{?dist}
URL: https://svgpp.org
Source0:        https://github.com/svgpp/svgpp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: svgpp-exboost-path.patch
%global with_tests 1
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tree
# /oreon:deps
%description
SVG++ is a header-only library for handling SVG files
that can be used with any XML parser.

# -- devel

%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}
Requires: boost-devel
BuildArch: noarch
%description devel
SVG++ is a header-only library for handling SVG files
that can be used with any XML parser.

# -- subpackages end

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mv ./include/exboost ./include/svgpp/exboost

%build

%install
install -m 755 -d %{buildroot}%{_includedir}
cp -a include/svgpp %{buildroot}%{_includedir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if 0%{?with_tests}
%check

export CMAKE_POLICY_VERSION_MINIMUM=3.5
pushd src/test/
%cmake
%cmake_build
./%{__cmake_builddir}/ParserGTest
%endif
%files -f %{oreon_filedir}/main.list
%files -n svgpp-devel -f %{oreon_filedir}/svgpp-devel.list

%changelog

%autochangelog
