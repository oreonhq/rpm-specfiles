%global source0_hash 0550c21f0a120302190a1a332530921de2b27208e24e28a953fbd890567dc294
%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh || echo 0)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}
Name:           itcl
Version:        4.3.2
Release:        1%{?dist}
Summary:        Object oriented extensions to Tcl and Tk
License:        TCL
URL:            http://incrtcl.sourceforge.net/itcl/
Source0:        https://downloads.sourceforge.net/incrtcl/itcl%{version}.tar.gz
Patch1:         itcl-libdir.patch
Patch2:         itcl-soname.patch
Requires:       tcl(abi) = %{tcl_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
# /oreon:deps
%description
[incr Tcl] is Tcl extension that provides object-oriented features that are
missing from the Tcl language.

%package devel
Summary:  Development headers and libraries for linking against itcl
Requires:       %{name} = %{version}-%{release}
%description devel
Development headers and libraries for linking against itcl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{version}
%patch -P1 -p0 -b .libdir
%patch -P2 -p0 -b .soname

%build

%configure
%make_build
%install
%make_install
chmod +x '%{buildroot}%{tcl_sitearch}/%{name}%{version}/'*.so
sed -i -e "s#%{_libdir}/%{name}%{version}#%{tcl_sitearch}/%{name}%{version}#" \
        '%{buildroot}%{_libdir}/itclConfig.sh'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n itcl-devel -f %{oreon_filedir}/itcl-devel.list

%changelog

%autochangelog
