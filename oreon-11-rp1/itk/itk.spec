%global source0_hash da646199222efdc4d8c99593863c8d287442ea5a8687f95460d6e9e72431c9c7

%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           itk
Version:        4.1.0
Release:        13%{?dist}
Summary:        Object oriented extensions to Tk

License:        TCL
URL:            http://incrtcl.sourceforge.net/itcl/
Source0:        https://downloads.sourceforge.net/incrtcl/%{name}%{version}.tar.gz
Patch0:         itk-libdir.patch
Patch1:         itk-soname.patch
Patch2:         itcl4.0.0-linuxloading.patch
Patch4:         itk-tolowercase.patch

Requires:       tcl(abi) = 8.6 itcl tk
BuildRequires:  gcc
BuildRequires:  tk-devel itcl-devel
BuildRequires: make

%description
[incr Tk] is Tk extension that provides object-oriented features that are
missing from the Tk extension to Tcl.  The OO features provided by itk are
useful for building megawidgets.

%package devel
Summary:  Development headers and libraries for linking against itk
Requires:       %{name} = %{version}-%{release}
%description devel
Development headers and libraries for linking against itk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{version}
%patch -P0 -p1 -b .libdir
%patch -P1 -p1 -b .soname
%patch -P2 -p1 -b .linuxloading
%patch -P4 -p1 -b .tolowercase

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/*.so
%dir %{tcl_sitearch}/itk%{version}
%{tcl_sitearch}/%{name}%{version}/*.tcl
%{tcl_sitearch}/%{name}%{version}/*.itk
%{tcl_sitearch}/%{name}%{version}/tclIndex
%{_mandir}/mann/*.gz
%license license.terms

%files devel
%{_includedir}/*.h
# What happened to itk's stub library and itkConfig.sh?

%changelog
%autochangelog
