%global source0_hash 3b749138229e7808d0009a97e2ac47815ad5278df6879a9cc64351a7921ba06f

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global upstream_name FoX

Name:		FoXlibf
Version:	4.1.2
Release:	29%{?dist}
Summary:	A Fortran XML Library
# Automatically converted from old format: zlib and BSD - review is highly recommended.
License:	Zlib AND LicenseRef-Callaway-BSD
URL:		http://www1.gly.bris.ac.uk/~walker/FoX/
Source0:	http://www1.gly.bris.ac.uk/~walker/FoX/source/%{upstream_name}-%{version}.tar.gz
Patch0:		FoX-4.1.2-DESTDIR.patch
Patch1:		FoX-4.1.2-system-paths.patch
Patch2:		FoX-4.1.2-sharedlibs.patch
Patch3:		FoX-4.1.2-dompp.patch
BuildRequires:	gcc-gfortran
BuildRequires: make

%description
FoX is an XML library written in Fortran 95. It allows software developers to
read, write and modify XML documents from Fortran applications without the 
complications of dealing with multiple language development.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for FoX

%description devel
Development files for FoX.

%package static
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Static libraries for FoX

%description static
Static libraries for FoX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{upstream_name}-%{version}
%patch -P0 -p1 -b .DESTDIR
%patch -P1 -p1 -b .system
%patch -P2 -p1 -b .shared

# We need a variant "pretty-print" version of the dom library for exciting
cp -a dom dompp
sed -i "s/ 27293398$/ ibset(27293398,22)/" dompp/m_dom_dom.F90 
sed -i "s|libFoX_dom|libFoX_dompp|g" dompp/makefile

%patch -P3 -p1 -b .dompp

%build
export FCFLAGS="%{optflags} %{?_fmoddir: -I%_fmoddir} -fPIC"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
pushd %{buildroot}%{_libdir}
for i in libFoX_common libFoX_dom libFoX_dompp libFoX_fsys libFoX_sax libFoX_utils libFoX_wcml libFoX_wkml libFoX_wxml; do
	ln -s $i.so.0.0.0 $i.so.0
	ln -s $i.so.0.0.0 $i.so
done
chmod -x %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc README.FoX.txt
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libFoX*.so.*

%files devel
%{_bindir}/FoX-config
%{_includedir}/FoX/
%{_libdir}/libFoX*.so

%files static
%{_libdir}/libFoX*.a

%changelog
%autochangelog
