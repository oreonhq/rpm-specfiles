%global source0_hash c5ec9e3ec53a0a913f81504e202c7bfefbe9c070b7f5599c5e13a6c75d6af913

Name:           ilbc
Version:        3.0.4
Release:        %autorelease
Summary:        Internet Low Bitrate Codec

License:        BSD-3-Clause
URL:            https://github.com/TimothyGu/libilbc
Source0:        https://github.com/TimothyGu/libilbc/archive/refs/tags/v%{version}.tar.gz#/libilbc-%{version}.tar.gz

Patch0:         ilbc-flags.patch
Patch1:         ilbc-s390.patch

BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
iLBC is a speech codec suitable for robust voice communication over IP.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libilbc-%{version}
sed -r -i 's/(set\(CMAKE_CXX_STANDARD[[:blank:]]+)14\b/\117/' CMakeLists.txt

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
rm -fr %{buildroot}%{_docdir}/libilbc

%files
%doc README.md NEWS.md
%license COPYING
%{_libdir}/lib%{name}.so.3
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_bindir}/%{name}_test
%{_includedir}/%{name}.h
%{_includedir}/%{name}_export.h
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
