%global source0_hash 8b3ac4e7620e7ffe04deaae9562a37e1e1a375cf589eec06ee3e7a04ea5c9fcc

Name:           mathex
Version:        0.3b
Release:        32%{?dist}
Summary:        C++ library to parse/evaluate mathematical expressions

# Exceptions apply to static linking, see license.txt
License:        LGPL-2.1-or-later WITH Qwt-exception-1.0
URL:            http://sscilib.sourceforge.net/
Source0:        http://sourceforge.net/projects/sscilib/files/%{name}/%{name}-0.3-b.zip
Source1:        CMakeLists.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
C++ library to parse/evaluate mathematical expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}
cp %{SOURCE1} .
sed -i 's|\r||g' changelog.txt license.txt lesser.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc changelog.txt
%license license.txt lesser.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
