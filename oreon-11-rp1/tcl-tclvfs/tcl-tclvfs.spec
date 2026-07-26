%global source0_hash f25e55294109eb750b1f1d810a0016f0cb07f23e5e1ad513501e4b3b5bb4f489

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tclvfs
%global checkin 166cafa5ca

Name:		tcl-%{realname}
Version:	1.5.0
Release:	2%{?dist}
Epoch:		1
Summary:	Tcl extension for Virtual Filesystem support
License:	MIT
URL:		https://core.tcl-lang.org/tclvfs
Source0:	https://core.tcl-lang.org/tclvfs/tarball/%{checkin}/tclvfs-%{checkin}.tar.gz
Provides:	tcl-vfs = %{version}-%{release}
Provides:	%{realname} = %{version}-%{release}
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:	tcl-devel >= 9.0, tk-devel
Requires:	tcl(abi) = 9.0, tcl-trf

%description
The TclVfs project aims to provide an extension to the Tcl language which
allows Virtual Filesystems to be built using Tcl scripts only. It is also a
repository of such Tcl-implemented filesystems (metakit, zip, tar, http,
webdav, namespace, url)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-%{checkin}
# %%patch -P0 -p1 -b .tcl86
# %%patch -P1 -p1 -b .configure-c99

%build
%configure
sed -i 's|/generic:|\$(srcdir)/generic:|g' Makefile
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/vfs1.5.0 %{buildroot}%{tcl_sitearch}/vfs1.5.0
chmod +x %{buildroot}%{tcl_sitearch}/vfs1.5.0/template/fishvfs.tcl

%files
%doc Readme.txt DESCRIPTION.txt ChangeLog
%license license.terms
%{tcl_sitearch}/vfs1.5.0/
%{_mandir}/mann/vfs*

%changelog
%autochangelog
