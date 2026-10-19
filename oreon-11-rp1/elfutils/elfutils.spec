%global source0_hash fd5cc6b77ad6773cac93cb3f415f9318ac3b3455eecf801f6b4a742c4f6c7209
%bcond_with static
Name: elfutils
Version: 0.196
%global baserelease 1
Release:        1%{?dist}
URL: http://elfutils.org/
%global source_url https://sourceware.org/pub/elfutils/%{version}/
License: GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GFDL-1.3-no-invariants-or-later
Source0:        %{source_url}%{name}-%{version}.tar.bz2
Source1: elfutils-debuginfod.sysusers
Summary:        A collection of utilities and DSOs to handle ELF files and DWARF data
%global depsuffix %{?_isa}%{!?_isa:-%{_arch}}
%ifarch %{ix86} x86_64 %{arm} aarch64
%global enable_stackprof 1
%else
%global enable_stackprof 0
%endif
Requires: elfutils-libelf%{depsuffix} = %{version}-%{release}
Requires: elfutils-libs%{depsuffix} = %{version}-%{release}
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
%global _gnu %{nil}
%global _program_prefix eu-
%global provide_yama_scope      0
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%global provide_yama_scope      1
%endif
%global with_sysusers           0
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global with_sysusers           1
%endif
Patch1: elfutils-0.186-fdo-swap.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bsdtar
BuildRequires:  bzip2
BuildRequires:  bzip2-devel
BuildRequires:  curl
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  ima-evm-utils-devel
BuildRequires:  iproute
BuildRequires:  jq
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  procps
BuildRequires:  rpm-devel
BuildRequires:  rpm-sign
BuildRequires:  socat
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zstd
# /oreon:deps
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
Requires: default-yama-scope
Requires: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
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
Requires: elfutils-debuginfod-client-devel%{depsuffix} = %{version}-%{release}
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

%package default-yama-scope
Summary: Default yama attach scope sysctl setting
License: GPL-2.0-or-later OR LGPL-3.0-or-later
Provides: default-yama-scope
BuildArch: noarch
BuildRequires: systemd >= 215
Requires(post): systemd
%description default-yama-scope
Yama sysctl setting to enable default attach scope settings
enabling programs to use ptrace attach, access to
/proc/PID/{mem,personality,stack,syscall}, and the syscalls
process_vm_readv and process_vm_writev which are used for
interprocess services, communication and introspection
(like synchronisation, signaling, debugging, tracing and
profiling) of processes.

%package debuginfod-client
Summary: Library and command line client for build-id HTTP ELF/DWARF server
License: GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later)
%if 0%{!?_isa:1}
Provides: elfutils-debuginfod-client%{depsuffix} = %{version}-%{release}
%endif
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
BuildRequires: systemd-rpm-macros
BuildRequires: make
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%{?sysusers_requires_compat}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

autoreconf -f -v -i

# In case the above patches added any new test scripts, make sure they
# are executable.
find . -name \*.sh ! -perm -0100 -print | xargs chmod +x

%build

RPM_OPT_FLAGS="${RPM_OPT_FLAGS/-Wall/}"
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -Wformat"
trap 'cat config.log' EXIT
%configure CFLAGS="$RPM_OPT_FLAGS" \
%if "%{?dist_debuginfod_url}"
	--enable-debuginfod \
	--enable-debuginfod-urls="%{dist_debuginfod_url}" \
%endif
	--enable-debuginfod-ima-verification \
	--enable-debuginfod-ima-cert-path=%{_sysconfdir}/keys/ima
trap '' EXIT
%make_build
%install
%make_install
chmod +x ${RPM_BUILD_ROOT}%{_prefix}/%{_lib}/lib*.so*
%if %{without static}
rm ${RPM_BUILD_ROOT}%{_prefix}/%{_lib}/lib{elf,dw,asm}.a
%endif
%find_lang %{name}
install -Dm0644 config/10-default-yama-scope.conf ${RPM_BUILD_ROOT}%{_sysctldir}/10-default-yama-scope.conf
install -Dm0644 config/debuginfod.service ${RPM_BUILD_ROOT}%{_unitdir}/debuginfod.service
install -Dm0644 config/debuginfod.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/debuginfod
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/cache/debuginfod
touch ${RPM_BUILD_ROOT}%{_localstatedir}/cache/debuginfod/debuginfod.sqlite
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/elfutils-debuginfod.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

uname -r; rpm -q binutils gcc glibc || true
%make_build check || (cat tests/test-suite.log; false)
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
%post default-yama-scope

if [ -x /usr/lib/systemd/systemd-sysctl ] ; then
%sysctl_apply 10-default-yama-scope.conf
fi
%pre debuginfod

%sysusers_create_compat %{SOURCE1}
%post debuginfod

%systemd_post debuginfod.service
%postun debuginfod

%systemd_postun_with_restart debuginfod.service
%files -f %{oreon_filedir}/main.list
%files -n elfutils-libs -f %{oreon_filedir}/elfutils-libs.list
%files -n elfutils-devel -f %{oreon_filedir}/elfutils-devel.list
%files -n elfutils-libelf -f %{oreon_filedir}/elfutils-libelf.list
%files -n elfutils-libelf-devel -f %{oreon_filedir}/elfutils-libelf-devel.list
%files -n elfutils-default-yama-scope -f %{oreon_filedir}/elfutils-default-yama-scope.list
%files -n elfutils-debuginfod-client -f %{oreon_filedir}/elfutils-debuginfod-client.list
%files -n elfutils-debuginfod-client-devel -f %{oreon_filedir}/elfutils-debuginfod-client-devel.list
%files -n elfutils-debuginfod -f %{oreon_filedir}/elfutils-debuginfod.list

%changelog

%autochangelog
