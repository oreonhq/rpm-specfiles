%global source0_hash 3d55d170ebc317e156189ccc927fb48b47841f978172f73c2a711ef5b4647cdc

%global forgeurl https://github.com/ublk-org/ublksrv
%global commit a2f2daa9f02509a008d9304c197f6a2b0da0ad38
Version:       1.6
%forgemeta

Summary:       Userspace block driver server and ublk tool
Name:          ubdsrv
Release:       %autorelease
URL:           %{forgeurl}
Source:        %{forgesource}
License:       LGPLv2+ or MIT

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: autoconf, autoconf-archive, automake, libtool
BuildRequires: liburing-devel >= 2.2
BuildRequires: pkgconf
BuildRequires: git

%description
This package allows you to write Linux block devices in userspace.  It
contains a library which can be linked to programs that implement
Linux userspace block devices, and also the "ublk" program which can
be used to create, list and delete ublk devices.

%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}
Provides:      ublksrv = %{version}-%{release}

%description devel
This package contains development tools for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
autoreconf -f -i
%{configure} --disable-static
make V=1 %{?_smp_mflags}

%install
%{make_install}

# Remove libtool droppings.
rm %{buildroot}%{_libdir}/*.la

%files
%license COPYING COPYING.LGPL LICENSE
%doc README.rst
%{_sbindir}/ublk
%{_sbindir}/ublk.*
%{_sbindir}/ublk_user_id
%{_sbindir}/ublk_chown.sh
%{_sbindir}/ublk_chown_docker.sh
%{_mandir}/man1/ublk.1.gz
%{_libdir}/libublksrv.so.0*

%files devel
%license COPYING COPYING.LGPL LICENSE
%doc README.rst
%{_includedir}/ublksrv_aio.h
%{_includedir}/ublksrv.h
%{_includedir}/ublk_cmd.h
%{_includedir}/ublksrv_utils.h
%{_libdir}/libublksrv.so
%{_libdir}/pkgconfig/ublksrv.pc

%changelog
%autochangelog
