%global source1_hash fbfcfaf7aebd713051c2a9ab500a273e9a11c882e0f1b4bf3ea8a5525cf7f2a9
%global source0_hash ded93d519ea6aa153f6a7bd13b6782eefe9f2e44b15e2f699bf356558bbbf74b
%global		gittag	4_1_1
Name:		ogdi
Version:	4.1.1
Release:        1%{?dist}
Summary:        Open Geographic Datastore Interface
License:	LicenseRef-Callaway-BSD
URL:		http://ogdi.sourceforge.net/
Source0:        https://github.com/lib%{name}/%{name}/archive/%{name}_%{gittag}.tar.gz
Source1:	http://ogdi.sourceforge.net/ogdi.pdf
Patch0:		ogdi-4.1.0-sailer.patch
Obsoletes:	%{name}-odbc < 4.1.1
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  libtirpc-devel
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
OGDI is the Open Geographic Datastore Interface. OGDI is an
application programming interface (API) that uses a standardized
access methods to work in conjunction with GIS software packages (the
application) and various geospatial data products. OGDI uses a
client/server architecture to facilitate the dissemination of
geospatial data products over any TCP/IP network, and a
driver-oriented approach to facilitate access to several geospatial
data products/formats.

%package devel
Summary:	OGDI header files and documentation
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	zlib-devel expat-devel
%description devel
OGDI header files and developer's documentation.

%package tcl
Summary:	TCL wrapper for OGDI
Requires:	%{name} = %{version}-%{release}
%description tcl
TCL wrapper for OGDI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}_%{gittag}

# include documentation
%{__cp} -p %{SOURCE1} .

# remove unbundled stuff
rm -rf external
sed -i '/^subdirs/s/external //' makefile

%build

TOPDIR=`pwd`; TARGET=Linux; export TOPDIR TARGET
INST_LIB=%{_libdir}/;export INST_LIB
export CFG=debug # for -g
export CFLAGS="$RPM_OPT_FLAGS -DDONT_TD_VOID -DUSE_TERMIO -std=gnu17"
%configure \
	--with-binconfigs \
	--with-expat \
	--with-zlib
%{__make}
%{__make} -C ogdi/tcl_interface \
	TCL_LINKLIB="-ltcl"
%{__make} -C contrib/gdal
%install
TOPDIR=`pwd`; TARGET=Linux; export TOPDIR TARGET
%{__make} install \
	INST_INCLUDE=%{buildroot}%{_includedir}/%{name} \
	INST_LIB=%{buildroot}%{_libdir} \
	INST_BIN=%{buildroot}%{_bindir}
%{__make} install -C ogdi/tcl_interface \
	INST_LIB=%{buildroot}%{_libdir}
%{__make} install -C contrib/gdal \
	INST_LIB=%{buildroot}%{_libdir}
%{__rm} %{buildroot}%{_bindir}/example?
%if "%{_lib}" == "lib"
%global cpuarch 32
%else
%global cpuarch 64
%endif
touch -r ogdi-config.in ogdi-config
%{__mkdir} -p %{buildroot}%{_libdir}/pkgconfig
%{__install} -p -m 644 ogdi.pc %{buildroot}%{_libdir}/pkgconfig/
%{__install} -p -m 755 ogdi-config %{buildroot}%{_bindir}/ogdi-config-%{cpuarch}
cat > %{buildroot}%{_bindir}/%{name}-config <<EOF
ARCH=\$(uname -m)
case \$ARCH in
x86_64 | ppc64 | ppc64le | ia64 | s390x | sparc64 | alpha | alphaev6 | aarch64 )
ogdi-config-64 \${*}
;;
*)
ogdi-config-32 \${*}
;;
esac
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}-config
touch -r ogdi-config.in %{buildroot}%{_bindir}/%{name}-config
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ogdi-devel -f %{oreon_filedir}/ogdi-devel.list
%files -n ogdi-tcl -f %{oreon_filedir}/ogdi-tcl.list

%changelog

%autochangelog
