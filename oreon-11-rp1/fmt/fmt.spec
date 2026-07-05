%global source0_hash ea7de4299689e12b6dddd392f9896f08fb0777ac7168897a244a6d6085043fea

Name:           fmt
Version:        12.1.0
Release:        1%{?dist}

License:        MIT
Summary:        Small, safe and fast formatting library for C++
URL:            https://github.com/fmtlib/%{name}
Source0:        https://github.com/fmtlib/fmt/archive/refs/tags/%{version}.tar.gz#/fmt-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

# This package replaces the old name of cppformat
Provides:       cppformat = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat < %{?epoch:%{epoch}:}%{version}-%{release}

%description
C++ Format is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# for usage with -DFMT_HEADER_ONLY
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

# This package replaces the old name of cppformat
Provides:       cppformat-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
This package contains the header file for using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DFMT_CMAKE_DIR:STRING=%{_libdir}/cmake/%{name} \
    -DFMT_LIB_DIR:STRING=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc ChangeLog.md README.md
%{_libdir}/lib%{name}.so.12*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
