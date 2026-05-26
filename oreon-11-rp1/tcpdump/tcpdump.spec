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
# oreon url source checksums begin
%global source0_sha256 40a8cefd45f0d2a06827e6658efb830d484868c449ad80f7efb33516af44f3da
%global source0_file tcpdump-4.99.6.tar.xz
%global source1_sha256 082967d6bf793499d3d655cea2149e07c0da97287f1877a6eab88d17cb703d0d
%global source1_file tcpslice-1.8.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/tcpdump-4.99.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "40a8cefd45f0d2a06827e6658efb830d484868c449ad80f7efb33516af44f3da" || { echo "oreon: Source0 SHA256 mismatch for tcpdump-4.99.6.tar.xz" >&2; exit 1; })
%(f=%{_sourcedir}/tcpslice-1.8.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "082967d6bf793499d3d655cea2149e07c0da97287f1877a6eab88d17cb703d0d" || { echo "oreon: Source1 SHA256 mismatch for tcpslice-1.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
