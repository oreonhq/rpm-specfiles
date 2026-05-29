%global source0_hash none

%global major 9
%global majorver %{major}.0
%global vers %{majorver}.2

Summary: The graphical toolkit for the Tcl scripting language
Name: tk
Version: %{vers}
Release: 1%{?dist}
Epoch:   1
License: TCL AND HPND-Pbmplus AND CC-BY-SA-3.0 AND MIT-open-group AND MIT
URL: http://tcl.sourceforge.net
Source0:        http://download.sourceforge.net/sourceforge/tcl/tk-src.tar.gz
Requires: tcl = %{epoch}:%{vers}
BuildRequires: make
BuildRequires: gcc
BuildRequires: tcl-devel = %{epoch}:%{vers}, autoconf
BuildRequires: libX11-devel
BuildRequires: libXft-devel
# panedwindow.n from itcl conflicts
Conflicts: itcl <= 3.2
Obsoletes: tile <= 0.8.2
Provides: tile = 0.8.2
Patch: tk-8.6.12-make.patch
Patch: tk-8.6.15-conf.patch

%description
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

%package devel
Summary: Tk graphical toolkit development files
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tcl-devel = %{epoch}:%{vers}
Requires: libX11-devel libXft-devel
Conflicts: tk8-devel

%description devel
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

The package contains the development files and man pages for tk.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}%{vers}

%build
cd unix
autoconf
%configure --enable-threads \
--disable-zipfs
%make_build CFLAGS="%{optflags}" TK_LIBRARY=%{_datadir}/%{name}%{majorver}

%check
# do not run "make test" by default since it requires an X display
%{?_with_check: %define _with_check 1}
%{!?_with_check: %define _with_check 0}

%if %{_with_check}
#  make test
%endif

%install
make install -C unix INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{_datadir}/%{name}%{majorver}

ln -s wish%{majorver} %{buildroot}%{_bindir}/wish

# for linking with -l%%{name}
ln -s libtcl%{major}%{name}%{majorver}.so %{buildroot}%{_libdir}/lib%{name}.so

mkdir -p %{buildroot}/%{_includedir}/%{name}-private/{generic/ttk,unix}
find generic unix -name "*.h" -exec cp -p '{}' %{buildroot}/%{_includedir}/%{name}-private/'{}' ';'
( cd %{buildroot}/%{_includedir}
  for i in *.h ; do
    [ -f %{buildroot}/%{_includedir}/%{name}-private/generic/$i ] && ln -sf ../../$i %{buildroot}/%{_includedir}/%{name}-private/generic ;
  done
)

# remove buildroot traces
sed -i -e "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" %{buildroot}/%{_libdir}/%{name}Config.sh

%if 0%{?flatpak}
mkdir -p %{buildroot}%{_usr}/bin
ln -s %{_bindir}/wish %{_bindir}/wish%{majorver} %{buildroot}%{_usr}/bin/
%endif

%pre
[ ! -h %{_prefix}/%{_lib}/%{name}%{majorver} ] || rm %{_prefix}/%{_lib}/%{name}%{majorver}

%ldconfig_scriptlets

%files
%{_bindir}/wish*
%{_datadir}/%{name}%{majorver}
%{_libdir}/libtcl%{major}%{name}%{majorver}.so
%{_libdir}/%{name}%{majorver}
%{_mandir}/man1/*
%{_mandir}/mann/*
%if 0%{?flatpak}
%{_usr}/bin/wish*
%endif
%doc README.md changes.md license.terms

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}stub.a
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}Config.sh
%{_libdir}/pkgconfig/tk.pc
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{vers}-1
- Prepare for Oreon 11 (RP1)
