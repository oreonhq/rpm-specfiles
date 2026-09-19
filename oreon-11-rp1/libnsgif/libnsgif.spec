%global source0_hash 6014c842f61454d2f5a0f8243d7a8d7bde9b7da3ccfdca2d346c7c0b2c4c061b

%global abi_ver 1

Name:           libnsgif
Version:        1.0.0
Release:        %autorelease
Summary:        Decoding library for the GIF image file format
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libnsgif/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netsurf-buildsystem

%description
Libnsgif is a decoding library for the GIF image file format written in C.
It was developed as part of the NetSurf project.

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

%check
%make_build test %{make_vars}

%files
%license COPYING
%{_libdir}/%{name}.so.%{abi_ver}{,.*}

%files devel
%doc README.md
%{_includedir}/nsgif.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
