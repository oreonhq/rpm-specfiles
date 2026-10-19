%global source0_hash b77ef8b961233a100a34da588962a95a2f3b00c9b2dc0ea67100b36ec72128af
%global debug_package %{nil}
Name:           zstr
Version:        1.1.0
Release:        1%{?dist}
Summary:        A C++ header-only ZLib wrapper
License:        MIT
URL:            https://github.com/mateidavid/zstr
VCS :           git:%{url}.git
Source0:        https://github.com/mateidavid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-zlib-ng.patch
ExcludeArch:    %{ix86}
%global _desc %{expand:This C++ header-only library enables the use of C++ standard iostreams to
access ZLib-compressed streams.
For input access (decompression), the compression format is auto-detected, and
multiple concatenated compressed streams are decompressed seamlessly.
For output access (compression), the only parameter exposed by this API is the
compression level.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib-ng)
# /oreon:deps
%description
%_desc

%package devel
Summary:        A C++ header-only ZLib wrapper
BuildArch:      noarch
Requires:       pkgconfig(zlib-ng)
Provides:       %{name}-static = %{version}-%{release}
%description devel
%_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
mkdir -p %{buildroot}%{_includedir}/zstr
install -m 0644 -p src/*.hpp %{buildroot}%{_includedir}/zstr
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n zstr-devel -f %{oreon_filedir}/zstr-devel.list

%changelog

%autochangelog
