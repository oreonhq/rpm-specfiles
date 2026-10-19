%global source0_hash 1693dd678355749c5d9e48ecdd4628dbfe71d82955afde950ee8d88b5adc01cf
%define _hardened_build 1
Summary:        Restricted shell for ssh based file services
Name: scponly
Version: 4.8
Release:        1%{?dist}
License: BSD-2-Clause
URL: http://sublimation.org/scponly/
Source0:        http://downloads.sf.net/scponly/scponly-%{version}.tgz
Patch0: scponly-install.patch
Patch1: scponly-4.8-elif-gcc44.patch
Patch2: scponly-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssh-clients
BuildRequires:  openssh-server
BuildRequires:  rsync
# /oreon:deps
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

cp -p /usr/lib/rpm/redhat/config.{guess,sub} .
%configure --enable-scp-compat --enable-winscp-compat --enable-chrooted-binary
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"
chmod 0644 scponly.c scponly.h helper.c
%install
%{__rm} -rf %{buildroot}
sed -i "s|%{_prefix}/local/|%{_prefix}/|g" scponly.8* INSTALL README
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
