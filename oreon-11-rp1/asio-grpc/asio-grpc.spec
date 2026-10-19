%global source0_hash 441d88fcffdc9136d843706390d68a3dd6e2090513b44f352a04157a4e5aa937
Name:           asio-grpc
Version:        3.7.0
Release:        1%{?dist}
Summary:        Asynchronous gRPC with Asio/unified executors
License:        Apache-2.0
URL:            https://github.com/Tradias/asio-grpc
Source0:        https://github.com/Tradias/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/cmake
mv %{buildroot}/usr/lib*/cmake/asio-grpc %{buildroot}%{_datadir}/cmake/
%oreon_autofiles asio-grpc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n asio-grpc-devel -f %{oreon_filedir}/asio-grpc-devel.list

%changelog

%autochangelog
