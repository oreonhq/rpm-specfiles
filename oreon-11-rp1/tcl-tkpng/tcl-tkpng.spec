%global source0_hash 92f361d4f43c3a0638f85f87af6cef30c63a1896fa59a9220bcfab4852ab10fb

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tkpng

Name:		tcl-%{realname}
Version:	0.9
Release:	36%{?dist}
Summary:	Tcl/Tk support for PNG
License:	TCL
URL:		http://www.muonics.com/FreeStuff/TkPNG/
Source0:	http://downloads.sourceforge.net/tkpng/%{realname}%{version}.tgz
Patch0:		tcl-tkpng-configure-c99.patch
Provides:	%{realname} = %{version}-%{release}
Provides:	tk-%{realname} = %{version}-%{release}
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	tcl-devel, tk-devel, zlib-devel
Requires:	tcl(abi) = 8.6

%description
TkPNG is an open source package that adds PNG photo image support to Tcl/Tk. 
Although other extensions such as Img also add support for PNG images, this 
package was designed to be lightweight, not depending on libpng nor 
implementing other image formats, and suitable for inclusion in the Tk core. 
Tk does not currently have native support for any image formats that allow 
for alpha (partial-transparency) channels, although it does have support for 
alpha blending internally.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}%{version}

%build
%if 0%{?__isa_bits} == 64
%configure --enable-64bit
%else
%configure
%endif

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{realname}%{version} %{buildroot}%{tcl_sitearch}/%{realname}%{version}

%files
%license license.terms
%doc README ChangeLog
%{tcl_sitearch}/%{realname}%{version}/

%changelog
%autochangelog
