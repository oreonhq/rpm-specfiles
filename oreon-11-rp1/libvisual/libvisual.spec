# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2aa5967c5c9522c8d7ab9bd9246c77a582c1aaf4f2b3f06493dbe3066f00380a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global smallversion 0.4

Name:           libvisual
Version:        0.4.2
Release:        1%{?dist}
Epoch:          1

Summary:        Abstraction library for audio visualisation plugins
License:        LGPL-2.1-or-later
URL:            https://github.com/Libvisual/libvisual
Source0:        https://github.com/Libvisual/libvisual/releases/download/libvisual-%{version}/libvisual-%{version}.tar.bz2

Patch1:         libvisual-0.4.2-respect-environment-ldflags.patch
Patch2:         libvisual-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  autoconf-archive
BuildRequires:  gettext-devel
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
%oreon_sha256
%setup -q
%patch -P1 -p1 -b .respect-environment-ldflags
%patch -P2 -p1 -b .c99
autoreconf -ifv

%build
%configure
%make_build

%install
%make_install

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
%autochangelog
