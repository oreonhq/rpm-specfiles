%global source0_hash 09e2ff033d39baa8b388a2d7fbc5390bfde99ae3b7c67c7daaf7433fbcf0f01e

# Rebuild --with static to enable static subpackages
# This is *not* supported by elfutils maintainers
%bcond_with static

Name: elfutils
Version: 0.194
%global baserelease 5
Release: %{baserelease}%{?dist}
URL: http://elfutils.org/
%global source_url https://sourceware.org/pub/elfutils/%{version}/
License: GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GFDL-1.3-no-invariants-or-later
Source: %{?source_url}%{name}-%{version}.tar.bz2
Source1: elfutils-debuginfod.sysusers
Summary: A collection of utilities and DSOs to handle ELF files and DWARF data

# Needed for isa specific Provides and Requires.
%global depsuffix %{?_isa}%{!?_isa:-%{_arch}}

# eu-stacktrace currently only supports x86_64
%ifarch x86_64
%global enable_stacktrace 1
%else
%global enable_stacktrace 0
%endif

Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}
Requires: elfutils-libs%{depsuffix} = %{version}-%{release}
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}

BuildRequires: gcc
# For libstdc++ demangle support
BuildRequires: gcc-c++

BuildRequires: gettext
BuildRequires: bison
BuildRequires: flex

# Compression support
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel

# For debuginfod
BuildRequires: pkgconfig(libmicrohttpd) >= 0.9.33
BuildRequires: pkgconfig(libcurl) >= 7.29.0
BuildRequires: pkgconfig(sqlite3) >= 3.7.17
BuildRequires: pkgconfig(libarchive) >= 3.1.2
# For debugindod metadata query
BuildRequires: pkgconfig(json-c) >= 0.11

# For tests need to bunzip2 test files.
BuildRequires: bzip2
BuildRequires: zstd
# For the run-debuginfod-find.sh test case in %%check for /usr/sbin/ss etc.
BuildRequires: iproute
BuildRequires: procps
BuildRequires: bsdtar
BuildRequires: curl
# For run-debuginfod-response-headers.sh test case
BuildRequires: socat
# For run-debuginfod-find-metadata.sh
BuildRequires: jq

# For debuginfod rpm IMA verification
BuildRequires: rpm-devel
BuildRequires: ima-evm-utils-devel
BuildRequires: openssl-devel
BuildRequires: rpm-sign

# For eu-stacktrace
%if %{enable_stacktrace}
BuildRequires: sysprof-capture-devel
%endif

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gettext-devel

%global _gnu %{nil}
%global _program_prefix eu-

%global provide_yama_scope      0

%if 0%{?fedora} >= 22 || 0%{?rhel} >= 7
%global provide_yama_scope      1
%endif

%global with_sysusers           0

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global with_sysusers           1
%endif

# Patches

# For s390x... FDO package notes are bogus.
Patch1: elfutils-0.186-fdo-swap.patch

# Prevent assert failure in readelf for some -ggdb3 binaries.
Patch2: elfutils-0.194-alloc-jobs.patch

# Fix const warning from newer GCC.
Patch3: elfutils-0.194-fix-const.patch

# Work around ET_REL files with sh_addr fields set to non-zero
Patch4: elfutils-0.194-sh_addr-non-zero.patch

# Recognize SHT_AARCH64_ATTRIBUTES.
# https://sourceware.org/bugzilla/show_bug.cgi?id=33923
Patch5: elfutils-0.194-aarch64-Recognize-SHT_AARCH64_ATTRIBUTES.patch

%description
Elfutils is a collection of utilities, including stack (to show
backtraces), nm (for listing symbols from object files), size
(for listing the section sizes of an object or archive file),
strip (for discarding symbols), readelf (to see the raw ELF file
structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).

%package libs
Summary: Libraries to handle compiled objects
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-libs%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}
%if %{provide_yama_scope}
Requires: default-yama-scope
%endif
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 20
Recommends: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
%else
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
%endif

%description libs
The elfutils-libs package contains libraries which implement DWARF, ELF,
and machine-specific ELF handling and process introspection.  These
libraries are used by the programs in the elfutils package.  The
elfutils-devel package enables building other programs using these
libraries.

%package devel
Summary: Development libraries to handle compiled objects
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-devel%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-libs%{depsuffix} = %{version}-%{release}
Requires: elfutils-libelf-devel%{depsuffix} = %{version}-%{release}
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 20
Recommends: elfutils-debuginfod-client-devel%{depsuffix} = %{version}-%{release}
%else
Requires: elfutils-debuginfod-client-devel%{depsuffix} = %{version}-%{release}
%endif

%description devel
The elfutils-devel package contains the libraries to create
applications for handling compiled objects.  libdw provides access
to the DWARF debugging information.  libasm provides a programmable
assembler interface.

%if %{with static}
%package devel-static
Summary: Static archives to handle compiled objects
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-devel-static%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-devel%{depsuffix} = %{version}-%{release}
Requires: elfutils-libelf-devel-static%{depsuffix} = %{version}-%{release}

%description devel-static
The elfutils-devel-static package contains the static archives
with the code to handle compiled objects.
%endif

%package libelf
Summary: Library to read and write ELF files
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-libelf%{depsuffix} = %{version}-%{release}
%endif
Obsoletes: libelf <= 0.8.2-2

%description libelf
The elfutils-libelf package provides a DSO which allows reading and
writing ELF files on a high level.  Third party programs depend on
this package to read internals of ELF files.  The programs of the
elfutils package use it also to generate new ELF files.

%package libelf-devel
Summary: Development support for libelf
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-libelf-devel%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}
Obsoletes: libelf-devel <= 0.8.2-2

%description libelf-devel
The elfutils-libelf-devel package contains the libraries to create
applications for handling compiled objects.  libelf allows you to
access the internals of the ELF object file format, so you can see the
different sections of an ELF file.

%if %{with static}
%package libelf-devel-static
Summary: Static archive of libelf
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-libelf-devel-static%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-libelf-devel%{depsuffix} = %{version}-%{release}
Requires: libzstd-static%{depsuffix}

%description libelf-devel-static
The elfutils-libelf-static package contains the static archive
for libelf.
%endif

%if %{provide_yama_scope}
%package default-yama-scope
Summary: Default yama attach scope sysctl setting
License: GPL-2.0-or-later OR LGPL-3.0-or-later
Provides: default-yama-scope
BuildArch: noarch
# For the sysctl_apply macro we need systemd as build requires.
# We also need systemd-sysctl in post to apply the default kernel config.
# But this creates a circular requirement (see below). And it would always
# pull in systemd even in build containers that don't really need it.
# Luckily systemd is normally always installed already. The only times it
# might not is when we do an initial install (and the cyclic dependency
# chain might be broken) or when installing into a container. In the first
# case we'll reboot soon to apply the default kernel config. In the second
# case we really require that the host has the correct kernel config so it
# also is available inside the container. So if we have weak dependencies
# use Recommends (sadly Recommends(post) doesn't exist). This works because
# in all cases that really matter systemd will already be installed. #1599083
BuildRequires: systemd >= 215
%if 0%{?fedora} > 24 || 0%{?rhel} > 7
Recommends: systemd
%else
Requires(post): systemd
%endif

%description default-yama-scope
Yama sysctl setting to enable default attach scope settings
enabling programs to use ptrace attach, access to
/proc/PID/{mem,personality,stack,syscall}, and the syscalls
process_vm_readv and process_vm_writev which are used for
interprocess services, communication and introspection
(like synchronisation, signaling, debugging, tracing and
profiling) of processes.
%endif

%package debuginfod-client
Summary: Library and command line client for build-id HTTP ELF/DWARF server
License: GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later)
%if 0%{!?_isa:1}
Provides: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
%endif
# For debuginfod-find binary
Requires: elfutils-libs%{depsuffix} = %{version}-%{release}
Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}

%package debuginfod-client-devel
Summary: Libraries and headers to build debuginfod client applications
License: GPL-2.0-or-later OR LGPL-3.0-or-later
%if 0%{!?_isa:1}
Provides: elfutils-debuginfod-client-devel%{depsuffix} = %{version}-%{release}
%endif
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}

%package debuginfod
Summary: HTTP ELF/DWARF file server addressed by build-id
License: GPL-3.0-or-later
Requires: elfutils-libs%{depsuffix} = %{version}-%{release}
Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
BuildRequires: systemd
%if %{with_sysusers}
BuildRequires: systemd-rpm-macros
%endif
BuildRequires: make
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%if %{with_sysusers}
%{?sysusers_requires_compat}
%else
Requires(pre): shadow-utils
%endif
# To extract .deb files with a bsdtar (= libarchive) subshell
Requires: bsdtar

%description debuginfod-client
The elfutils-debuginfod-client package contains shared libraries
dynamically loaded from -ldw, which use a debuginfod service
to look up debuginfo and associated data. Also includes a
command-line frontend.

%description debuginfod-client-devel
The elfutils-debuginfod-client-devel package contains the libraries
to create applications to use the debuginfod service.

%description debuginfod
The elfutils-debuginfod package contains the debuginfod binary
and control files for a service that can provide ELF/DWARF
files to remote clients, based on build-id identification.
The ELF/DWARF file searching functions in libdwfl can query
such servers to download those files on demand.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

autoreconf -f -v -i

# In case the above patches added any new test scripts, make sure they
# are executable.
find . -name \*.sh ! -perm -0100 -print | xargs chmod +x

%build
# Remove -Wall from default flags.  The makefiles enable enough warnings
# themselves, and they use -Werror.  Appending -Wall defeats the cases where
# the makefiles disable some specific warnings for specific code.
# But add -Wformat explicitly for use with -Werror=format-security which
# doesn't work without -Wformat (enabled by -Wall).
RPM_OPT_FLAGS="${RPM_OPT_FLAGS/-Wall/}"
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -Wformat"


trap 'cat config.log' EXIT
# dist_debuginfod_url is defined in macros.dist. Fedora and CentOS have
# URLs pointing to their respective servers.  RHEL and Amazon Linux do
# not configure a default server.
%configure CFLAGS="$RPM_OPT_FLAGS" \
%if "%{?dist_debuginfod_url}"
	--enable-debuginfod \
	--enable-debuginfod-urls="%{dist_debuginfod_url}" \
%endif
%if %{enable_stacktrace}
	--enable-stacktrace \
%endif
	--enable-debuginfod-ima-verification \
	--enable-debuginfod-ima-cert-path=%{_sysconfdir}/keys/ima
trap '' EXIT
%make_build

%install
%make_install

chmod +x ${RPM_BUILD_ROOT}%{_prefix}/%{_lib}/lib*.so*
%if %{without static}
# We don't want the static libraries
rm ${RPM_BUILD_ROOT}%{_prefix}/%{_lib}/lib{elf,dw,asm}.a
%endif

%find_lang %{name}

%if %{provide_yama_scope}
install -Dm0644 config/10-default-yama-scope.conf ${RPM_BUILD_ROOT}%{_sysctldir}/10-default-yama-scope.conf
%endif

install -Dm0644 config/debuginfod.service ${RPM_BUILD_ROOT}%{_unitdir}/debuginfod.service
install -Dm0644 config/debuginfod.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/debuginfod
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/cache/debuginfod
touch ${RPM_BUILD_ROOT}%{_localstatedir}/cache/debuginfod/debuginfod.sqlite

%if %{with_sysusers}
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/elfutils-debuginfod.conf
%endif

%check
# Record some build root versions in build.log
uname -r; rpm -q binutils gcc glibc || true

%make_build check || (cat tests/test-suite.log; false)

# Only the latest Fedora and EPEL have these scriptlets,
# older Fedora and plain RHEL don't.
%if 0%{?ldconfig_scriptlets:1}
%ldconfig_scriptlets libs
%ldconfig_scriptlets libelf
%ldconfig_scriptlets debuginfod-client
%else
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%post libelf -p /sbin/ldconfig
%postun libelf -p /sbin/ldconfig
%post debuginfod-client -p /sbin/ldconfig
%postun debuginfod-client -p /sbin/ldconfig
%endif

%if %{provide_yama_scope}
%post default-yama-scope
# Due to circular dependencies might not be installed yet, so double check.
# (systemd -> elfutils-libs -> default-yama-scope -> systemd)
if [ -x /usr/lib/systemd/systemd-sysctl ] ; then
%sysctl_apply 10-default-yama-scope.conf
fi
%endif

%files
%license COPYING COPYING-GPLV2 COPYING-LGPLV3 doc/COPYING-GFDL
%doc README TODO CONTRIBUTING
%{_bindir}/eu-addr2line
%{_bindir}/eu-ar
%{_bindir}/eu-elfclassify
%{_bindir}/eu-elfcmp
%{_bindir}/eu-elfcompress
%{_bindir}/eu-elflint
%{_bindir}/eu-findtextrel
%{_bindir}/eu-make-debug-archive
%{_bindir}/eu-nm
%{_bindir}/eu-objdump
%{_bindir}/eu-ranlib
%{_bindir}/eu-readelf
%{_bindir}/eu-size
%{_bindir}/eu-srcfiles
%{_bindir}/eu-stack
%if %{enable_stacktrace}
%{_bindir}/eu-stacktrace
%endif
%{_bindir}/eu-strings
%{_bindir}/eu-strip
%{_bindir}/eu-unstrip
%{_mandir}/man1/eu-*.1*

%files libs
%license COPYING-GPLV2 COPYING-LGPLV3
%{_libdir}/libasm-%{version}.so
%{_libdir}/libdw-%{version}.so
%{_libdir}/libasm.so.*
%{_libdir}/libdw.so.*

%files devel
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/known-dwarf.h
%{_includedir}/elfutils/libasm.h
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwfl.h
%{_includedir}/elfutils/libdwelf.h
%{_includedir}/elfutils/version.h
%{_includedir}/elfutils/libdwfl_stacktrace.h
%{_libdir}/libasm.so
%{_libdir}/libdw.so
%{_libdir}/pkgconfig/libdw.pc

%if %{with static}
%files devel-static
%{_libdir}/libdw.a
%{_libdir}/libasm.a
%endif

%files -f %{name}.lang libelf
%license COPYING-GPLV2 COPYING-LGPLV3
%{_libdir}/libelf-%{version}.so
%{_libdir}/libelf.so.*

%files libelf-devel
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%{_libdir}/libelf.so
%{_libdir}/pkgconfig/libelf.pc
%{_mandir}/man3/elf_*.3*
%{_mandir}/man3/elf32_*.3*
%{_mandir}/man3/elf64_*.3*
%{_mandir}/man3/gelf_*.3*
%{_mandir}/man3/libelf.3*

%if %{with static}
%files libelf-devel-static
%{_libdir}/libelf.a
%endif

%if %{provide_yama_scope}
%files default-yama-scope
%{_sysctldir}/10-default-yama-scope.conf
%endif

%files debuginfod-client
%{_libdir}/libdebuginfod-%{version}.so
%{_libdir}/libdebuginfod.so.*
%{_bindir}/debuginfod-find
%{_mandir}/man1/debuginfod-find.1*
%{_mandir}/man7/debuginfod*.7*
%config(noreplace) %{_sysconfdir}/profile.d/*
%if "%{?dist_debuginfod_url}"
%config(noreplace) %{_sysconfdir}/debuginfod/*
%config(noreplace) %{_datadir}/fish/vendor_conf.d/*
%endif

%files debuginfod-client-devel
%{_libdir}/pkgconfig/libdebuginfod.pc
%{_mandir}/man3/debuginfod_*.3*
%{_includedir}/elfutils/debuginfod.h
%{_libdir}/libdebuginfod.so

%files debuginfod
%{_bindir}/debuginfod
%config(noreplace) %{_sysconfdir}/sysconfig/debuginfod
%{_unitdir}/debuginfod.service
%if %{with_sysusers}
%{_sysusersdir}/elfutils-debuginfod.conf
%endif
%{_mandir}/man8/debuginfod*.8*


%dir %attr(0700,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod
%ghost %attr(0600,debuginfod,debuginfod) %{_localstatedir}/cache/debuginfod/debuginfod.sqlite

%pre debuginfod
%if %{with_sysusers}
%sysusers_create_compat %{SOURCE1}
%else
getent group debuginfod >/dev/null || groupadd -r debuginfod
getent passwd debuginfod >/dev/null || \
    useradd -r -g debuginfod -d /var/cache/debuginfod -s /sbin/nologin \
            -c "elfutils debuginfo server" debuginfod
exit 0
%endif

%post debuginfod
%systemd_post debuginfod.service

%postun debuginfod
%systemd_postun_with_restart debuginfod.service

%changelog
* Fri Apr 3 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.194-5
- Use HTTPS for sourceware tarball instead

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.194-1
- Prepare for Oreon 11 (RP1)
