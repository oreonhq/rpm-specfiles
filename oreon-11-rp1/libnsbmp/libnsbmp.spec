%global source0_hash 5407a7682a122baaaa5a15b505290e2d37df54c13c5edef4b09d12c862d82293
%global abi_ver 0
Name:           libnsbmp
Version:        0.1.7
Release:        1%{?dist}
Summary:        Decoding library for BMP and ICO image file formats
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libnsbmp/
Source0:        http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netsurf-buildsystem
# /oreon:deps
%description
Libnsbmp is a decoding library for BMP and ICO image file formats written in
C. It was developed as part of the NetSurf project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%global make_vars %{shrink:
    COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
    OPTCFLAGS='' OPTLDFLAGS=''
}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e s@-Werror@@ Makefile

%build

%make_build %{make_vars}
%install
%make_install %{make_vars}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build test %{make_vars}
%files -f %{oreon_filedir}/main.list
%files -n libnsbmp-devel -f %{oreon_filedir}/libnsbmp-devel.list

%changelog

%autochangelog
