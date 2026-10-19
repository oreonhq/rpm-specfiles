%global source0_hash 6d24734aef46d1dc16f3476685414794d6a4e65f48079e1029374477104e8319
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%(echo 'puts $tcl_version' | tclsh)}
Name:           tdom
Version:        0.9.6
Release:        1%{?dist}
Summary:        DOM parser for Tcl
License:        MPL-2.0 AND MIT
URL:            http://www.tdom.org
Source0:        http://tdom.org/downloads/%{name}-%{version}-src.tgz
Requires:       tcl(abi) >= 8.5
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
# /oreon:deps
%description
tDOM combines high performance XML data processing with easy and powerful Tcl
scripting functionality. tDOM should be one of the fastest ways to manipulate
XML with a scripting language and uses very little memory.

%package devel
Summary: Development files for compiling against tdom
Requires:       %{name} = %{version}-%{release} expat-devel
%description devel
Development header files for compiling against tdom.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}-src
%oreon_prep
%build

%configure --enable-threads --with-expat=yes
%make_build
%install
%make_install
mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.so %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version}/*.a %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/%{name}%{version} %{buildroot}%{tcl_sitearch}
sed -i -e 's/file join $dir libtdom/file join $dir .. .. libtdom/' %{buildroot}%{tcl_sitearch}/%{name}%{version}/pkgIndex.tcl
sed -i -e "s#%{_libdir}/%{name}%{version}#%{_libdir}#" %{buildroot}%{_libdir}/tdomConfig.sh
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tdom-devel -f %{oreon_filedir}/tdom-devel.list

%changelog

%autochangelog
