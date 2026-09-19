%global source0_hash 20969da7da7d241a581db89e1ec78bf5c76015a9e7135b94e23c348347c2366b

Summary: A general purpose sound file conversion tool
Name: sox
# A mistake in naming, 14.4.2rc2 breaks upgrade path.
# This workaround will go away with rebase to 14.4.3
# it affects Source, %%prep and Version
Version: 14.4.2.0
Release: 44%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
# Modified source tarball with libgsm license, without unlicensed liblpc10:
# _Source: http://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}.tar.gz
# _Source: %%{name}/%%{name}-%%{version}.modified.tar.gz
# _Source: %%{name}/%%{name}-14.4.2.modified.tar.bz2
Source0: https://github.com/i386x/sox-downstream/archive/%{name}-%{version}.modified.tar.gz
URL: http://sox.sourceforge.net/
# 0000 - 0099: General:
Patch0: sox-14.4.2-lsx_symbols.patch
Patch1: sox-14.4.2-lpc10.patch
Patch2: sox-14.4.2-fsf_address_fix.patch
# 0100 - 0999: Extensions:
# - no extensions yet
# 1000 - 8999: Bug fixes:
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1500570
# - upstream discussion: https://sourceforge.net/p/sox/mailman/sox-devel/thread/CAG_ZyaD8huzEm9cajDd63z1nGOTVRw=Y8vPE-t5pHB=9XmQ_Xw@mail.gmail.com/#msg36124536
# - patch origin: https://bogomips.org/sox.git/patch/?id=818bdd0ccc1e5b6cae742c740c17fd414935cf39
# - security fix for CVE-2017-15371
Patch1000: sox-14.4.2-bug_1500570_fix.patch
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1500554
# - upstream discussion: https://sourceforge.net/p/sox/mailman/sox-devel/thread/CAG_ZyaDcmDNEHRr2WBR2fPcXtu_kd5OdpRVTbhDe1YQZQA2c9w@mail.gmail.com/#msg36103130
# - patch origin: https://github.com/mansr/sox/commit/ef3d8be0f80cbb650e4766b545d61e10d7a24c9e.patch
# - security fix for CVE-2017-15370
Patch1001: sox-14.4.2-bug_1500554_fix.patch
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1500553
# - upstream discussion: https://sourceforge.net/p/sox/mailman/sox-devel/thread/CAG_ZyaBLxUKk_xmrvn2YfnVLNRE_Rzxe+cYBC5CJtK_xWrVvNw@mail.gmail.com/#msg36121067
# - patch origin: https://bogomips.org/sox.git/patch/?id=3f7ed312614649e2695b54b398475d32be4f64f3
# - security fix for CVE-2017-15372
Patch1002: sox-14.4.2-bug_1500553_fix.patch
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1510923
# - upstream discussion: https://sourceforge.net/p/sox/mailman/sox-devel/thread/CAG_ZyaA_WyTTEWeGYPUhG95M3wOv64vTqn8jeH4JYvgMnx83Tw@mail.gmail.com/#msg36128861
# - patch origin: https://sourceforge.net/p/sox/mailman/sox-devel/thread/20171120110535.14410-1-mans@mansr.com/#msg36129559
# - security fix for CVE-2017-15642
Patch1003: sox-14.4.2-bug_1510923_fix.patch
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1558887
# - upstream discussion: https://sourceforge.net/p/sox/bugs/308/
Patch1004: sox-14.4.2-hcom_stopwrite_big_endian_bug_fix.patch
# -rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1309426 [CLOSED DUPL]
#        https://bugzilla.redhat.com/show_bug.cgi?id=1226675
#        https://bugzilla.redhat.com/show_bug.cgi?id=1540762 [CLOSED DUPL]
#        https://bugzilla.redhat.com/show_bug.cgi?id=1492910 [CLOSED DUPL]
# - upstream discussion: https://sourceforge.net/p/sox/bugs/309/
Patch1005: sox-14.4.2-bug_1226675_fix.patch
# - security fix for CVE-2017-11332
#   * rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1480674
#   * upstream commit: https://sourceforge.net/p/sox/code/ci/6e177c455fb554327ff8125b6e6dde1568610abe/
# - security fix for CVE-2017-11358
#   * rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1480675
#   * upstream commit: https://sourceforge.net/p/sox/code/ci/e410d00c4821726accfbe1f825f2def6376e181f/
# - security fix for CVE-2017-11359
#   * rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1480676
#   * upstream commit: https://sourceforge.net/p/sox/code/ci/7b3f30e13e4845bafc93215a372c6eb7dcf04118/
# - rhbz tracker: https://bugzilla.redhat.com/show_bug.cgi?id=1480678
# - upstream discussion: https://sourceforge.net/p/sox/bugs/296/
Patch1006: sox-14.4.2-bug_1480678_fix.patch
# - rhbz: https://bugzilla.redhat.com/show_bug.cgi?id=1545867
# - upstream patch: https://sourceforge.net/p/sox/mailman/sox-devel/thread/20180426131552.29249-9-mans@mansr.com/#msg36303839
# - security fix for CVE-2017-18189
Patch1007: sox-14.4.2-bug_1545867_fix.patch
# 9000 - 9999: Tests:
Patch9000: sox-14.4.2-installcheck_fix.patch
Patch9001: sox-sample_tes-t-c99.patch
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/IJFYI5Q2BYZKIGDFS2WLOBDUSEGWHIKV/
BuildRequires: make
BuildRequires: gcc
BuildRequires: libvorbis-devel
BuildRequires: alsa-lib-devel, libtool-ltdl-devel, libsamplerate-devel
BuildRequires: gsm-devel, wavpack-devel, ladspa-devel, libpng-devel
BuildRequires: flac-devel, libao-devel, libsndfile-devel, libid3tag-devel
BuildRequires: pulseaudio-libs-devel, opusfile-devel
BuildRequires: libtool, libmad-devel, lame-devel, twolame-devel

%description
SoX (Sound eXchange) is a sound file format converter. SoX can convert
between many different digitized sound formats and perform simple
sound manipulation functions, including sound effects.

%package -n  sox-devel
Summary: The SoX sound file format converter libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n sox-devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-downstream-%{name}-%{version}.modified
%patch -P0 -p1
%patch -P1 -p1 -b .lpc
%patch -P2 -p1
%patch -P1000 -p1
%patch -P1001 -p1
%patch -P1002 -p1
%patch -P1003 -p1
%patch -P1004 -p1
%patch -P1005 -p1
%patch -P1006 -p1
%patch -P1007 -p1
%patch -P9000 -p1
%patch -P9001 -p1
#regenerate scripts from older autoconf to support aarch64
autoreconf -vfi

%build
CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%configure --without-lpc10 \
           --with-gsm \
           --includedir=%{_includedir}/sox \
           --disable-static \
           --with-distro=Fedora \
           --with-dyn-default

make V=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libsox.la
rm -f $RPM_BUILD_ROOT%{_libdir}/sox/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/sox/*.a

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %doc}
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/sox
%{_bindir}/soxi
%{_libdir}/libsox.so.*
%dir %{_libdir}/sox/
%{_libdir}/sox/libsox_fmt_*.so
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n sox-devel
%{_includedir}/sox
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%{_mandir}/man3/*

%changelog
%autochangelog
