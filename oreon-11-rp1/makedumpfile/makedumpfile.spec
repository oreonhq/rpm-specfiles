%global source0_hash b54e88bef256c589eb4adce17bc856da898a762626fe54f76a77a7f22ad9a844

%global eppic_ver 72da440362e20291d5ecbb04b6eb7c7b492f233c
%global eppic_shortver %(c=%{eppic_ver}; echo ${c:0:7})
Name: makedumpfile
Version: 1.7.8
Summary: make a small dumpfile of kdump
Release: 2%{?dist}

License: GPL-2.0-only
URL: https://github.com/makedumpfile/makedumpfile
Source0:        https://github.com/makedumpfile/makedumpfile/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/lucchouina/eppic/archive/refs/tags/%{eppic_ver}/eppic-%{eppic_shortver}.tar.gz

Conflicts: kexec-tools < 2.0.28-5
BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: elfutils-devel
BuildRequires: glib2-devel
BuildRequires: bzip2-devel
BuildRequires: ncurses-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: lzo-devel
BuildRequires: snappy-devel
BuildRequires: libzstd-devel
BuildRequires: pkgconfig
BuildRequires: intltool
BuildRequires: gettext

%description
makedumpfile is a tool to compress and filter out unneeded data from kernel
dumps to reduce its file size. It is typically used with the kdump mechanism.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -a 0 -a 1
sed -r -i 's|/usr/sbin|%_sbindir|g' Makefile

%build
%make_build LINKTYPE=dynamic USELZO=on USESNAPPY=on USEZSTD=on
%make_build -C eppic-%{eppic_ver}/libeppic
%make_build LDFLAGS="$LDFLAGS -Ieppic-%{eppic_ver}/libeppic -Leppic-%{eppic_ver}/libeppic" eppic_makedumpfile.so

%install
%make_install
install -m 644 -D makedumpfile.conf %{buildroot}/%{_sysconfdir}/makedumpfile.conf.sample
rm %{buildroot}/%{_sbindir}/makedumpfile-R.pl

install -m 755 -D eppic_makedumpfile.so %{buildroot}/%{_libdir}/eppic_makedumpfile.so

%files
%{_sbindir}/makedumpfile
%{_mandir}/man5/makedumpfile.conf.5*
%{_mandir}/man8/makedumpfile.8*
%{_sysconfdir}/makedumpfile.conf.sample
%{_libdir}/eppic_makedumpfile.so
%{_datadir}/makedumpfile/
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.8-2
- Prepare for Oreon 11 (RP1)
