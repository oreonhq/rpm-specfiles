%global source0_hash e5be3a38a0d2b71ba558eb310a2db44ea6e7c208e16d4fd907dc6ed11c46b1a7

# Regarding the following rpmlint citation:
#
#   library package calls exit() or _exit() [...]
#
# Electric fence is a debugger, not a library.  The fact that it comes
# in the form factor of a library is just because that's how you
# override malloc-related calls from libc.  Calling _exit is the
# ultimate outcome of detecting a class of memory errors (double free,
# free of wild pointer, etc.)  Overflows (or underflows) are detected
# by the operating system and lead to process termination as well.
#
#   devel-file-in-non-devel-package /usr/lib64/libefence.a
#
# Electric fence is itself a development package.

Summary: A debugger which detects memory allocation violations
Name: ElectricFence
Version: 2.2.2
Release: 69%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://perens.com/FreeSoftware/ElectricFence/

# ftp://ftp.perens.com/pub/ElectricFence/beta/ used to be here, but
# the site is inaccessible as of lately.  I looked through the web but
# didn't find anything.  Debian has a link to a site that hosts an
# obsolete version.  I don't think there's any proper upstream for
# this.
Source: %{name}-%{version}.tar.gz
Patch1: ElectricFence-2.0.5-longjmp.patch
Patch2: ElectricFence-2.1-vaarg.patch
Patch3: ElectricFence-2.2.2-pthread.patch
Patch4: ElectricFence-2.2.2-madvise.patch
Patch5: ElectricFence-mmap-size.patch
Patch6: ElectricFence-2.2.2-banner.patch
Patch7: ElectricFence-2.2.2-ef.patch
Patch8: ElectricFence-2.2.2-builtins.patch
Patch9: ElectricFence-2.2.2-sse.patch
Patch10: ElectricFence-2.2.2-posix_memalign.patch
Patch11: ElectricFence-2.2.2-malloc_usable_size.patch
Patch12: ElectricFence-2.2.2-man-ef.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1105913
Patch13: ElectricFence-2.2.2-sys_errlist.patch

Patch14: ElectricFence-2.2.2-lto.patch

Patch15: ElectricFence-strerror.patch

BuildRequires:  gcc
BuildRequires: make
%description
ElectricFence is a utility for C programming and
debugging. ElectricFence uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by
free(). ElectricFence will then stop the program on the first
instruction that caused a bounds violation and you can use your
favorite debugger to display the offending statement.

Install ElectricFence if you need a debugger to find malloc()
violations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make CFLAGS='${RPM_OPT_FLAGS} -DUSE_SEMAPHORE -fpic'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}{%{_bindir},%{_libdir},%{_mandir}/man{1,3}}

make	BIN_INSTALL_DIR=%{buildroot}%{_bindir} \
	LIB_INSTALL_DIR=%{buildroot}%{_libdir} \
	MAN_INSTALL_DIR=%{buildroot}%{_mandir} \
	install

echo ".so man3/efence.3" > %{buildroot}%{_mandir}/man3/libefence.3

%ldconfig_scriptlets

%files
%doc README CHANGES COPYING
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so*
%{_mandir}/*/*

%changelog
%autochangelog
