%global source0_hash 5407a7682a122baaaa5a15b505290e2d37df54c13c5edef4b09d12c862d82293

%global abi_ver 0

Name:           libnsbmp
Version:        0.1.7
Release:        %autorelease
Summary:        Decoding library for BMP and ICO image file formats
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libnsbmp/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netsurf-buildsystem

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

%check
%make_build test %{make_vars}

%files
%license COPYING
%{_libdir}/%{name}.so.%{abi_ver}{,.*}

%files devel
%doc src/README
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
