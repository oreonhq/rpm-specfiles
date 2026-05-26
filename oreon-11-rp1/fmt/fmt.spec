Name:           fmt
Version:        11.2.0
Release:        %autorelease

License:        MIT
Summary:        Small, safe and fast formatting library for C++
URL:            https://github.com/fmtlib/%{name}
Source0:        https://github.com/fmtlib/fmt/archive/11.2.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 bc23066d87ab3168f27cef3e97d545fa63314f5c79df5ea444d41d56f962c6af
%global source0_file 11.2.0.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/11.2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bc23066d87ab3168f27cef3e97d545fa63314f5c79df5ea444d41d56f962c6af" || { echo "oreon: Source0 SHA256 mismatch for 11.2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
%{_libdir}/lib%{name}.so.11*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.2.0-1
- Prepare for Oreon 11 (RP1)
