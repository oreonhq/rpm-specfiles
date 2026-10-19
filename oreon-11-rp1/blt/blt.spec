%global source0_hash 6de705eccf2ec676b4071b74ec9e211c590477fadf6f05566cfd8ed6a03c60da
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}
Summary:        Widget extension to the Tcl/Tk scripting language
Name: blt
Version: 2.4
Release:        1%{?dist}
License: MIT
URL: http://sourceforge.net/projects/blt/
Source0:        http://downloads.sourceforge.net/blt/BLT2.4z.tar.gz
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
Requires: (tk8 >= 1:8.4.7 with tk8 < 1:9)
Requires: itcl
Requires: tcl(abi) = 8.6
# oreon:deps
BuildRequires:  (tk-devel >= 1:8.4.7 with tk-devel < 1:9)
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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

%global  _pkg_extra_cflags -std=gnu17
sed -i -e "s|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@'|SHLIB_LD_FLAGS='-rdynamic -shared -Wl,-E -Wl,-soname,\$@ -ltk -ltcl'|" configure
%configure --with-tcl=%{_libdir} --with-tk=%{_libdir} --with-blt=%{tcl_sitelib} --includedir=%{_includedir}/%{name}
pushd src/shared
make
popd
for file in demos/*.tcl ; do
    sed -i -e 's#../src/bltwish#/usr/bin/wish8#' $file
done
sed -i -e 's#../bltwish#/usr/bin/wish8#' demos/scripts/xcolors.tcl
%install
make install INSTALL_ROOT=%{buildroot}
rm -f %{buildroot}%{_bindir}/bltsh*
rm -f %{buildroot}%{_bindir}/bltwish*
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{tcl_sitelib}/%{name}%{version}/{README,NEWS,PROBLEMS}
rm -rf %{buildroot}%{_mandir}/
%ldconfig_scriptlets
%oreon_autofiles blt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles blt-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n blt-devel -f %{oreon_filedir}/blt-devel.list
%files -n blt-doc -f %{oreon_filedir}/blt-doc.list

%changelog

%autochangelog
