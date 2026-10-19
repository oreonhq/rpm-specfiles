%global source0_hash e4982df6f969c08bf9dd858a6891059b4a3f50dc6c87c10abadbbe2fc4838946
%define majorver 8.6
%define vers %{majorver}.17
Summary:        The graphical toolkit for the Tcl scripting language, version 8
Name: tk8
Version: %{vers}
Release:        2%{?dist}
Epoch:   1
License: TCL AND HPND-Pbmplus AND CC-BY-SA-3.0 AND MIT-open-group AND MIT
URL: http://tcl.sourceforge.net
Source0:        http://download.sourceforge.net/sourceforge/tcl/tk%{version}-src.tar.gz
Requires: tcl8 = %{epoch}:%{vers}
Conflicts: itcl <= 3.2
Provides: tile = 0.8.2
Patch: tk-8.6.12-make.patch
Patch: tk-8.6.15-conf.patch
Patch: tk-8.6.10-font-sizes-fix.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  tcl8-devel
# /oreon:deps
%description
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

%package devel
Summary: Tk graphical toolkit development files
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tcl8-devel = %{epoch}:%{vers}
Requires: libX11-devel libXft-devel
Provides: tk-devel = %{epoch}:%{version}-%{release}
Conflicts: tk-devel >= 1:9.0.0-1
%description devel
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

The package contains the development files and man pages for tk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tk%{vers}

%build

cd unix
autoconf
%configure --enable-threads
%make_build CFLAGS="%{optflags}" TK_LIBRARY=%{_datadir}/tk%{majorver}
%check

%{?_with_check: %define _with_check 1}
%{!?_with_check: %define _with_check 0}
%if %{_with_check}
%endif
%install
make install -C unix INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{_datadir}/tk%{majorver}
ln -s wish%{majorver} %{buildroot}%{_bindir}/wish8
ln -s libtk%{majorver}.so %{buildroot}%{_libdir}/libtk.so
mkdir -p %{buildroot}/%{_includedir}/tk-private/{generic/ttk,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}/%{_includedir}/tk-private/'{}' ';'
( cd %{buildroot}/%{_includedir}
  for i in *.h ; do
    [ -f %{buildroot}/%{_includedir}/tk-private/generic/$i ] && ln -sf ../../$i %{buildroot}/%{_includedir}/tk-private/generic ;
  done
)
sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/tk-private|" %{buildroot}/%{_libdir}/tkConfig.sh
mv %{buildroot}/%{_mandir}/man1/wish.1 %{buildroot}/%{_mandir}/man1/wish8.1
rm -f %{buildroot}%{_mandir}/mann/*
rmdir %{buildroot}%{_mandir}/mann
%if 0%{?flatpak}
mkdir -p %{buildroot}%{_usr}/bin
ln -s %{_bindir}/wish8 %{_bindir}/wish%{majorver} %{buildroot}%{_usr}/bin/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%pre

[ ! -h %{_prefix}/%{_lib}/tk%{majorver} ] || rm %{_prefix}/%{_lib}/tk%{majorver}
%files -f %{oreon_filedir}/main.list
%files -n tk8-devel -f %{oreon_filedir}/tk8-devel.list

%changelog

%autochangelog
