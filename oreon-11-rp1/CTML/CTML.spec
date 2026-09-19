%global source0_hash e13b3bb04903f47b90b286f8a4695232179e28474a0a33f1a3f333552338d132

%global debug_package %{nil}

%global common_description %{expand:
CTML is a C++ HTML document constructor, that was designed to be simple to use
and implement. Has no dependencies on any other projects, only the C++ standard
library.}

Name:           CTML
Version:        2.0.0
Release:        %autorelease
Summary:        C++ HTML document constructor only depending on the standard library

License:        MIT
URL:            https://github.com/tinfoilboy/CTML
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  catch2-devel

%description
%{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Replace bundled copy of catch with the packaged one
ln -sf %{_includedir}/catch2/catch.hpp tests

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} include/ctml.hpp

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}

%changelog
%autochangelog
