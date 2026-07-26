%global source0_hash 5bf13104cb327472b5cb65643352a9138646becacc06763088d83001d832d048

Name:           libx86
Version:        1.1
Release:        48%{?dist}
Summary:        Library for making real-mode x86 calls

License:        MIT
URL:            http://www.codon.org.uk/~mjg59/libx86
Source0:        http://www.codon.org.uk/~mjg59/libx86/downloads/%{name}-%{version}.tar.gz
# does not build on ppc, ppc64 and s390* yet, due to the lack of port i/o
# redirection and video routing
ExcludeArch:    ppc %{power64} s390 s390x %{sparc} aarch64 armv7hl

Patch0: libx86-add-pkgconfig.patch
Patch1: libx86-mmap-offset.patch
# patch from  https://bugs.debian.org/cgi-bin/bugreport.cgi?msg=34;filename=libx86-libc-test.patch.txt;att=1;bug=570676
# debian control portion removed as it fails to apply and we do not need it anyway
Patch2: libx86-libc-test.patch
Patch3: libx86-fix_processor_flags.patch
Patch4: libx86-ld_flags.patch
Patch5: libx86-1.1-24-fix-invalid-hlt-opcode.patch
Patch6: libx86-c99.patch
Patch7: libx86-c99-2.patch

BuildRequires:  gcc
BuildRequires: make
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

%autosetup

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" make BACKEND=x86emu LIBDIR=%{_libdir} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
rm $RPM_BUILD_ROOT/%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc COPYRIGHT
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/x86.pc

%changelog
%autochangelog
