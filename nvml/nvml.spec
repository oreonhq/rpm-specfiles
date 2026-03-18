
# rpmbuild options:
#   --with | --without ndctl

# disable 'make check' on all cases
%define _skip_check 1

# do not terminate build if files in the $RPM_BUILD_ROOT
# directory are not found in %%files (without fabric case)
%define _unpackaged_files_terminate_build 0

# suse check
%if %{defined suse_version}
	%define dist .suse%{suse_version}
%endif

# by default build with ndctl, unless explicitly disabled
%bcond_without ndctl

# by default build without pmemcheck, unless explicitly enabled
# pmemcheck is not packaged by Fedora
%bcond_with pmemcheck

%if 0%{?rhel}
%bcond_with pandoc
%else
%bcond_without pandoc
%endif

%define min_ndctl_ver 60.1
%define upstreamversion 2.1.0

Name:		nvml
Version:	%{upstreamversion}
Release:	5%{?dist}
Summary:	Persistent Memory Development Kit (formerly NVML)
License:	BSD-3-Clause
URL:		http://pmem.io/pmdk

Source0:	https://github.com/pmem/pmdk/releases/download/%{upstreamversion}/pmdk-%{upstreamversion}.tar.gz
#Patch0:		0001-test-don-t-print-the-address-of-a-FILE-after-fclose.patch


BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	glibc-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	man
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:  cmake

%if %{with ndctl}
BuildRequires:	ndctl-devel >= %{min_ndctl_ver}
BuildRequires:	daxctl-devel >= %{min_ndctl_ver}
BuildRequires:  ndctl
%endif

%if %{with pandoc}
BuildRequires:	groff
BuildRequires:	pandoc
%endif

# for tests
BuildRequires:	gdb
BuildRequires:	bc
BuildRequires:	libunwind-devel
#BuildRequires:	valgrind

# Debug variants of the libraries should be filtered out of the provides.
%global __provides_exclude_from ^%{_libdir}/pmdk_debug/.*\\.so.*$

# By design, PMDK does not support any 32-bit architecture.
# Due to dependency on some inline assembly, PMDK can be compiled only
# on these architectures:
# - x86_64
# - ppc64le (experimental)
# - aarch64 (unmaintained, supporting hardware doesn't exist?)
# - riscv64
#
# Other 64-bit architectures could also be supported, if only there is
# a request for that, and if somebody provides the arch-specific
# implementation of the low-level routines for flushing to persistent
# memory.

# https://bugzilla.redhat.com/show_bug.cgi?id=1340634
# https://bugzilla.redhat.com/show_bug.cgi?id=1340635
# https://bugzilla.redhat.com/show_bug.cgi?id=1340637

ExclusiveArch: x86_64 ppc64le

%description
The Persistent Memory Development Kit is a collection of libraries for
using memory-mapped persistence, optimized specifically for persistent memory.


%package -n libpmem
Summary: Low-level persistent memory support library
%description -n libpmem
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided.  This package provides the v1 API.

%files -n libpmem
%dir %{_datadir}/pmdk
%{_libdir}/libpmem.so.*
%{_datadir}/pmdk/pmdk.magic
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmem-devel
Summary: Development files for the low-level persistent memory library
Requires: libpmem = %{version}-%{release}
%description -n libpmem-devel
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v1 API.

This library is provided for software which tracks every store to
pmem and needs to flush those changes to durability. Most developers
will find higher level libraries like libpmemobj to be much more
convenient.

%files -n libpmem-devel
%{_libdir}/libpmem.so
%{_libdir}/pkgconfig/libpmem.pc
%{_includedir}/libpmem.h
%if %{with pandoc}
%{_mandir}/man7/libpmem.7.gz
%{_mandir}/man3/pmem_*.3.gz
%{_mandir}/man5/pmem_ctl.5.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmem-debug
Summary: Debug variant of the low-level persistent memory library
Requires: libpmem = %{version}-%{release}
%description -n libpmem-debug
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v1 API.

This sub-package contains debug variant of the library, providing
run-time assertions and trace points. The typical way to access the
debug version is to set the environment variable LD_LIBRARY_PATH to
/usr/lib64/pmdk_debug.

%files -n libpmem-debug
%dir %{_libdir}/pmdk_debug
%{_libdir}/pmdk_debug/libpmem.so
%{_libdir}/pmdk_debug/libpmem.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmem2
Summary: Low-level persistent memory support library
%description -n libpmem2
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v2 API.

%files -n libpmem2
%dir %{_datadir}/pmdk
%{_libdir}/libpmem2.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmem2-devel
Summary: Development files for the low-level persistent memory library
Requires: libpmem = %{version}-%{release}
%description -n libpmem2-devel
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v2 API.

This library is provided for software which tracks every store to
pmem and needs to flush those changes to durability. Most developers
will find higher level libraries like libpmemobj to be much more
convenient.

%files -n libpmem2-devel
%{_libdir}/libpmem2.so
%{_libdir}/pkgconfig/libpmem2.pc
%{_includedir}/libpmem2.h
%{_includedir}/libpmem2/*.h
%if %{with pandoc}
%{_mandir}/man7/libpmem2*7.gz
%{_mandir}/man3/pmem2_*.3.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmem2-debug
Summary: Debug variant of the low-level persistent memory library
Requires: libpmem = %{version}-%{release}
%description -n libpmem2-debug
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v2 API.

This sub-package contains debug variant of the library, providing
run-time assertions and trace points. The typical way to access the
debug version is to set the environment variable LD_LIBRARY_PATH to
/usr/lib64/pmdk_debug.

%files -n libpmem2-debug
%dir %{_libdir}/pmdk_debug
%{_libdir}/pmdk_debug/libpmem2.so
%{_libdir}/pmdk_debug/libpmem2.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md

%package -n libpmemobj
Summary: Persistent Memory Transactional Object Store library
Requires: libpmem >= %{version}-%{release}
%description -n libpmemobj
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming.

%files -n libpmemobj
%{_libdir}/libpmemobj.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmemobj-devel
Summary: Development files for the Persistent Memory Transactional Object Store library
Requires: libpmemobj = %{version}-%{release}
Requires: libpmem-devel = %{version}-%{release}
%description -n libpmemobj-devel
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming. Developers new to persistent memory
probably want to start with this library.

%files -n libpmemobj-devel
%{_libdir}/libpmemobj.so
%{_libdir}/pkgconfig/libpmemobj.pc
%{_includedir}/libpmemobj.h
%dir %{_includedir}/libpmemobj
%{_includedir}/libpmemobj/*.h
%if %{with pandoc}
%{_mandir}/man7/libpmemobj.7.gz
%{_mandir}/man5/poolset.5.gz
%{_mandir}/man3/pmemobj_*.3.gz
%{_mandir}/man3/pobj_*.3.gz
%{_mandir}/man3/oid_*.3.gz
%{_mandir}/man3/toid*.3.gz
%{_mandir}/man3/direct_*.3.gz
%{_mandir}/man3/d_r*.3.gz
%{_mandir}/man3/tx_*.3.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmemobj-debug
Summary: Debug variant of the Persistent Memory Transactional Object Store library
Requires: libpmemobj = %{version}-%{release}
%description -n libpmemobj-debug
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming. Developers new to persistent memory
probably want to start with this library.

This sub-package contains debug variant of the library, providing
run-time assertions and trace points. The typical way to access the
debug version is to set the environment variable LD_LIBRARY_PATH to
/usr/lib64/pmdk_debug.

%files -n libpmemobj-debug
%dir %{_libdir}/pmdk_debug
%{_libdir}/pmdk_debug/libpmemobj.so
%{_libdir}/pmdk_debug/libpmemobj.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmempool
Summary: Persistent Memory pool management library
Requires: libpmem >= %{version}-%{release}
%description -n libpmempool
The libpmempool library provides a set of utilities for off-line
administration, analysis, diagnostics and repair of persistent memory
pools created by libpmemobj libraries.

%files -n libpmempool
%{_libdir}/libpmempool.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmempool-devel
Summary: Development files for Persistent Memory pool management library
Requires: libpmempool = %{version}-%{release}
Requires: libpmem-devel = %{version}-%{release}
%description -n libpmempool-devel
The libpmempool library provides a set of utilities for off-line
administration, analysis, diagnostics and repair of persistent memory
pools created by libpmemobj libraries.

%files -n libpmempool-devel
%{_libdir}/libpmempool.so
%{_libdir}/pkgconfig/libpmempool.pc
%{_includedir}/libpmempool.h
%if %{with pandoc}
%{_mandir}/man7/libpmempool.7.gz
%{_mandir}/man5/poolset.5.gz
%{_mandir}/man3/pmempool_*.3.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n libpmempool-debug
Summary: Debug variant of the Persistent Memory pool management library
Requires: libpmempool = %{version}-%{release}
%description -n libpmempool-debug
The libpmempool library provides a set of utilities for off-line
administration, analysis, diagnostics and repair of persistent memory
pools created by libpmemobj libraries.

This sub-package contains debug variant of the library, providing
run-time assertions and trace points. The typical way to access the
debug version is to set the environment variable LD_LIBRARY_PATH to
/usr/lib64/pmdk_debug.

%files -n libpmempool-debug
%dir %{_libdir}/pmdk_debug
%{_libdir}/pmdk_debug/libpmempool.so
%{_libdir}/pmdk_debug/libpmempool.so.*
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%package -n pmempool
Summary: Utilities for Persistent Memory
Requires: libpmem >= %{version}-%{release}
Requires: libpmemobj >= %{version}-%{release}
Requires: libpmempool >= %{version}-%{release}
Obsoletes: nvml-tools < %{version}-%{release}
%description -n pmempool
The pmempool is a standalone utility for management and off-line analysis
of Persistent Memory pools created by PMDK libraries. It provides a set
of utilities for administration and diagnostics of Persistent Memory pools.
The pmempool may be useful for troubleshooting by system administrators
and users of the applications based on PMDK libraries.

%files -n pmempool
%{_bindir}/pmempool
%if %{with pandoc}
%{_mandir}/man1/pmempool.1.gz
%{_mandir}/man1/pmempool-*.1.gz
%endif
%config(noreplace) %{_sysconfdir}/bash_completion.d/pmempool
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md


%if %{with ndctl}

%package -n daxio
Summary: Perform I/O on Device DAX devices or zero a Device DAX device
Requires: libpmem >= %{version}-%{release}
%description -n daxio
The daxio utility performs I/O on Device DAX devices or zero
a Device DAX device.  Since the standard I/O APIs (read/write) cannot be used
with Device DAX, data transfer is performed on a memory-mapped device.
The daxio may be used to dump Device DAX data to a file, restore data from
a backup copy, move/copy data to another device or to erase data from
a device.

%files -n daxio
%{_bindir}/daxio
%if %{with pandoc}
%{_mandir}/man1/daxio.1.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md

# _with_ndctl
%endif

%if %{with pmemcheck}
%package -n pmreorder
Summary: Consistency Checker for Persistent Memory
Requires: python3
%description -n pmreorder
The pmreorder tool is a collection of python scripts designed to parse
and replay operations logged by pmemcheck - a persistent memory checking tool.
Pmreorder performs the store reordering between persistent memory barriers -
a sequence of flush-fence operations. It uses a consistency checking routine
provided in the command line options to check whether files are in a consistent state.

%files -n pmreorder
%{_bindir}/pmreorder
%{_datadir}/pmreorder/*.py
%if %{with pandoc}
%{_mandir}/man1/pmreorder.1.gz
%endif
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md

# _with_pmemcheck
%endif

%prep
%setup -q -n pmdk-%{upstreamversion}
#%patch0 -p1


%build
# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%define _lto_cflags %{nil}

# For debug build default flags may be overriden to disable compiler
# optimizations.
CFLAGS="%{optflags}" \
EXTRA_CFLAGS="-Wno-error" \
LDFLAGS="%{?__global_ldflags}" \
%make_build NORPATH=1 %{!?with_pandoc:DOC=n}


# Override LIB_AR with empty string to skip installation of static libraries
%install
%make_install \
	LIB_AR= \
	%{!?with_pandoc:DOC=n} \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	includedir=%{_includedir} \
	mandir=%{_mandir} \
	bindir=%{_bindir} \
	sysconfdir=%{_sysconfdir} \
	docdir=%{_docdir}
mkdir -p %{buildroot}%{_datadir}/pmdk
cp utils/pmdk.magic %{buildroot}%{_datadir}/pmdk/



%check
%if 0%{?_skip_check} == 1
	echo "Check skipped"
%else
	echo "PMEM_FS_DIR=/tmp"                  > src/test/testconfig.sh
	echo "PMEM_FS_DIR_FORCE_PMEM=1"         >> src/test/testconfig.sh
	echo 'TEST_BUILD="debug nondebug"'      >> src/test/testconfig.sh
	echo "TM=1"                             >> src/test/testconfig.sh

	echo "config = {"                        > src/test/testconfig.py
	echo "  'pmem_fs_dir': '/tmp',"         >> src/test/testconfig.py
	echo "  'fs_dir_force_pmem': 1,"        >> src/test/testconfig.py
	echo "  'build': ['debug', 'release']," >> src/test/testconfig.py
	echo "  'tm': 1,"                       >> src/test/testconfig.py
	echo "  'test_type': 'check',"          >> src/test/testconfig.py
	echo "  'fs': 'all',"                   >> src/test/testconfig.py
	echo "  'unittest_log_level': 1,"       >> src/test/testconfig.py
	echo "  'keep_going': False,"           >> src/test/testconfig.py
	echo "  'timeout': '30m',"              >> src/test/testconfig.py
	echo "  'dump_lines': 30,"              >> src/test/testconfig.py
	echo "  'force_enable': None,"          >> src/test/testconfig.py
	echo "  'device_dax_path': [],"         >> src/test/testconfig.py
	echo "  'granularity': 'cacheline',"    >> src/test/testconfig.py
	echo "  'enable_admin_tests': False,"   >> src/test/testconfig.py
	echo "  'fail_on_skip': False,"         >> src/test/testconfig.py
	echo "  'cacheline_fs_dir': '/tmp',"    >> src/test/testconfig.py
	echo "  'force_cacheline': True,"       >> src/test/testconfig.py
	echo "  'granularity': 'cacheline',"    >> src/test/testconfig.py
	echo "}"                                >> src/test/testconfig.py

	rm -f src/test/obj_sync/TEST7
	rm -f src/test/pmemset*/TEST*
	rm -f src/test/rpmemd_dbg/TEST*
	rm -f src/test/rpmemd_log/TEST*
	rm -f src/test/obj_zones/TEST*
	rm -f src/test/ex_libpmemobj/TESTS.py

	# bad on ppc64
	rm -f src/test/obj_ctl_arenas/TEST3 src/test/pmem2_future/TESTS.py

	make pycheck
	make check
%endif

%ldconfig_scriptlets   -n libpmem
%ldconfig_scriptlets   -n libpmem2
%ldconfig_scriptlets   -n libpmemobj
%ldconfig_scriptlets   -n libpmempool


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upstreamversion}-5
- Prepare for Oreon 11 (RP1)
