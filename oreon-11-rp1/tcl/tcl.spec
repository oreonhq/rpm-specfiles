# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5d265f3499b588681825d8093177830707b7035ad866b17189a3a6ab6dade0ff

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global xver 9
%global yver 0
%global majorver %{xver}.%{yver}

Name:           tcl
Version:        %{majorver}.4
Release:        1%{?dist}
Epoch:          1
Summary:        Tool Command Language, pronounced tickle
License:        TCL AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
URL:            https://www.tcl-lang.org/
Source0:        https://downloads.sourceforge.net/sourceforge/tcl/tcl-core%{version}-src.tar.gz
Patch0:         tcl-9.0.2-autopath.patch
Patch1:         tcl-8.6.15-conf.patch
Patch2:         tcl-9.0.0-tcltests-path-fix.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace

Provides:       bundled(libtommath) = 1.3.0
Provides:       bundled(zlib) = 1.3.2
Provides:       tcl(abi) = %{majorver}
Provides:       /usr/bin/tclsh
Provides:       /usr/bin/tclsh%{majorver}
Obsoletes:      tcl-tcldict <= %{version}
Provides:       tcl-tcldict = %{version}

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fast and powerful way to create
cross-platform GUI applications. Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package doc
Summary:        Tcl documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description doc
Tcl library and command manual pages.

%package devel
Summary:        Tcl scripting language development environment
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Conflicts:      tcl8-devel

%description devel
Headers, stub library, tclConfig.sh and pkg-config file needed to build
software that embeds or links against Tcl.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}%{version}

%build
pushd unix
autoconf
%configure \
    --enable-dtrace \
    --enable-symbols \
    --enable-shared \
    --with-system-libtommath=no \
    --disable-rpath
%make_build CFLAGS="%{optflags}" TCL_LIBRARY=%{_datadir}/%{name}%{majorver}
popd

%install
make install install-libraries install-msgs -C unix INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{_datadir}/%{name}%{majorver}

ln -s tclsh%{majorver} %{buildroot}%{_bindir}/tclsh
ln -s lib%{name}%{majorver}.so %{buildroot}%{_libdir}/lib%{name}.so

mkdir -p %{buildroot}%{_libdir}/%{name}%{majorver}
ln -s %{_libdir}/%{name}Config.sh %{buildroot}%{_libdir}/%{name}%{majorver}/%{name}Config.sh

mkdir -p %{buildroot}%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}%{_includedir}/%{name}-private/'{}' ';'
( cd %{buildroot}%{_includedir}
  for i in *.h ; do
    [ -f %{buildroot}%{_includedir}/%{name}-private/generic/$i ] && ln -sf ../../$i %{buildroot}%{_includedir}/%{name}-private/generic ;
  done
)

sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" %{buildroot}%{_libdir}/%{name}Config.sh
rm -rf %{buildroot}%{_datadir}/%{name}%{majorver}/ldAix

%check
cd unix
make test

%ldconfig_scriptlets

%files
%license license.terms
%doc README.md changes.md
%{_bindir}/tclsh*
%{_datadir}/%{name}%{xver}
%{_datadir}/%{name}%{majorver}
%{_libdir}/lib%{name}%{majorver}.so
%{_mandir}/man1/*
%dir %{_libdir}/%{name}%{majorver}

%files doc
%{_mandir}/man3/*
%{_mandir}/mann/*

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}stub.a
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}Config.sh
%{_libdir}/%{name}ooConfig.sh
%{_libdir}/%{name}%{majorver}/%{name}Config.sh
%{_libdir}/pkgconfig/tcl.pc

%changelog
%autochangelog
