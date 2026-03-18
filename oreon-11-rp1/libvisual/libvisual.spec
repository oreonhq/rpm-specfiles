%global smallversion 0.4

Name:           libvisual
Version:        0.4.2
Release:        4%{?dist}
Epoch:          1

Summary:        Abstraction library for audio visualisation plugins
License:        LGPL-2.1-or-later
URL:            https://github.com/Libvisual/libvisual
Source0:        https://github.com/Libvisual/libvisual/releases/download/libvisual-%{version}/libvisual-%{version}.tar.bz2

Patch1:         libvisual-0.4.2-respect-environment-ldflags.patch
Patch2:         libvisual-c99.patch

BuildRequires:  automake, autoconf, libtool, autoconf-archive, gettext-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sdl12-compat-devel
BuildRequires:  xorg-x11-proto-devel

%description
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

Often when it comes to audio visualisation plugins or programs that create
visuals they do depend on a player or something else, basically there is no
general framework that enable application developers to easy access cool
audio visualisation plugins. Libvisual wants to change this by providing
an interface towards plugins and applications, through this easy to use
interface applications can easily access plugins and since the drawing is
done by the application it also enables the developer to draw the visual
anywhere he wants.

%package        devel
Summary:        Development files for libvisual
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

This package contains the files needed to build an application with libvisual.

%package        tools
Summary:        Command-line tools for libvisual
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    tools
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

This package contains tools for interacting with libvisual.

%prep
%setup -q
%patch -P1 -p1 -b .respect-environment-ldflags
%patch -P2 -p1 -b .c99
autoreconf -ifv

%build
%configure
%make_build

%install
%make_install

# Avoid multilib conflicts
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv %{buildroot}%{_includedir}/libvisual-%{smallversion}/libvisual/lvconfig.h \
     %{buildroot}%{_includedir}/libvisual-%{smallversion}/libvisual/lvconfig-$wordsize.h

  cat >%{buildroot}%{_includedir}/libvisual-%{smallversion}/libvisual/lvconfig.h <<EOF
#ifndef __LV_CONFIG_H_MULTILIB__
#define __LV_CONFIG_H_MULTILIB__

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "lvconfig-32.h"
#elif __WORDSIZE == 64
# include "lvconfig-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}-%{smallversion}

%files -f %{name}-%{smallversion}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README NEWS TODO AUTHORS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}-%{smallversion}

%files tools
%{_bindir}/lv-tool-%{smallversion}
%{_mandir}/man1/lv-tool-%{smallversion}.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-4
- Prepare for Oreon 11 (RP1)
