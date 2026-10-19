%global source0_hash a1d8cbe44b38beaa29fc2130c4e7b79b8bf02e2bcc028ffefd7a25a2122202a0
%define majorver 8.6
%define	vers %{majorver}.17
%{!?sdt:%define sdt 1}
Summary:        Tool Command Language, pronounced tickle, version 8
Name: tcl8
Version: %{vers}
Release:        1%{?dist}
Epoch: 1
License: TCL AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
URL: http://tcl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/tcl/tcl-core%{version}-src.tar.gz
Provides: tcl(abi) = %{majorver}
Provides: tcl-tcldict = %{vers}
Patch: tcl-8.6.15-autopath.patch
Patch: tcl-8.6.15-conf.patch
Patch: tcl-8.6.13-tcltests-path-fix.patch
Patch: tcl-8.6.13-configure-c99.patch
%if %sdt
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package devel
Summary: Tcl scripting language development environment
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: tcl-devel = %{epoch}:%{version}-%{release}
Conflicts: tcl-devel >= 1:9.0.0-1
%description devel
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

The package contains the development files and man pages for tcl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tcl%{version}
rm -r compat/zlib

%build

pushd unix
autoconf
%configure \
%if %sdt
--enable-dtrace \
%endif
--enable-threads \
--enable-symbols \
--enable-shared
%make_build CFLAGS="%{optflags}" TCL_LIBRARY=%{_datadir}/tcl%{majorver}
%check

%{?_without_check: %define _without_check 1}
%{!?_without_check: %define _without_check 0}
%if ! %{_without_check}
  cd unix
  make test
%endif
%install
make install -C unix INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{_datadir}/tcl%{majorver}
ln -s tclsh%{majorver} %{buildroot}%{_bindir}/tclsh8
ln -s libtcl%{majorver}.so %{buildroot}%{_libdir}/libtcl.so
mkdir -p %{buildroot}/%{_libdir}/tcl%{majorver}
ln -s %{_libdir}/tclConfig.sh %{buildroot}/%{_libdir}/tcl%{majorver}/tclConfig.sh
mkdir -p %{buildroot}/%{_includedir}/tcl-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}/%{_includedir}/tcl-private/'{}' ';'
( cd %{buildroot}/%{_includedir}
	for i in *.h ; do
		[ -f %{buildroot}/%{_includedir}/tcl-private/generic/$i ] && ln -sf ../../$i %{buildroot}/%{_includedir}/tcl-private/generic ;
	done
)
sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/tcl-private|" %{buildroot}/%{_libdir}/tclConfig.sh
rm -rf %{buildroot}/%{_datadir}/tcl%{majorver}/ldAix
mv %{buildroot}/%{_mandir}/man1/tclsh.1 %{buildroot}/%{_mandir}/man1/tclsh8.1
rm -f %{buildroot}%{_mandir}/man3/* %{buildroot}%{_mandir}/mann/*
rmdir %{buildroot}%{_mandir}/man3 %{buildroot}%{_mandir}/mann
%if 0%{?flatpak}
mkdir -p %{buildroot}%{_usr}/bin
ln -s %{_bindir}/tclsh8 %{_bindir}/tclsh%{majorver} %{buildroot}%{_usr}/bin/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n tcl8-devel -f %{oreon_filedir}/tcl8-devel.list

%changelog

%autochangelog
