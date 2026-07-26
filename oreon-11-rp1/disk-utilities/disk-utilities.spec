%global source0_hash 602ed055b371a310ea70599b0fbb7a46536381431eaa3a0c1c7a4e168c5bc93c

# IPF support requires libcapsimage which is not distributable in Fedora
%bcond_with ipf

Name:           disk-utilities
Version:        2021.03.20
Release:        11%{?dist}
Summary:        Utilities for ripping, dumping, analysing, and modifying disk images

License:        Unlicense
URL:            https://github.com/keirf/Disk-Utilities
Source0:        %{url}/archive/%{version}/Disk-Utilities-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
%if %{with ipf}
BuildRequires:  libcapsimage-devel
%endif

%description
Disk Utilities is a collection of utilities for ripping, dumping, analysing,
and modifying disk images.

%package -n     libdisk
Summary:        A library for converting and manipulating disk images

%description -n libdisk
libdisk is a library for converting and manipulating disk images. It can
create disk images in a range of formats from Kryoflux STREAM and SPS/IPF
images (among others), and then allow these to be accessed and modified.

%package -n     libdisk-devel
Summary:        Development files for libdisk
Requires:       libdisk%{?_isa} = %{version}-%{release}

%description -n libdisk-devel
The libdisk-devel package contains libraries and header files for
developing applications that use libdisk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Disk-Utilities-%{version}

%build
%set_build_flags
%if %{with ipf}
export caps=y
%endif
%make_build

%install
export PREFIX="%{buildroot}%{_prefix}"
%if %{with ipf}
export caps=y
%endif
%make_install LIBDIR="%{buildroot}%{_libdir}"

%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/disk-analyse

%files -n libdisk
%license COPYING
%{_libdir}/libdisk.so.0*

%files -n libdisk-devel
%{_includedir}/libdisk
%{_libdir}/libdisk.so

%changelog
%autochangelog
