%global source0_hash cd9fc3fe2b47743840e42c1592d3d87f8302eb18639c0b8b4ba0898002e2348f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gdb
Version: 18.1
Release: 1%{?dist}
Summary: GNU debugger (minimal build)
License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL: https://www.sourceware.org/gdb/
Source0: https://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz
Source1: gdb-%{version}.tar.xz.sig
Source2: gdb-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: gcc-c++
BuildRequires: texinfo
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: zstd-devel
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: expat-devel
BuildRequires: bison
BuildRequires: flex
%endif

%description
GDB lets you see what is going on inside a program while it executes. This
minimal build has no Python, Guile or debuginfod support.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n gdb-%{version} -p1

%build
mkdir -p oreon-build
cd oreon-build
../configure --prefix=%{_prefix} --libdir=%{_libdir} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --with-system-readline --with-system-zlib --without-python --without-guile --without-debuginfod \
  --without-babeltrace --without-intel-pt --disable-sim --disable-binutils --disable-ld --disable-gold \
  --disable-gas --disable-gprof --disable-gprofng --disable-werror \
  CFLAGS="%{_oreon_cflags}" CXXFLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}"
make -s %{?_smp_mflags} all-gdb all-gdbserver

%install
cd oreon-build
make -s install-gdb install-gdbserver DESTDIR=%{buildroot}
cd ..
rm -rf %{buildroot}%{_includedir}/{bfd,ansidecl,bfdlink,ctf,ctf-api,diagnostics,dis-asm,plugin-api,symcat}*.h
rm -f %{buildroot}%{_infodir}/{bfd,ctf-spec,sframe-spec}.info*
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING COPYING.LIB
