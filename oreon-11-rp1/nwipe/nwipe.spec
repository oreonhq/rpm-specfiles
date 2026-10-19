%global source0_hash 0e38474495cc6c86043a1de0460cf0dc009ad68e079ee23d71569e80e55cd2e6
Name:           nwipe
Version:        0.42
Release:        1%{?dist}
Summary:        Securely erase disks using a variety of recognized methods
%global         gituser         martijnvanbrummelen
%global         gitname         nwipe
%global         commit          316b7073089fc705dda8d8b0d6bcc948818deacb
%global         gitdate         20250910
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
License:        GPL-2.0-only
URL:            https://github.com/martijnvanbrummelen/nwipe
VCS:            git:https://github.com/martijnvanbrummelen/nwipe
Source0:        https://github.com/%{gituser}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       /usr/bin/readlink
Requires:       /usr/sbin/dmidecode
Requires:       hdparm
Requires:       /usr/sbin/modprobe
Requires:       /usr/sbin/smartctl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libconfig-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  parted-devel
# /oreon:deps
%description
The nwipe is a command that will securely erase disks using a variety of 
recognized methods. It is a fork of the dwipe command used by Darik's 
Boot and Nuke (dban). Nwipe was created out of need to run the DBAN dwipe
command outside of DBAN. This allows it to use any host distribution which
gives better hardware support. It is essentially the same as dwipe, with 
a few changes:
- pthreads is used instead of fork
- The parted library is used to detect drives
- The code is designed to be compiled with gcc
- Increased number of wipe methods
- Smartmontools is used to provide USB serial #
- DmiDecode is used to provide host info to nwipes log 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#autosetup -n %%{gitname}-%%{commit} -p 1
%autosetup -n %{gitname}-%{version} -p 1

%build

export CFLAGS="%{optflags} -std=c99"
autoreconf -vif
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
