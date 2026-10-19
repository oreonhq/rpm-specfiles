%global source0_hash 234b110e6df9b7f6843e2ee53473127c2211243a16748f229fc0127845f68d94
Summary:        A real mode 80x86 assembler and linker
Name: dev86
Version: 0.16.21
Release:        33%{?dist}
License: GPL-1.0-or-later AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL: http://v3.sk/~lkundrak/dev86/
Source0:        https://src.fedoraproject.org/repo/pkgs/dev86/Dev86src-0.16.21.tar.gz/6b96fe9d2d1c546842a4d1c7ef387e4c/Dev86src-0.16.21.tar.gz
Patch0: dev86-noelks.patch
Patch1: dev86-64bit.patch
Patch2: dev86-nostrip.patch
Patch4: dev86-long.patch
%global __brp_strip_lto %{nil}
%global __brp_strip_static_archive %{nil}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The dev86 package provides an assembler and linker for real mode 80x86
instructions. You'll need to have this package installed in order to
build programs that run in real mode, including LILO and the kernel's
bootstrapping code, from their sources.

You should install dev86 if you intend to build programs that run in real
mode from their source code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .noelks
%if 0%{?__isa_bits} == 64
%patch -P1 -p1 -b .64bit
%endif
%patch -P2 -p1 -b .nostrip
%patch -P4 -p1 -b .long

%build

%global build_type_safety_c 0
make bcc86 unproto copt as86 ld86 CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -std=gnu17"
make -C cpp CFLAGS="$RPM_OPT_FLAGS -std=gnu17" %{?_smp_mflags}
make -C ar CFLAGS="$RPM_OPT_FLAGS -std=gnu17" %{?_smp_mflags}
make -C ld CFLAGS="$RPM_OPT_FLAGS -std=gnu17" %{?_smp_mflags}
make
%install
rm -rf ${RPM_BUILD_ROOT}
make	DIST=${RPM_BUILD_ROOT} \
	MANDIR=%{_mandir} \
	LIBDIR=%{_libdir}/bcc \
	INCLDIR=%{_libdir}/bcc \
	LOCALPREFIX=%{_prefix} \
	install install-man
for i in bootblocks copt dis88 unproto bin86 ; do cp $i/README README.$i ; done
cp bin86/README-0.4 README-0.4.bin86
cp bin86/ChangeLog ChangeLog.bin86
mv libc/COPYING COPYING.LGPL
pushd ${RPM_BUILD_ROOT}%{_bindir}
rm -f nm86 size86
ln -s objdump86 nm86
ln -s objdump86 size86
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
