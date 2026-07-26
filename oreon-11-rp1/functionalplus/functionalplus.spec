%global source0_hash 446c63ac3f2045e7587f694501882a3d7c7b962b70bcc08deacf5777bdaaff8c

%global debug_package %{nil}

Name:           functionalplus
Version:        0.2.24
Release:        %autorelease
Summary:        Functional Programming Library for C++

License:        BSL-1.0
URL:            https://github.com/Dobiasd/FunctionalPlus
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Functional Programming Library for C++. Write concise and readable C++ code.

%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n FunctionalPlus-%{version}
sed '/-Werror/d' -i cmake/warnings.cmake

%build
%cmake -DFunctionalPlus_INSTALL_CMAKEDIR=%{_datadir}/cmake/FunctionalPlus
%cmake_build
%ifnarch %{ix86}
pushd test
%cmake
%cmake_build
popd
%endif

%install
%cmake_install

%check
%ifnarch %{ix86}
pushd test
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/fplus/
%{_datadir}/cmake/FunctionalPlus/

%changelog
%autochangelog
