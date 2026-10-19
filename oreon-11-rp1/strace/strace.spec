%global source0_hash 4bde6246926890dcee824f6e6ac42a06752f47d77e5097d86e3c0d6d4b709fe5
Summary:        Tracks and displays system calls associated with a running process
Name: strace
Version: 7.2
Release:        1%{?dist}
License: LGPL-2.1+ and GPL-2.0+
URL: https://strace.io
Source0:        https://strace.io/files/%{version}/strace-%{version}.tar.xz
%if 0%{?suse_version} >= 1100
%define buildrequires_stacktrace BuildRequires: libdw-devel binutils-devel
%define buildrequires_selinux BuildRequires: libselinux-devel
%endif
%{?buildrequires_stacktrace}
%{?buildrequires_selinux}
%{?!buildroot:BuildRoot: %_tmppath/buildroot-%name-%version-%release}
%define maybe_use_defattr %{?suse_version:%%defattr(-,root,root)}
%{?!__make:       %global __make %_bindir/make}
%{?!__install:    %global __install %_bindir/install}
%{?!make_build:   %global make_build %__make %{?_smp_mflags}}
%{?!make_install: %global make_install %__make install DESTDIR="%{?buildroot}" INSTALL="%__install -p"}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
# /oreon:deps
%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
echo -n %version-%release > .tarball-version
echo -n 2026 > .year
echo -n 2025-11-13 > doc/.strace.1.in.date
echo -n 2025-07-02 > doc/.strace-log-merge.1.in.date

%build

echo 'BEGIN OF BUILD ENVIRONMENT INFORMATION'
uname -a |head -1
libc="$(ldd /bin/sh |sed -n 's|^[^/]*\(/[^ ]*/libc\.so[^ ]*\).*|\1|p' |head -1)"
$libc |head -1
file -L /bin/sh
gcc --version |head -1
ld --version |head -1
kver="$(printf '%%s\n%%s\n' '#include <linux/version.h>' 'LINUX_VERSION_CODE' | gcc -E -P -)"
printf 'kernel-headers %%s.%%s.%%s\n' $((kver/65536)) $((kver/256%%256)) $((kver%%256))
echo 'END OF BUILD ENVIRONMENT INFORMATION'
CFLAGS_FOR_BUILD="$RPM_OPT_FLAGS"; export CFLAGS_FOR_BUILD
%configure --enable-mpers=check --enable-bundled=yes
%make_build
%install
%make_install
for f in ChangeLog ChangeLog-CVS; do
	gzip -9n < "$f" > "$f".gz &
done
wait
%oreon_autofiles main

%check

width=$(echo __LONG_WIDTH__ |%__cc -E -P -)
skip_32bit=0
%if 0%{?fedora} >= 35 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
skip_32bit=1
%endif
if [ "${width}" != 32 ] || [ "${skip_32bit}" != 1 ]; then
	%{buildroot}%{_bindir}/strace -V
	%make_build -k check VERBOSE=1
	echo 'BEGIN OF TEST SUITE INFORMATION'
	tail -n 99999 -- tests*/test-suite.log tests*/ksysent.gen.log
	find tests* -type f -name '*.log' -print0 |
		xargs -r0 grep -H '^KERNEL BUG:' -- ||:
	echo 'END OF TEST SUITE INFORMATION'
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
