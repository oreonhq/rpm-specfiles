%global source0_hash 154ab23b60070e8f27013c22977f1129425d67d1e8acd6e13010e617811e4cff
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: binutils
Version: 2.47
Release: 1%{?dist}
Summary: GNU binutils
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/binutils/
Source0: https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: zlib-devel
%endif

%description
These are the GNU binutils. These are utilities of use when dealing with binary files, either object files or executables. These tools consist of the linkers (ld and gold), the assembler (gas), and the profiler (gprof and gprofng) each of which have their own sub-directory named after them. There is also a collection of other binary tools, including the disassembler (objdump) in this directory.

%prep
%oreon_sha256
%autosetup -p1

%build
# fortify flags break this build
unset CFLAGS CXXFLAGS LDFLAGS
mkdir -p %{_builddir}/binutils-build
cd %{_builddir}/binutils-build
%if %{with bootstrap} || 0%{?bootstrap}
%{_builddir}/binutils-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --enable-shared \
  --disable-werror \
  --disable-nls \
  --disable-multilib \
  --disable-gprofng \
  --enable-gold=no
%else
%{_builddir}/binutils-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --enable-shared \
  --disable-werror \
  --disable-nls \
  --disable-multilib \
  --disable-gprofng \
  --enable-gold=no \
  --with-system-zlib
%endif
make -j%{?_smp_build_ncpus}

%install
cd %{_builddir}/binutils-build
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
