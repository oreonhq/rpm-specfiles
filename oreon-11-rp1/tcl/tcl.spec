%global source0_hash none

%global xver 9
%global yver 0
%global zver 2

%global majorver %{xver}.%{yver}
%global vers %{majorver}.%{zver}
%{!?sdt:%global sdt 1}

Summary: Tool Command Language, pronounced tickle
Name: tcl
Version: %{vers}
Release: 1%{?dist}
Epoch: 1
License: TCL AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
URL: http://tcl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/tcl/tcl-core%{version}-src.tar.gz
BuildRequires: make
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: zlib-devel
%if 0%{?fedora}
BuildRequires: libtommath-devel
%else
Provides: bundled(libtommath) = 1.3.0
%endif
Provides: tcl(abi) = %{majorver}
Obsoletes: tcl-tcldict <= %{vers}
Provides: tcl-tcldict = %{vers}
# https://bugzilla.redhat.com/show_bug.cgi?id=2318255
Provides: bundled(zlib) = 1.3.1
Patch: tcl-9.0.2-autopath.patch
Patch: tcl-8.6.15-conf.patch
Patch: tcl-9.0.0-tcltests-path-fix.patch

%if %sdt
BuildRequires: systemtap-sdt-dtrace
BuildRequires: systemtap-sdt-devel
%endif

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
%autosetup -p1 -n %{name}%{version}
# uncomment the following line when fixed https://bugzilla.redhat.com/show_bug.cgi?id=2318255
#rm -r compat/zlib

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
# install-libraries install-msgs is workaround for
# https://core.tcl-lang.org/tcl/tktview/3d6d7523525d19ffe95109e08a90f2413c956f82
make install install-libraries install-msgs -C unix INSTALL_ROOT=%{buildroot} TCL_LIBRARY=%{_datadir}/%{name}%{majorver}

ln -s tclsh%{majorver} %{buildroot}%{_bindir}/tclsh

# for linking with -lib%%{name}
ln -s lib%{name}%{majorver}.so %{buildroot}%{_libdir}/lib%{name}.so

mkdir -p %{buildroot}/%{_libdir}/%{name}%{majorver}

# postgresql and maybe other packages too need tclConfig.sh
# paths don't look at /usr/lib for efficiency, so we symlink into tcl8.6 for now
ln -s %{_libdir}/%{name}Config.sh %{buildroot}/%{_libdir}/%{name}%{majorver}/%{name}Config.sh

mkdir -p %{buildroot}/%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}/%{_includedir}/%{name}-private/'{}' ';'
( cd %{buildroot}/%{_includedir}
	for i in *.h ; do
		[ -f %{buildroot}/%{_includedir}/%{name}-private/generic/$i ] && ln -sf ../../$i %{buildroot}/%{_includedir}/%{name}-private/generic ;
	done
)

# remove buildroot traces
sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" %{buildroot}/%{_libdir}/%{name}Config.sh
rm -rf %{buildroot}/%{_datadir}/%{name}%{majorver}/ldAix

%if 0%{?flatpak}
mkdir -p %{buildroot}%{_usr}/bin
ln -s %{_bindir}/tclsh %{_bindir}/tclsh%{majorver} %{buildroot}%{_usr}/bin/
%endif

%ldconfig_scriptlets

%files
%{_bindir}/tclsh*
%{_datadir}/%{name}%{xver}
%{_datadir}/%{name}%{majorver}
%{_libdir}/lib%{name}%{majorver}.so
%{_mandir}/man1/*
%if 0%{?flatpak}
%{_usr}/bin/tclsh*
%endif
%dir %{_libdir}/%{name}%{majorver}
%doc README.md changes.md
%doc license.terms

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{vers}-1
- Prepare for Oreon 11 (RP1)
