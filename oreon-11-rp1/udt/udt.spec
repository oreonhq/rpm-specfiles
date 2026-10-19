%global source0_hash aa25b6d7cbac474ca05b7c7b36f59e9a3cd5c61faed8bf1b7174ac118c3de1db
Name:		udt
Version:	4.11
Release:        1%{?dist}
Summary:        UDP based Data Transfer Protocol
License:	BSD-3-Clause AND Zlib
URL:		http://udt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/udt/udt/%{version}/udt.sdk.%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%package devel
Summary:	UDP based Data Transfer Protocol - development files
Requires:	%{name} = %{version}-%{release}
%description
UDT is a reliable UDP based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

%description devel
UDT development files.

# Work around %%_builddir being defined too late (#2043864)
%global _package_note_file %{_builddir}/udt4/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n udt4

sed 's!-O3!%{optflags}!' -i src/Makefile app/Makefile
sed 's!-shared!& %{?__global_ldflags} -lpthread -Wl,-soname,libudt.so.0!' \
    -i src/Makefile
sed 's!LDFLAGS =!& %{?__global_ldflags}!' -i app/Makefile
sed 's/\r//' -i doc/doc/udtdoc.css

%build

ARCH=
%ifarch %{ix86}
ARCH=IA32
%endif
%ifarch x86_64
ARCH=AMD64
%endif
%ifarch ia64
ARCH=IA64
%endif
make arch=$ARCH
%install
mkdir -p %{buildroot}%{_libdir}
install src/libudt.so %{buildroot}%{_libdir}/libudt.so.0
ln -s libudt.so.0 %{buildroot}%{_libdir}/libudt.so
mkdir -p %{buildroot}%{_includedir}/udt
install -p -m 644 src/*.h %{buildroot}%{_includedir}/udt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n udt-devel -f %{oreon_filedir}/udt-devel.list

%changelog

%autochangelog
