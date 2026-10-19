%global source0_hash 872ce0b9507f468cfd748815a4236bf1f4acb4525eb8286ce5495ccd4a0d8467
%global _binaries_in_noarch_packages_terminate_build   0
%global __debug_package %{nil}
Name:           arch-test
Version:        0.22
Release:        1%{?dist}
Summary:        Tools to detect architectures runnable by your machine+kernel
License:        MIT
URL:            https://github.com/kilobyte/arch-test
Source0:        https://github.com/kilobyte/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/aarch64-linux-gnu-as
BuildRequires:  /usr/bin/aarch64-linux-gnu-ld
BuildRequires:  /usr/bin/alpha-linux-gnu-as
BuildRequires:  /usr/bin/alpha-linux-gnu-ld
BuildRequires:  /usr/bin/arc-linux-gnu-as
BuildRequires:  /usr/bin/arc-linux-gnu-ld
BuildRequires:  /usr/bin/arm-linux-gnu-as
BuildRequires:  /usr/bin/arm-linux-gnu-ld
BuildRequires:  /usr/bin/hppa-linux-gnu-as
BuildRequires:  /usr/bin/hppa-linux-gnu-ld
BuildRequires:  /usr/bin/i686-w64-mingw32-as
BuildRequires:  /usr/bin/i686-w64-mingw32-ld
BuildRequires:  /usr/bin/ia64-linux-gnu-as
BuildRequires:  /usr/bin/ia64-linux-gnu-ld
BuildRequires:  /usr/bin/loongarch64-linux-gnu-as
BuildRequires:  /usr/bin/loongarch64-linux-gnu-ld
BuildRequires:  /usr/bin/m68k-linux-gnu-as
BuildRequires:  /usr/bin/m68k-linux-gnu-ld
BuildRequires:  /usr/bin/mips64-linux-gnu-as
BuildRequires:  /usr/bin/mips64-linux-gnu-ld
BuildRequires:  /usr/bin/powerpc64-linux-gnu-as
BuildRequires:  /usr/bin/powerpc64-linux-gnu-ld
BuildRequires:  /usr/bin/powerpc64le-linux-gnu-as
BuildRequires:  /usr/bin/powerpc64le-linux-gnu-ld
BuildRequires:  /usr/bin/riscv64-linux-gnu-as
BuildRequires:  /usr/bin/riscv64-linux-gnu-ld
BuildRequires:  /usr/bin/s390x-linux-gnu-as
BuildRequires:  /usr/bin/s390x-linux-gnu-ld
BuildRequires:  /usr/bin/sh-linux-gnu-as
BuildRequires:  /usr/bin/sh-linux-gnu-ld
BuildRequires:  /usr/bin/sparc64-linux-gnu-as
BuildRequires:  /usr/bin/sparc64-linux-gnu-ld
BuildRequires:  /usr/bin/x86_64-linux-gnu-as
BuildRequires:  /usr/bin/x86_64-linux-gnu-ld
BuildRequires:  /usr/bin/x86_64-w64-mingw32-as
BuildRequires:  /usr/bin/x86_64-w64-mingw32-ld
BuildRequires:  make
BuildRequires:  mingw32-crt
BuildRequires:  mingw64-crt
# /oreon:deps
%description
This tool will tell you "can your machine+kernel run architecture X?".

The check is for the ability to run machine code and supporting appropriate
syscall ABI, not for the presence of userland libraries.  IE, a positive
answer means you can use a chroot or container of that architecture, add it
to your multiarch set, etc, but doesn't mean you can currently run non-static
binaries without installing required libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# add search path to find '-lkernel32'
sed -i 's:-s win32.o:-s win32.o -L%{mingw32_libdir}:' Makefile
sed -i 's:-s win64.o:-s win64.o -L%{mingw64_libdir}:' Makefile

# use triplets of cross-build binutils of Fedora
sed -i 's/sh4-linux-gnu/sh-linux-gnu/' Makefile
cat << "EOF" >config
VERSION=%{version}
MIPS=mips64-linux-gnu
POWERPC=powerpc64-linux-gnu
ARM=arm-linux-gnu
RISCV=riscv64-linux-gnu
EOF

%build

%make_build
%install
%make_install PREFIX=%{_prefix}
chmod 644 %{buildroot}%{_mandir}/man1/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
