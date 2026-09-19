%global source0_hash b301ace86fcc371805d6299e00bc8b51996ec20a4f1c04e0bffb522ef66a5341

Summary:        Version 0.6 of this Cross platform C++ game library
Name:           ClanLib06
Version:        0.6.5
Release:        68%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.clanlib.org/
# No URL as this old version is no longer available on clanlib.org
Source0:        ClanLib-%{version}-1.tar.gz
# prebuild docs to avoid multilib conflicts. To regenerate untar and configure,
# cd Documentation, make, make install HTML_PREFIX=`pwd`/html, cd ..,
# tar cvfz ClanLib-%%{version}-generated-docs.tar.gz Documentation/html
Source1:        ClanLib-%{version}-generated-docs.tar.gz
Patch0:         ClanLib-0.6.5-debian.patch
Patch1:         ClanLib-0.6.5-suse.patch
Patch2:         ClanLib-0.6.5-tolua++.patch
Patch3:         ClanLib-0.6.5-smalljpg.patch
Patch4:         ClanLib-0.6.5-gcc4.3.patch
Patch5:         ClanLib-0.6.5-mikmod32.patch
Patch6:         ClanLib-0.6.5-alsa.patch
Patch7:         ClanLib-0.6.5-extra-keys.patch
Patch8:         ClanLib-0.6.5-xev-keycodes.patch
Patch9:         ClanLib-0.6.5-iterator-abuse.patch
Patch10:        ClanLib-0.6.5-gcc4.6.patch
Patch11:        ClanLib-0.6.5-gzopen-flags.patch
Patch12:        ClanLib-0.6.5-libpng15.patch
Patch13:        ClanLib-0.6.5-lua52.patch
Patch14:        ClanLib-0.6.5-gcc6.patch
Patch15:        ClanLib-0.6.5-xwayland-fixes.patch
Patch16:        ClanLib-0.6.5-resolution-sort-fix.patch
Patch17:        ClanLib-0.6.5-numpad-keys-fix.patch
Patch18:        ClanLib-0.6.5-compiler-warnings.patch
Patch19:        ClanLib-header.patch
Patch20:        ClanLib-0.6.5-joystick.patch
Patch21:        ClanLib-0.6.5-fix-ldflags-use.patch
Patch22:        ClanLib-0.6.5-use-pthread_mutexattr_settype.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  libX11-devel libXext-devel libXt-devel libGLU-devel
BuildRequires:  libICE-devel libXxf86vm-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel libpng-devel libjpeg-devel mikmod-devel
BuildRequires:  alsa-lib-devel Hermes-devel freetype-devel autoconf
BuildRequires:  tolua++-devel >= 1.0.93-14
Provides:       clanlib06 = %{version}-%{release}

%description
Version 0.6 of this cross platform C++ game library, which is still used
by many games.

%package devel
Summary:        Development files for ClanLib 0.6
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel Hermes-devel mikmod-devel libpng-devel
Provides:       clanlib06-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use ClanLib 0.6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1 -n ClanLib-%{version}
# mark asm files as NOT needing execstack
for i in `find Sources -name '*.s'`; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done
autoconf

%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-unused-result -Wno-write-strings -Wno-char-subscripts -Wno-deprecated-declarations"
%ifarch %{ix86}
ARCH_CONFIG_FLAGS=--enable-asm386
%endif
%configure --disable-debug --enable-dyn --disable-directfb $ARCH_CONFIG_FLAGS
tolua++ -o Sources/Lua/clanbindings.cpp Sources/Lua/clanbindings.pkg
# no smpflags, it somehow breaks the libs, causing a crash on exit like this:
#0  0x00007ffff7ecee98 in CL_Signal_v2<CL_InputDevice*, CL_Key const&>::~CL_Signal_v2() () from /lib64/libclanJPEG.so.2
#1  0x00007ffff786a48e in __cxa_finalize () from /lib64/libc.so.6
#2  0x00007ffff7e44367 in __do_global_dtors_aux () from /lib64/libclanPNG.so.2
#3  0x00007fffffffd1d0 in ?? ()
#4  0x00007ffff7fe213b in _dl_fini () from /lib64/ld-linux-x86-64.so.2
make

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.a
chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/clanlib-config.1*

%ldconfig_scriptlets

%files
%doc CREDITS NEWS ascii-logo
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README README.gui README.upgrade Documentation/html
%{_bindir}/clanlib-config
%{_libdir}/*.so
%{_includedir}/ClanLib
%{_mandir}/man1/clanlib-config.1.gz

%changelog
%autochangelog
