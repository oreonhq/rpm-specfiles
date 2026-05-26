%global __remake_config 0

# FTBFS on i686 with GCC 14 -Werror=incompatible-pointer-types
# https://github.com/ofiwg/libfabric/issues/9763
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%ifarch %{ix86}
%global build_type_safety_c 2
%endif
%endif

Name:           libfabric
Version:        2.3.1
Release:        %autorelease
Summary:        Open Fabric Interfaces

License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/ofiwg/libfabric
Source0:        https://github.com/ofiwg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 2e939f17ce4d30a999d0445f741d3055b19dfd894eff70450e23470fe774f35a
%global source0_file libfabric-2.3.1.tar.bz2
# oreon url source checksums end

%if %{__remake_config}
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnl3-devel
# RDMA not available on 32-bit ARM: #1484155
%ifnarch %{arm}
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
%endif
%ifarch x86_64
%if 0%{?fedora} || (0%{?rhel} >= 7 && 0%{?rhel} < 10)
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  numactl-devel
%endif

%description
OpenFabrics Interfaces (OFI) is a framework focused on exporting fabric
communication services to applications.  OFI is best described as a collection
of libraries and applications used to export fabric services.  The key
components of OFI are: application interfaces, provider libraries, kernel
services, daemons, and test applications.

Libfabric is a core component of OFI.  It is the library that defines and
exports the user-space API of OFI, and is typically the only software that
applications deal with directly.  It works in conjunction with provider
libraries, which are often integrated directly into libfabric.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libfabric-2.3.1.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2e939f17ce4d30a999d0445f741d3055b19dfd894eff70450e23470fe774f35a" || { echo "oreon: Source0 SHA256 mismatch for libfabric-2.3.1.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{name}-%{version}

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --disable-static --disable-silent-rules
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%{_bindir}/fi_info
%{_bindir}/fi_mon_sampler
%{_bindir}/fi_pingpong
%{_bindir}/fi_strerror
%{_libdir}/*.so.1*
%{_mandir}/man1/*.1*

%files devel
%license COPYING
%doc AUTHORS README
# We knowingly share this with kernel-headers and librdmacm-devel
# https://github.com/ofiwg/libfabric/issues/1277
%{_includedir}/rdma/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-1
- Prepare for Oreon 11 (RP1)
