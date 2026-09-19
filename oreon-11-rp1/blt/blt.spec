%global source0_hash 6de705eccf2ec676b4071b74ec9e211c590477fadf6f05566cfd8ed6a03c60da

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary: Widget extension to the Tcl/Tk scripting language
Name: blt
Version: 2.4
Release: 76.z%{?dist}

License: MIT
URL: http://sourceforge.net/projects/blt/
Source0: http://downloads.sourceforge.net/blt/BLT2.4z.tar.gz
#Source0: http://downloads.sourceforge.net/blt/blt-20050731cvs.tgz
Patch0: http://downloads.sourceforge.net/blt/blt2.4z-patch-2
Patch1: http://jfontain.free.fr/blt2.4z-patch-64
Patch2: blt2.4-tk8.5.patch
Patch3: blt2.4z-destdir.patch
Patch4: blt2.4z-norpath.patch
Patch5: blt2.4z-noexactversion.patch
Patch6: blt2.4z-zoomstack.patch
Patch7: blt2.4z-tk8.5.6-patch
Patch8: blt2.4z-tcl8.6.patch
Patch9: blt2.4z-tk8.6.patch
Patch10: blt-configure-c99.patch

Provides: tk-blt = %{version}-%{release}
# Not ready to tk/tcl9
BuildRequires: (tk-devel >= 1:8.4.7 with tk-devel < 1:9) gcc
BuildRequires: make

Requires: (tk8 >= 1:8.4.7 with tk8 < 1:9)
Requires: itcl
Requires: tcl(abi) = 8.6

%description
BLT is a very powerful extension to Tk. It adds plotting widgets
(graph, barchart and stripchart), hierarchy tree and table, tab
notebook, table geometry manager, vector, background program
execution, busy utility, eps canvas item, drag and drop facility,
bitmap command and miscellaneous commands.
Note: this version is stubs enabled and therefore should be compatible
with Tcl/Tk versions after and including 8.3.1.

%package devel
Summary:        Development files for BLT
Requires:       (tk-devel >= 1:8.4.7 with tk-devel < 1:9)
Requires:       %{name} = %{version}-%{release}

%description devel
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry managers
and miscellaneous other commands. Note that you won't need to any patching
of the Tcl or Tk source file to use BLT, but you will need to have Tcl/Tk
installed in order to use BLT.

This package provides headers needed to build packages based on BLT.

%package doc
Summary:        HTML documentation for BLT
BuildArch:      noarch

%description doc
This package provides the html documentation for BLT

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{version}z
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

# Fix bad interpreter path
sed -i -e 's#/usr/local/bin/tclsh#/usr/bin/tclsh8#' demos/scripts/page.tcl

# Rename a couple of files that conflict with other packages
mv man/graph.mann man/bltgraph.mann
mv man/bitmap.mann man/bltbitmap.mann

%build
# This package is not ready for C23, expeciallly for
# C23 strict function prototype change
%global  _pkg_extra_cflags -std=gnu17

# fix RHBZ 1105266
sed -i -e "s|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@'|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@ -ltk -ltcl'|" configure
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} --with-blt=%{tcl_sitelib} --includedir=%{_includedir}/%{name}
pushd src/shared
# no _smp_mflags; race conditions.
make
popd

for file in demos/*.tcl ; do
    sed -i -e 's#../src/bltwish#/usr/bin/wish8#' $file
done
sed -i -e 's#../bltwish#/usr/bin/wish8#' demos/scripts/xcolors.tcl

%install
make install INSTALL_ROOT=%{buildroot}
# Fedora policy is not to generate new shells for Tcl extensions
rm -f %{buildroot}%{_bindir}/bltsh*
rm -f %{buildroot}%{_bindir}/bltwish*
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a
# Remove some doc files from the script area
rm -f %{buildroot}%{tcl_sitelib}/%{name}%{version}/{README,NEWS,PROBLEMS}
# Remove man pages.  HTML documentation is already available.
rm -rf %{buildroot}%{_mandir}/

%ldconfig_scriptlets

%files
%doc README INSTALL PROBLEMS
%{_libdir}/*.so
%{tcl_sitelib}/%{name}%{version}
%{tcl_sitearch}/%{name}%{version}
# Man pages conflict with iwidgets.  This is a common problem among
# Tk widget extensions.
#%{_mandir}/man3/*
#%{_mandir}/mann/*

%files doc
%doc html/

%files devel
%{_includedir}/%{name}

%changelog
%autochangelog
