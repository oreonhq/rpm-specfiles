%global source0_hash 75ed2ace81f0fa3e9c3fb64dab0e8857ed59247ea755f5898416feb2c66807b9

Name:           chkrootkit
Version:        0.58
Release:        3b%{?dist}
Summary:        Tool to locally check for signs of a rootkit
License:        BSD-2-Clause AND GPL-2.0-or-later
URL:            http://www.chkrootkit.org
Source0:        ftp://ftp.chkrootkit.org/pub/seg/pac/chkrootkit-%{version}b.tar.gz
Source2:        chkrootkit.png
Source3:        chkrootkit.desktop
Source4:        chkrootkit.console
Source5:        chkrootkit.pam
Source6:        README.false_positives
Patch1:         chkrootkit-0.44-getCMD.patch
Patch2:         chkrootkit-0.44-inetd.patch
Patch3:         chkrootkit-0.47-chklastlog.patch
Patch4:         chkrootkit-0.49-chkproc-psver.patch
Patch5:         chkrootkit-0.49-CVE-2014-0476.patch
Patch6:         chkrootkit-0.53-netstat-l2cap.patch
# Fix a build failure caused by a signal handler function having the
# wrong signature
# Mailed to upstream authors jessen and nelsonmurilo 2025-01-17
Patch7:         chkrootkit-0.57-sighandler-type.patch

BuildRequires:  desktop-file-utils perl-interpreter
BuildRequires:  glibc-static gcc
BuildRequires: make

Requires:       usermode
Requires:	net-tools

%description
chkrootkit is a tool to locally check for signs of a rootkit.
It contains:

 * chkrootkit: shell script that checks system binaries for
   rootkit modification.
 * ifpromisc: checks if the network interface is in promiscuous mode.
 * chklastlog: checks for lastlog deletions.
 * chkwtmp: checks for wtmp deletions.
 * chkproc: checks for signs of LKM trojans.
 * chkdirs: checks for signs of LKM trojans.
 * strings: quick and dirty strings replacement.
 * chkutmp: checks for utmp deletions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}b
%patch -P 1 -p1 -b .getCMD
%patch -P 2 -p1 -b .inetd
%patch -P 3 -p1 -b .chklastlog
%patch -P 4 -p0 -b .chkproc-psver
%patch -P 5 -p1
%patch -P 6 -p0
%patch -P 7 -p1
sed -i -e 's!\s\+@strip.*!!g' Makefile

%build
make sense CC="%{__cc} $RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
ln -s %{_bindir}/consolehelper ${RPM_BUILD_ROOT}%{_bindir}/chkrootkit

install -p -D -m0644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/chkrootkit.png
install -p -D -m0644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/chkrootkit
perl -pi -e 's!--PATH--!%{_libdir}/%{name}-%{version}!' ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/chkrootkit
install -p -D -m0644 %{SOURCE5} ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/chkrootkit
for f in \
    check_wtmpx  \
    chkdirs  \
    chklastlog  \
    chkproc  \
    chkrootkit  \
    chkutmp \
    chkwtmp  \
    ifpromisc  \
    strings-static \
; do
    install -p -D -m0755 $f ${RPM_BUILD_ROOT}%{_libdir}/%{name}-%{version}/${f}
done
ln -s strings-static ${RPM_BUILD_ROOT}%{_libdir}/%{name}-%{version}/strings

desktop-file-install                   \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  %{SOURCE3}

install -p -m0644 %{SOURCE6} .

%files
%license COPYRIGHT
%doc ACKNOWLEDGMENTS README README.chklastlog README.chkwtmp chkrootkit.lsm README.false_positives
%{_bindir}/chkrootkit
%config(noreplace) %{_sysconfdir}/pam.d/chkrootkit
%config(noreplace) %{_sysconfdir}/security/console.apps/chkrootkit
%{_libdir}/%{name}-%{version}
%{_datadir}/applications/chkrootkit.desktop
%{_datadir}/pixmaps/chkrootkit.png

%changelog
%autochangelog
