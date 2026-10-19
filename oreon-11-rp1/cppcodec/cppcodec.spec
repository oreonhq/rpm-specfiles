%global source0_hash 0edaea2a9d9709d456aa99a1c3e17812ed130f9ef2b5c2d152c230a5cbc5c482
%global debug_package %{nil}
Name:           cppcodec
Version:        0.2
Release:        1%{?dist}
Summary:        Header-only C++11 library to encode/decode base64/base64url/base32/base32hex/hex
License:        MIT
URL:            https://github.com/tplgy/cppcodec
Source0:        https://github.com/tplgy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description    devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# No bundled catch
rm -vrf test/catch

%build

%cmake -DBUILD_TESTING=TRUE
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
