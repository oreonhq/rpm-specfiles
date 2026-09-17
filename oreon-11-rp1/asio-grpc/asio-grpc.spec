%global source0_hash e8efeef741c604a816534d5b9dfd600378a884ea3b330e4e448975f74f78355c

Name:           asio-grpc
Version:        2.8.0
Release:        8%{?dist}
Summary:        Asynchronous gRPC with Asio/unified executors
License:        Apache-2.0
URL:            https://github.com/Tradias/asio-grpc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# This is a header-only package
BuildArch:      noarch
BuildRequires:  cmake
# It checks for this but doesn't actually use it.
BuildRequires:  gcc-c++
# These are for the test suite, which uh, doesn't actually build sanely.
# BuildRequires:  zlib-devel
# BuildRequires:  c-ares-devel
# BuildRequires:  openssl-devel
# BuildRequires:  protobuf-devel
# BuildRequires:  re2-devel
# BuildRequires:  boost-devel
# BuildRequires:  liburing-devel
# BuildRequires:  git
# BuildRequires:  doxygen
# BuildRequires:  graphviz
# BuildRequires:  doctest-devel
# BuildRequires:  asio-devel

%description
An Executor, Networking TS and std::execution interface to
grpc::CompletionQueue for writing asynchronous gRPC clients and servers using
C++20 coroutines, Boost.Coroutines, Asio's stackless coroutines, callbacks,
sender/receiver and more.

%package        devel
Summary:        Development files for asio-grpc
Requires:       boost-devel, asio-devel, liburing-devel

%description    devel
The asio-grpc-devel package contains libraries and header files for
developing applications that use asio-grpc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# move cmake files out of an arch specific dir
mkdir -p %{buildroot}%{_datadir}/cmake
mv %{buildroot}/usr/lib*/cmake/asio-grpc %{buildroot}%{_datadir}/cmake/

%check

# %%files

%files devel
%license LICENSE
%doc README.md
%{_datadir}/cmake/asio-grpc/
%{_includedir}/agrpc/

%changelog
%autochangelog
