%global source0_hash 1693dd678355749c5d9e48ecdd4628dbfe71d82955afde950ee8d88b5adc01cf

%define _hardened_build 1
Summary: Restricted shell for ssh based file services
Name: scponly
Version: 4.8
Release: 39%{?dist}
License: BSD-2-Clause
URL: http://sublimation.org/scponly/
Source: http://downloads.sf.net/scponly/scponly-%{version}.tgz
Patch0: scponly-install.patch
Patch1: scponly-4.8-elif-gcc44.patch
Patch2: scponly-configure-c99.patch

# Checks only for location of binaries
BuildRequires: make
BuildRequires:  gcc
BuildRequires: openssh-clients >= 3.4
BuildRequires: openssh-server
BuildRequires: rsync

%description
scponly is an alternative 'shell' for system administrators 
who would like to provide access to remote users to both 
read and write local files without providing any remote 
execution priviledges. Functionally, it is best described 
as a wrapper to the "tried and true" ssh suite of applications. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
# config.guess in tarball lacks ppc64
cp -p /usr/lib/rpm/redhat/config.{guess,sub} .
%configure --enable-scp-compat --enable-winscp-compat --enable-chrooted-binary

%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"

# Remove executable bit so the debuginfo does not hae executable source files
chmod 0644 scponly.c scponly.h helper.c

%install
%{__rm} -rf %{buildroot}

# 
sed -i "s|%{_prefix}/local/|%{_prefix}/|g" scponly.8* INSTALL README
make install DESTDIR=%{buildroot}

%files 
%doc AUTHOR CHANGELOG CONTRIB COPYING INSTALL README TODO BUILDING-JAILS.TXT
%doc SECURITY
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/scponly.8*
%{_bindir}/scponly
%{_sbindir}/scponlyc
%dir %{_sysconfdir}/scponly/
%config(noreplace) %{_sysconfdir}/scponly/*

%changelog
%autochangelog
