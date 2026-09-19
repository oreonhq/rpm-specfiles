%global source0_hash 7e5ec6891254c8f00128952ed6b9a73d827539136c3b804563521a0042abe72c

%global debug_package %{nil}
# header only lib

Name:           cpp-jwt
Version:        1.5.1
Release:        3%{?dist}
Summary:        JSON Web Token library for C++

License:        MIT
URL:            https://github.com/arun11299/cpp-jwt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  openssl-devel
BuildRequires:  gtest-devel

%global _description %{expand:
JSON Web Token(JWT) is a JSON based standard (RFC-
7519) for creating assertions or access tokens that consists of some
claims (encoded within the assertion). This assertion can be used in some
kind of bearer authentication mechanism that the server will provide to
clients, and the clients can make use of the provided assertion for
accessing resources.}

%description %{_description}

%package devel
Summary:        %{summary}
Recommends:     cmake
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake # -DCPP_JWT_BUILD_EXAMPLES=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/jwt/
%{_datadir}/cmake/%{name}

%changelog
%autochangelog
