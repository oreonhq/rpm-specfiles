%global source0_hash 5d265f3499b588681825d8093177830707b7035ad866b17189a3a6ab6dade0ff
%global xver 9
%global yver 0
%global zver 4
%global majorver %{xver}.%{yver}
%global vers %{majorver}.%{zver}
%{!?sdt:%global sdt 1}
Summary:        Tool Command Language, pronounced tickle
Name: tcl
Version: %{vers}
Release:        1%{?dist}
Epoch: 1
License: TCL AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
URL: http://tcl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/tcl/tcl-core%{version}-src.tar.gz
Provides: bundled(libtommath) = 1.3.0
Provides: tcl(abi) = %{majorver}
Obsoletes: tcl-tcldict <= %{vers}
Provides: tcl-tcldict = %{vers}
Provides: bundled(zlib) = 1.3.1
Patch: tcl-9.0.2-autopath.patch
Patch: tcl-8.6.15-conf.patch
Patch: tcl-9.0.0-tcltests-path-fix.patch
%if %sdt
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
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

%package doc
Summary: Tcl documentation
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
TCL documentation.

%package devel
Summary: Tcl scripting language development environment
Requires: %{name} = %{epoch}:%{version}-%{release}
Conflicts: tcl8-devel
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
%global oreon_srcdir %{name}%{version}
%oreon_prep
%build

pushd unix
autoconf
%configure \
%if %sdt
--enable-dtrace \
%endif
--enable-symbols \
--enable-shared \
--with-system-libtommath%{!?fedora:=no} \
--disable-rpath
%make_build CFLAGS="%{optflags}" TCL_LIBRARY=%{_datadir}/%{name}%{majorver}
%check

%{?_without_check: %define _without_check 1}
%{!?_without_check: %define _without_check 0}
%if ! %{_without_check}
  cd unix
  make test
%endif
%install
make install install-libraries install-msgs -C unix INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{_datadir}/%{name}%{majorver}
ln -s tclsh%{majorver} %{buildroot}%{_bindir}/tclsh
ln -s lib%{name}%{majorver}.so %{buildroot}%{_libdir}/lib%{name}.so
mkdir -p %{buildroot}/%{_libdir}/%{name}%{majorver}
ln -s %{_libdir}/%{name}Config.sh %{buildroot}/%{_libdir}/%{name}%{majorver}/%{name}Config.sh
mkdir -p %{buildroot}/%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}/%{_includedir}/%{name}-private/'{}' ';'
( cd %{buildroot}/%{_includedir}
	for i in *.h ; do
		[ -f %{buildroot}/%{_includedir}/%{name}-private/generic/$i ] && ln -sf ../../$i %{buildroot}/%{_includedir}/%{name}-private/generic ;
	done
)
sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" %{buildroot}/%{_libdir}/%{name}Config.sh
rm -rf %{buildroot}/%{_datadir}/%{name}%{majorver}/ldAix
%if 0%{?flatpak}
mkdir -p %{buildroot}%{_usr}/bin
ln -s %{_bindir}/tclsh %{_bindir}/tclsh%{majorver} %{buildroot}%{_usr}/bin/
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tcl-doc -f %{oreon_filedir}/tcl-doc.list
%files -n tcl-devel -f %{oreon_filedir}/tcl-devel.list

%changelog

%autochangelog
