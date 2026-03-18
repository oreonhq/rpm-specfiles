%define tcpslice_dir tcpslice-1.8

Summary: A network traffic monitoring tool
Name: tcpdump
Epoch: 14
Version: 4.99.6
Release: 3%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC AND ISC AND NTP
URL: http://www.tcpdump.org
BuildRequires: make
BuildRequires: automake openssl-devel libpcap-devel git-core gcc
BuildRequires: systemd-rpm-macros

Source0: http://www.tcpdump.org/release/tcpdump-%{version}.tar.xz
Source1: http://www.tcpdump.org/release/%{tcpslice_dir}.tar.gz
Source2: http://www.tcpdump.org/release/tcpdump-%{version}.tar.xz.sig
Source3: tcpdump-sysusers.conf

Patch0002:      0002-Use-getnameinfo-instead-of-gethostbyaddr.patch
Patch0003:      0003-Drop-root-priviledges-before-opening-first-savefile-.patch
Patch0007:      0007-Introduce-nn-option.patch
Patch0009:      0009-Change-n-flag-to-nn-in-TESTonce.patch

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/tcpdump
%endif

%description
Tcpdump is a command-line tool for monitoring network traffic.
Tcpdump can capture and display the packet headers on a particular
network interface or on all interfaces.  Tcpdump can display all of
the packet headers, or just the ones that match particular criteria.

Install tcpdump if you need a program to monitor network traffic.

%prep
%autosetup -a 1 -S git

%build
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) -fno-strict-aliasing -DGUESS_TSO"

pushd %{tcpslice_dir}
# update config.{guess,sub}
automake -a -f 2> /dev/null || :
./autogen.sh
%configure
%{make_build}
popd

%configure --with-crypto --with-user=tcpdump --without-smi
%{make_build}

%check
make check

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

pushd %{tcpslice_dir}
install -m755 tcpslice ${RPM_BUILD_ROOT}%{_sbindir}
install -m644 tcpslice.1 ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpslice.8
popd

install -m755 tcpdump ${RPM_BUILD_ROOT}%{_sbindir}
install -m644 tcpdump.1 ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdump.8

install -p -D -m 0644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysusersdir}/tcpdump.conf

# fix section numbers
sed -i 's/\(\.TH[a-zA-Z ]*\)[1-9]\(.*\)/\18\2/' \
	${RPM_BUILD_ROOT}%{_mandir}/man8/*


%files
%license LICENSE
%doc README.md CHANGES CREDITS
%{_sbindir}/tcpdump
%{_sbindir}/tcpslice
%{_sysusersdir}/tcpdump.conf
%{_mandir}/man8/tcpslice.8*
%{_mandir}/man8/tcpdump.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.99.6-3
- Prepare for Oreon 11 (RP1)
