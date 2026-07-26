%global source0_hash 55a090fc2b46ab44d0dde562a91fe5fc15445a3caedfaedda89fe3925da4705a

# This is a header only library
%global debug_package %{nil}

Name:           plog
Version:        1.1.10
Release:        7%{?dist}
Summary:        Portable, simple and extensible C++ logging library

License:        MIT
URL:            https://github.com/SergiusTheBest/plog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%global _description %{expand:
Plog is a C++ logging library that is designed to be as simple,
small and flexible as possible. It is created as an alternative
to existing large libraries and provides some unique features
as CSV log format and wide string support.}

%description %{_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DPLOG_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

# Delete wrongly installed doc content, we'll docify later
rm -rv %{buildroot}%{_datadir}/doc/%{name}

%check
%ctest

%files devel
%license LICENSE
%doc README.md doc
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
