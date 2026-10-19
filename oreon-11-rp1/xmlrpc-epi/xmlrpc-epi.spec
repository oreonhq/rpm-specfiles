%global source0_hash c74ef8fb680b140890138a82f37619714b67f69025a775b9ba2009d62cded0b8
Name:      xmlrpc-epi
Version:   0.54.2
Release:        1%{?dist}
Summary:        An implementation of the XML-RPC protocol in C
License:   MIT
URL:       http://xmlrpc-epi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:    0000-fix-printf-formatting-security.patch
Patch1:    0001-fix-heap-buffer-overflow-CVE-2016-6296.patch
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
An implementation of the XML-RPC protocol in C.

%package  devel
Summary:  Development files for xmlrpc-epi
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The xmlrpc-epi-devel package contains libraries and header files for
developing applications that use xmlrpc-epi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .fix-printf-formatting-security
%patch -P1 -p1 -b .fix-heap-buffer-overflow-CVE-2016-6296

%build

%configure --disable-static --includedir=%{_includedir}/xmlrpc-epi
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -r %{buildroot}%{_bindir}
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xmlrpc-epi-devel -f %{oreon_filedir}/xmlrpc-epi-devel.list

%changelog

%autochangelog
