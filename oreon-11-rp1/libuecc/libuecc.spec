%global source0_hash 465a6584c991c13fddf36700328c44fee9a3baff9025fb5f232b34d003d715e0

Version:        7
%global forgeurl https://github.com/neocturne/libuecc
%forgemeta

Name:           libuecc
Release:        %autorelease
Summary:        Very small Elliptic Curve Cryptography library

License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  cmake

%description
Very small Elliptic Curve Cryptography library that is well suited for embedded
software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
# TODO: Please submit an issue to upstream (rhbz#2380765)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%files
%doc CHANGELOG README
%license COPYRIGHT
%{_libdir}/%{name}.so.*

%files devel
%doc CHANGELOG README
%license COPYRIGHT
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
