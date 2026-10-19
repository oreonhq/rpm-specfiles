%global source0_hash 5bf13104cb327472b5cb65643352a9138646becacc06763088d83001d832d048
Name:           libx86
Version:        1.1
Release:        48%{?dist}
Summary:        Library for making real-mode x86 calls
License:        MIT
URL:            http://www.codon.org.uk/~mjg59/libx86
Source0:        http://www.codon.org.uk/~mjg59/libx86/downloads/%{name}-%{version}.tar.gz
ExcludeArch:    ppc %{power64} s390 s390x %{sparc} aarch64 armv7hl
Patch0: libx86-add-pkgconfig.patch
Patch1: libx86-mmap-offset.patch
Patch2: libx86-libc-test.patch
Patch3: libx86-fix_processor_flags.patch
Patch4: libx86-ld_flags.patch
Patch5: libx86-1.1-24-fix-invalid-hlt-opcode.patch
Patch6: libx86-c99.patch
Patch7: libx86-c99-2.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
A library to provide support for making real-mode x86 calls with an emulated
x86 processor.

%package devel
Summary:        Development tools for programs which will use libx86
Requires:       %{name} = %{version}-%{release}
%description devel
This package contains the static library and header file necessary for
development of programs that will use libx86 to make real-mode x86 calls.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" make BACKEND=x86emu LIBDIR=%{_libdir} %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
rm $RPM_BUILD_ROOT/%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libx86-devel -f %{oreon_filedir}/libx86-devel.list

%changelog

%autochangelog
