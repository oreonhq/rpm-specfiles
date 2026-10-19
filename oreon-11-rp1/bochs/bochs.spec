%global source0_hash 14aaf78dbe1337987923fffc4e7a962ae56abcf9a87474ace39e593f9f84ee84
%define _hardened_build 1
Name:           bochs
Version:        3.1
Release:        1%{?dist}
Summary:        Portable x86 PC emulator
License:        LGPL-2.0-or-later
URL:            http://bochs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}-0001_bx-qemu.patch
Patch7: %{name}-nonet-build.patch
Patch8: bochs-aarch64.patch
Patch10: bochs-usb.patch
Patch11: bochs-2.6.10-slirp-include.patch
ExcludeArch:    s390x i686
%ifarch %{ix86} x86_64
%endif
Requires:       %{name}-bios = %{version}-%{release}
Requires:       seavgabios-bin
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  byacc
BuildRequires:  docbook-utils
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
Bochs is a portable x86 PC emulation software package that emulates
enough of the x86 CPU, related AT hardware, and BIOS to run DOS,
Windows '95, Minix 2.0, and other OS's, all on your workstation.

%package        debugger
Summary:        Bochs with builtin debugger
Requires:       %{name} = %{version}-%{release}
%description    debugger
Special version of bochs compiled with the builtin debugger.

%package        gdb
Summary:        Bochs with support for debugging with gdb
Requires:       %{name} = %{version}-%{release}
%description    gdb
Special version of bochs compiled with a gdb stub so that the software running
inside the emulator can be debugged with gdb.

%ifarch %{ix86} x86_64
# building firmwares are quite tricky, because they often have to be built on
# their native architecture (or in a cross-capable compiler, that we lack in
# koji), and deployed everywhere. Recent koji builders support a feature
# that allow us to build packages in a single architecture, and create noarch
# subpackages that will be deployed everywhere. Because the package can only
# be built in certain architectures, the main package has to use
# BuildArch: <nativearch>, or something like that.
# Note that using ExclusiveArch is _wrong_, because it will prevent the noarch
# packages from getting into the excluded repositories.
%package	bios
Summary:        Bochs bios
BuildArch:      noarch
Provides:       bochs-bios-data = 2.3.8.1
Obsoletes:      bochs-bios-data < 2.3.8.1
%description bios
Bochs BIOS is a free implementation of a x86 BIOS provided by the Bochs project.
It can also be used in other emulators, such as QEMU
%endif

%package        devel
Summary:        Bochs header and source files
Requires:       %{name} = %{version}-%{release}
%description    devel
Header and source files from bochs source.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 7 -p0 -z .nonet

# Fix up some man page paths.
sed -i -e 's|/usr/local/share/|%{_datadir}/|' doc/man/*.*

# remove executable bits from sources to make rpmlint happy with the debuginfo
chmod -x `find -name '*.cc' -o -name '*.h' -o -name '*.inc'`
# Fix CHANGES encoding
iconv -f ISO_8859-2 -t UTF8 CHANGES > CHANGES.tmp
mv CHANGES.tmp CHANGES

%build

CONFIGURE_FLAGS=" \
  --enable-ne2000 \
  --enable-pci \
  --enable-all-optimizations \
  --enable-clgd54xx \
  --enable-sb16=linux \
  --enable-3dnow \
  --with-x11 \
  --with-nogui \
  --with-term \
  --with-rfb \
  --with-sdl2 \
  --without-wx \
  --with-svga=no \
  --enable-cpu-level=6 \
  --enable-disasm \
  --enable-e1000 \
  --enable-x86-64 \
  --enable-smp"
export CXXFLAGS="$RPM_OPT_FLAGS -DPARANOID"
%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-debugger
make %{?_smp_mflags}
mv bochs bochs-debugger
%configure $CONFIGURE_FLAGS --enable-x86-debugger --enable-gdb-stub --enable-smp=no
make %{?_smp_mflags}
mv bochs bochs-gdb
%configure $CONFIGURE_FLAGS
make %{?_smp_mflags}
%ifarch %{ix86} x86_64
cd bios
make bios
cp BIOS-bochs-latest BIOS-bochs-kvm
%endif
%install
rm -rf $RPM_BUILD_ROOT _installed-docs
make install DESTDIR=$RPM_BUILD_ROOT
ln -s %{_prefix}/share/seavgabios/vgabios-cirrus.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-cirrus
ln -s %{_prefix}/share/seavgabios/vgabios-isavga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-isavga
ln -s %{_prefix}/share/seavgabios/vgabios-qxl.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-qxl
ln -s %{_prefix}/share/seavgabios/vgabios-stdvga.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-stdvga
ln -s %{_prefix}/share/seavgabios/vgabios-vmware.bin $RPM_BUILD_ROOT%{_prefix}/share/bochs/vgabios-vmware
%ifnarch %{ix86} x86_64
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/bochs/*{BIOS,bios,i440fx}*
%endif
install -m 755 bochs-debugger bochs-gdb $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_docdir}/bochs _installed-docs
rm $RPM_BUILD_ROOT%{_mandir}/man1/bochs-dlx.1*
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm
cp -pr config.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu
cp -pr cpu/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
cp -pr cpu/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder
cp -pr cpu/decoder/*.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
cp -pr cpu/decoder/*.cc $RPM_BUILD_ROOT%{_prefix}/include/bochs/cpu/decoder/
cp -pr osdep.h $RPM_BUILD_ROOT%{_prefix}/include/bochs/disasm/
rm -f $RPM_BUILD_ROOT%{_datadir}/bochs/SeaVGABIOS-README
%oreon_autofiles bochs-debugger usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bochs-gdb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bochs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n bochs-debugger -f %{oreon_filedir}/bochs-debugger.list
%files -n bochs-gdb -f %{oreon_filedir}/bochs-gdb.list
%files -n bochs-devel -f %{oreon_filedir}/bochs-devel.list

%changelog

%autochangelog
