%global source0_hash 1eb813c7437b31a87496a1cd3ed79f00746720f5e7e29c79b42c02cb69f36c39
%global source1_hash ed965f2b205e7f7df65b305edfd8c662d8b0ebe4dc3b58109e6ad03d0f5ee233
%bcond bootstrap 0
Name:           llhttp
Version:        9.4.3
%global so_version 9.4
%global previous_so_version 9.2
Release:        1%{?dist}
Summary:        Port of http_parser to llparse
License:        MIT
URL:            https://github.com/nodejs/llhttp
Source0:        https://github.com/nodejs/%{name}/archive/refs/tags/release/v%{version}/%{name}-release-v%{version}.tar.gz
Source1:        https://github.com/nodejs/llhttp/archive/refs/tags/v9.3.1.tar.gz#/llhttp-9.3.1.tar.gz
%if %{with bootstrap}
%if "%{_lib}" == "lib64"
%else
%endif
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
This project is a port of http_parser to TypeScript. llparse is used to
generate the output C source file, which could be compiled and linked with the
embedder's program (like Node.js).

%package devel
Summary:        Development files for llhttp
Requires:       llhttp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The llhttp-devel package contains libraries and header files for
developing applications that use llhttp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n llhttp-release-v%{version}

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
%if %{with bootstrap}
cp -vp %{_libdir}/libllhttp.so.%{previous_so_version}{,.*} \
    %{buildroot}%{_libdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n llhttp-devel -f %{oreon_filedir}/llhttp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.3.1-1
- Prepare for Oreon 11 (RP1)
