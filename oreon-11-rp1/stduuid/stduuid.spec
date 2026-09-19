%global source0_hash b1176597e789531c38481acbbed2a6894ad419aab0979c10410d59eb0ebf40d3

# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/mariusbancila/stduuid
Version:        1.2.3
%forgemeta

Name:           stduuid
Release:        %autorelease
Summary:        A C++17 cross-platform implementation for UUIDs
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         https://github.com/mariusbancila/stduuid/pull/84.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

%description
stduuid is a C++17 cross-platform single-header library implementation for
universally unique identifiers, simply know as either UUID or GUID (mostly on
Windows). A UUID is a 128-bit number used to uniquely identify information in
computer systems, such as database table keys, COM interfaces, classes and type
libraries, and many others.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUUID_USING_CXX20_SPAN=ON \

%cmake_build

%install
%cmake_install

rm %{buildroot}%{_libdir}/cmake/stduuid/FindLibuuid.cmake

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/uuid.h
%{_libdir}/cmake/stduuid/

%changelog
%autochangelog
