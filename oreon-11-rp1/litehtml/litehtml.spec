%global source0_hash none

Name:           litehtml
Version:        0.10
Release:        1%{?dist}
Summary:        Fast and lightweight HTML/CSS rendering engine

License:        BSD-3-Clause
URL:            https://github.com/litehtml/litehtml
Source0:        https://github.com/litehtml/litehtml/archive/v%{version}/%{name}-%{version}.tar.gz
# Downstream patch
# The Fedora gumbo-parser package does not contain a cmake module,
# so don't look for it
Patch0:         litehtml_gumbo.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  gumbo-parser-devel
BuildRequires:  make
%if 0%{?rhel} && 0%{?rhel} < 10
BuildRequires:  /usr/bin/xxd
%else
BuildRequires:  xxd
%endif


%description
litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support.
Note that litehtml itself does not draw any text, pictures or other graphics
and that litehtml does not depend on any image/draw/font library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gumbo-parser-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Ensure no bundled gumbo and xxd are used
rm -rf src/gumbo
rm -rf xxd

# Since 1.17.0, gtest requires C++17 or later
sed -r -i 's/(CXX_STANDARD[[:blank:]]+)11/\117/' CMakeLists.txt


%build
%cmake -DBUILD_TESTING=ON -DEXTERNAL_GUMBO=ON -DEXTERNAL_GTEST=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}


%changelog
%autochangelog

