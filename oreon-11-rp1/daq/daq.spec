%global source0_hash d1f6709bc5dbddee3fdf170cdc1e49fb926e2031d4869ecf367a8c47efc87279
%global upstream_name daq
%if 0%{?el7}
ExclusiveArch:	x86_64 aarch64
%endif
Summary:        Data Acquisition Library
Name:		daq
Version:	2.0.7
Release:        1%{?dist}
License:	GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:		https://www.snort.org
Source0:        https://www.snort.org/downloads/snort/%{name}-%{version}.tar.gz
%{!?_licensedir: %global license %doc}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libdnet-devel
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Snort 2.9 introduces the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to libpcap functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.

%package modules
Summary:	Dynamic DAQ modules
%description modules
Dynamic DAQ modules.

%package devel
Summary:	Development libraries and headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries and headers for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{version}
autoreconf -ivf -Wobsolete

%build

export CFLAGS="$(echo %{__global_cflags} -Wno-incompatible-pointer-types)"
%{configure} --enable-static=no
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete -print
find $RPM_BUILD_ROOT -type f -name "*.a" -delete -print
%ldconfig_scriptlets
%oreon_autofiles daq-modules usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles daq-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n daq-modules -f %{oreon_filedir}/daq-modules.list
%files -n daq-devel -f %{oreon_filedir}/daq-devel.list

%changelog

%autochangelog
