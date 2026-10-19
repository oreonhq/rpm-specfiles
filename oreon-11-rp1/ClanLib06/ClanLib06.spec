%global source0_hash b301ace86fcc371805d6299e00bc8b51996ec20a4f1c04e0bffb522ef66a5341
Summary:        Version 0.6 of this Cross platform C++ game library
Name:           ClanLib06
Version:        0.6.5
Release:        68%{?dist}
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.clanlib.org/
Source0:        ClanLib-%{version}-1.tar.gz
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
Provides:       clanlib06 = %{version}-%{release}
# oreon:deps
BuildRequires:  Hermes-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mikmod-devel
BuildRequires:  tolua++-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
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
make
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.a
chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/clanlib-config.1*
%ldconfig_scriptlets
%oreon_autofiles ClanLib06-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ClanLib06-devel -f %{oreon_filedir}/ClanLib06-devel.list

%changelog

%autochangelog
