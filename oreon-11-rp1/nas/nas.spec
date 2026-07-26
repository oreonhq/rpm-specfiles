%global source0_hash b7884afb38feec03a196bd3b7e9c47b803c830ecd10d7455e9c97e122c37944c

Name:       nas 
Summary:    The Network Audio System (NAS)
Version:    1.9.5
Release:    15%{?dist}
URL:        http://radscan.com/nas.html
# README:               MIT (main license)
# lib/audio/aiff.c          MIT (with Apple warranty declaration)
# server/dda/voxware/auvoxware.h:
#                           (MIT) and
#                           (something similar to MIT license by SCO)
# server/dda/sun/ausuni.c:  (MIT) and
#                           (something similar to MIT)
## Not in any binary package
# config/aclocal.m4:    FSFULLR
# config/config.guess:  GPLv2+ with exceptions, effectively same as main license
# config/config.sub:    GPL with exceptions, effectively same as main license
# config/configure:     FSFUL
# config/install-sh:    MIT
# config/ltmain.sh:     GPLv2+ with exceptions, effectively same as main license
## Unused
# contrib/nasbugs/Aproto.h: MIT
# contrib/nasbugs/audio.h:  MIT
# contrib/xemacs/nas.c:     MIT
License:    MIT
%define daemon nasd
Source0:    https://sourceforge.net/projects/nas/files/nas/nas-%{version}/nas-%{version}.tar.gz
Source1:    %{daemon}.service
Source2:    %{daemon}.sysconfig
# Move noarch data to /usr/share
Patch0:     nas-1.9.3-Move-AuErrorDB-to-SHAREDIR.patch
# Adapt to GCC 14, in upstream after 1.9.5,
# bug #2149230, <https://sourceforge.net/p/nas/bugs/10/>
Patch1:     nas-1.9.5-No-implicit-ints-and-function-declarations.patch
# Respect linker flags when linking shared libraries, in upstream after 1.9.5,
# <https://sourceforge.net/p/nas/bugs/11/>
Patch2:     nas-1.9.5-Pass-extra-linker-flags-to-shared-libraries.patch
# Adapt pointer types to GCC 14, bug #2261396, in upstream after 1.9.5,
# <https://sourceforge.net/p/nas/bugs/12/>
Patch3:     nas-1.9.5-Correct-pointer-types-for-GCC-14.patch
# Adapt to API changes in libXaw-1.0.16, bug #2276343, in upstream after
# 1.9.5, <https://sourceforge.net/p/nas/bugs/14/>
Patch4:     nas-1.9.5-Adapt-to-libXaw-1.0.16.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
# Update config.sub to support aarch64, bug #926196
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       %{name}-libs = %{version}-%{release}

%package devel
Summary:    Development and doc files for the NAS 
Requires:   %{name}-libs = %{version}-%{release}

%package libs
Summary:    Run-time libraries for NAS

%description
In a nutshell, NAS is the audio equivalent of an X display server.  The
Network Audio System (NAS) was developed for playing, recording, and
manipulating audio data over a network.  Like the X Window System, it uses the
client/server model to separate applications from the specific drivers that
control audio input and output devices.

Key features of the Network Audio System include:
    • Device-independent audio over the network
    • Lots of audio file and data formats
    • Can store sounds in server for rapid replay
    • Extensive mixing, separating, and manipulation of audio data
    • Simultaneous use of audio devices by multiple applications
    • Use by a growing number of ISVs
    • Small size
    • Free!  No obnoxious licensing terms

%description libs
%{summary}.

%description devel
Development files and the documentation for Network Audio System.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Update config.sub to support aarch64, bug #926196
cp -p %{_datadir}/automake-*/config.{sub,guess} config
sed -i -e '/AC_FUNC_SNPRINTF/d' config/configure.ac
autoreconf -i -f config

# Fails to build since GCC 15 which moved a default language standard tp ISO
# C23. Porting nas to C23 is a big task probably not worth of this legacy
# code.
%global _pkg_extra_cflags -std=c99

%build
xmkmf
# See HISTORY file how to modify CDEBUGFLAGS
%make_build WORLDOPTS='-k CDEBUGFLAGS="%{build_cflags}" -k EXTRA_LDOPTIONS="%{build_ldflags}"' World

%install
%make_install BINDIR=%{_bindir} INCROOT=%{_includedir} \
  LIBDIR=%{_libdir}/X11  SHLIBDIR=%{_libdir} USRLIBDIR=%{_libdir} \
  MANPATH=%{_mandir} INSTALLFLAGS='-p' EXTRA_LDOPTIONS='%{__global_ldflags}' \
  install.man

# Systemd integration
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{daemon}.service
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{daemon}

# Rename a config file
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/nasd.conf{.eg,}

# Remove the static libraries
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.a

%post
%systemd_post %{daemon}.service

%preun
%systemd_preun %{daemon}.service

%postun
%systemd_postun_with_restart %{daemon}.service

%files
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/nasd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{daemon}
%{_unitdir}/%{daemon}.service
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files libs
%doc FAQ HISTORY README TODO
%{_libdir}/libaudio.so.*
%{_datadir}/X11/AuErrorDB

%files devel
%doc doc/actions doc/protocol.txt doc/*.ps
%{_includedir}/audio/
%{_libdir}/libaudio.so
%{_mandir}/man3/*

%changelog
%autochangelog
