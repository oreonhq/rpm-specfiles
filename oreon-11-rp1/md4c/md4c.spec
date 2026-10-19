%global source0_hash 353c346f376b87c954a13f3415ede2d51264cc61dc5abcd38ff1d2aa0d059b9e
Version:        0.5.3
Name:           md4c
Release:        1%{?dist}
Summary:        Markdown for C
License:        MIT
URL:            https://github.com/mity/md4c
Source0:        https://github.com/mity/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3
# /oreon:deps
%description
MD4C is Markdown parser implementation in C.

%package        devel
Summary:        Development files for md4c
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The md4c-devel package contains libraries and header files for
developing applications that use md4c.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n md4c-devel -f %{oreon_filedir}/md4c-devel.list

%changelog

%autochangelog

