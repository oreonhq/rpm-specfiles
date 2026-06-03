%global source0_hash d1c030756ecc182defee9fe885638c1785d35a2c2a297b4604c0e0dcc78e47da

Name:    cdrkit
Version: 1.1.11
Release: 63%{?dist}
Summary: A collection of CD/DVD utilities
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://cdrkit.org/
Source:        https://deb.debian.org/debian/pool/main/c/cdrkit/cdrkit_%{version}.orig.tar.gz#/cdrkit-%{version}.tar.gz

Patch1: cdrkit-1.1.8-werror.patch
Patch2: cdrkit-1.1.9-efi-boot.patch
Patch4: cdrkit-1.1.9-no_mp3.patch
Patch5: cdrkit-1.1.9-buffer_overflow.patch
Patch6: cdrkit-1.1.10-build-fix.patch
Patch7: cdrkit-1.1.11-manpagefix.patch
Patch8: cdrkit-1.1.11-rootstat.patch
Patch9: cdrkit-1.1.11-usalinst.patch
Patch10: cdrkit-1.1.11-readsegfault.patch
Patch11: cdrkit-1.1.11-format.patch
Patch12: cdrkit-1.1.11-handler.patch
Patch13: cdrkit-1.1.11-dvdman.patch
Patch14: cdrkit-1.1.11-paranoiacdda.patch
Patch15: cdrkit-1.1.11-utf8.patch
Patch16: cdrkit-1.1.11-cmakewarn.patch
Patch17: cdrkit-1.1.11-memset.patch
Patch19: cdrkit-1.1.11-ppc64le_elfheader.patch
Patch20: cdrkit-1.1.11-werror_gcc5.patch
Patch21: cdrkit-1.1.11-devname.patch
Patch22: cdrkit-1.1.11-sysmacros.patch
Patch23: cdrkit-1.1.11-gcc10.patch
Patch24: cdrkit-1.1.11-cmakesbin.patch
BuildRequires:  gcc
BuildRequires: cmake libcap-devel zlib-devel perl-interpreter perl-generators file-devel bzip2-devel

%description
cdrkit is a collection of CD/DVD utilities.

%package -n wodim
Summary: A command line CD/DVD recording program
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils

%description -n wodim
Wodim is an application for creating audio and data CDs. Wodim
works with many different brands of CD recorders, fully supports
multi-sessions and provides human-readable error messages.

%package -n genisoimage
Summary: Creates an image of an ISO9660 file-system
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils

%description -n genisoimage
The genisoimage program is used as a pre-mastering program; i.e., it
generates the ISO9660 file-system. Genisoimage takes a snapshot of
a given directory tree and generates a binary image of the tree
which will correspond to an ISO9660 file-system when written to
a block device. Genisoimage is used for writing CD-ROMs, and includes
support for creating boot-able El Torito CD-ROMs.

Install the genisoimage package if you need a program for writing
CD-ROMs.

%package -n dirsplit
Summary: Utility to split directories
Requires: perl-interpreter >= 4:5.8.1
Requires: genisoimage%{?_isa} = %{version}-%{release}

%description -n dirsplit
This utility is used to split directories into chunks before burning. 
Chunk size is usually set to fit to a CD/DVD.

%package -n icedax
Summary: A utility for sampling/copying .wav files from digital audio CDs
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils
Requires: vorbis-tools
Requires: cdparanoia
BuildRequires: cdparanoia-devel

%description -n icedax
Icedax is a sampling utility for CD-ROM drives that are capable of
providing a CD's audio data in digital form to your host. Audio data
read from the CD can be saved as .wav or .sun format sound files.
Recording formats include stereo/mono, 8/12/16 bits and different
rates. Icedax can also be used as a CD player.

%package -n libusal
Summary: Library to communicate with SCSI devices

%description -n libusal
The libusal package contains C libraries that allows applications
to communicate with SCSI devices and is well suitable for writing
CD-R media.

%package -n libusal-devel
Summary: Development files for libusal
Requires: libusal%{?_isa} = %{version}-%{release}

%description -n libusal-devel
The libusal-devel package contains C libraries and header files
for developing applications that use libusal for communication with
SCSI devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q 
%patch -P1 -p1 -b .werror
%patch -P2 -p1 -b .efi
%patch -P4 -p1 -b .no_mp3
%patch -P5 -p1 -b .buffer_overflow
%patch -P6 -p1 -b .build-fix
%patch -P7 -p1 -b .manpagefix
%patch -P8 -p1 -b .rootstat
%patch -P9 -p1 -b .usalinst
%patch -P10 -p1 -b .readsegfault
%patch -P11 -p1 -b .format
%patch -P12 -p1 -b .handler
%patch -P13 -p1 -b .dvdman
%patch -P14 -p1 -b .paranoiacdda
# not using -b since otherwise backup files would be included into rpm
%patch -P15 -p1
%patch -P16 -p1 -b .cmakewarn
%patch -P17 -p1 -b .edcspeed
%patch -P19 -p1 -b .elfheader
%patch -P20 -p1 -b .werror_gcc5
%patch -P21 -p1 -b .devname
%patch -P22 -p1 -b .sysmacros
%patch -P23 -p1 -b .gcc10
%patch -P24 -p1 -b .cmakesbin

# we do not want bundled paranoia library
rm -rf libparanoia

find . -type f -print0 | xargs -0 perl -pi -e 's#/usr/local/bin/perl#/usr/bin/perl#g'
find doc -type f -print0 | xargs -0 chmod a-x 


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=format-security -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export FFLAGS="$CFLAGS"

%cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DBUILD_SHARED_LIBS:BOOL=ON

%cmake_build

%install
%cmake_install
perl -pi -e 's#^require v5.8.1;##g' $RPM_BUILD_ROOT%{_bindir}/dirsplit
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkisofs
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkhybrid
ln -s icedax $RPM_BUILD_ROOT%{_bindir}/cdda2wav
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/cdrecord
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/dvdrecord

# missing man page. Do symlink like in debian
ln -sf wodim.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/netscsid.1.gz

# we don't need cdda2mp3 since we don't have any mp3 {en,de}coder
rm $RPM_BUILD_ROOT%{_bindir}/cdda2mp3

%post -n wodim
link=`readlink %{_bindir}/cdrecord`
if [ "$link" == "%{_bindir}/wodim" ]; then
	rm -f %{_bindir}/cdrecord
fi
link=`readlink %{_bindir}/dvdrecord`
if [ "$link" == "wodim" ]; then
	rm -f %{_bindir}/dvdrecord
fi

/usr/sbin/alternatives --install %{_bindir}/cdrecord cdrecord \
		%{_bindir}/wodim 50 \
	--slave %{_mandir}/man1/cdrecord.1.gz cdrecord-cdrecordman \
		%{_mandir}/man1/wodim.1.gz \
	--slave %{_bindir}/dvdrecord cdrecord-dvdrecord %{_bindir}/wodim \
	--slave %{_mandir}/man1/dvdrecord.1.gz cdrecord-dvdrecordman \
		%{_mandir}/man1/wodim.1.gz \
	--slave %{_bindir}/readcd cdrecord-readcd %{_bindir}/readom \
	--slave %{_mandir}/man1/readcd.1.gz cdrecord-readcdman \
		%{_mandir}/man1/readom.1.gz 

%preun -n wodim
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove cdrecord %{_bindir}/wodim
fi

%post -n genisoimage
link=`readlink %{_bindir}/mkisofs`
if [ "$link" == "genisoimage" ]; then
	rm -f %{_bindir}/mkisofs
fi

/usr/sbin/alternatives --install %{_bindir}/mkisofs mkisofs \
		%{_bindir}/genisoimage 50 \
	--slave %{_mandir}/man1/mkisofs.1.gz mkisofs-mkisofsman \
		%{_mandir}/man1/genisoimage.1.gz \
	--slave %{_bindir}/mkhybrid mkisofs-mkhybrid %{_bindir}/genisoimage \
	--slave %{_mandir}/man1/mkhybrid.1.gz mkisofs-mkhybridman \
		%{_mandir}/man1/genisoimage.1.gz

%preun -n genisoimage
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove mkisofs %{_bindir}/genisoimage
fi

%post -n icedax
link=`readlink %{_bindir}/cdda2wav`
if [ "$link" == "icedax" ]; then
	rm -f %{_bindir}/cdda2wav
fi
/usr/sbin/alternatives --install %{_bindir}/cdda2wav cdda2wav \
		%{_bindir}/icedax 50 \
	--slave %{_mandir}/man1/cdda2wav.1.gz cdda2wav-cdda2wavman \
		%{_mandir}/man1/icedax.1.gz 

%preun -n icedax
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove cdda2wav %{_bindir}/icedax
fi

%ldconfig_scriptlets -n libusal

%files -n wodim
%license COPYING
%doc Changelog FAQ FORK START
%doc doc/READMEs doc/wodim
%{_bindir}/devdump
%caps(cap_ipc_lock=ep) %{_bindir}/wodim
%ghost %{_bindir}/cdrecord
%ghost %{_bindir}/dvdrecord
%{_bindir}/readom
%{_sbindir}/netscsid
%{_mandir}/man1/devdump.*
%{_mandir}/man1/wodim.*
%{_mandir}/man1/netscsid.*
%{_mandir}/man1/readom.*

%files -n icedax
%license COPYING
%doc doc/icedax
%{_bindir}/icedax
%ghost %{_bindir}/cdda2wav
%{_bindir}/cdda2ogg
%{_mandir}/man1/icedax.*
%{_mandir}/man1/cdda2ogg.*
%{_mandir}/man1/list_audio_tracks.*

%files -n genisoimage
%license COPYING
%doc doc/genisoimage
%{_bindir}/genisoimage
%ghost %{_bindir}/mkisofs
%ghost %{_bindir}/mkhybrid
%{_bindir}/isodebug
%{_bindir}/isodump
%{_bindir}/isoinfo
%{_bindir}/isovfy
%{_bindir}/pitchplay
%{_bindir}/readmult
%{_mandir}/man5/genisoimagerc.*
%{_mandir}/man1/genisoimage.*
%{_mandir}/man1/isodebug.*
%{_mandir}/man1/isodump.*
%{_mandir}/man1/isoinfo.*
%{_mandir}/man1/isovfy.*
%{_mandir}/man1/pitchplay.*
%{_mandir}/man1/readmult.*

%files -n dirsplit
%license COPYING
%{_bindir}/dirsplit
%{_mandir}/man1/dirsplit.*

%files -n libusal
%license COPYING
%doc doc/plattforms/README.linux Changelog FAQ FORK START
%{_libdir}/libusal.so.*
%{_libdir}/librols.so.*

%files -n libusal-devel
%license COPYING
%{_libdir}/libusal.so
%{_libdir}/librols.so
%{_includedir}/usal

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.11-63
- Import
