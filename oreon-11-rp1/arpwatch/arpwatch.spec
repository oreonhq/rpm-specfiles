%global source0_hash 832d20a5a508d9694a84a17e2627de3b3aa8b42b19ebdd97e264c511168f6eb4
%bcond autoreconf 1
Name:           arpwatch
Epoch:          14
Version:        3.9
Release:        1%{?dist}
Summary:        Network monitoring tools for tracking IP addresses on a network
License:        BSD-3-Clause
SourceLicense:  %{shrink:
                %{license} AND
                BSD-4.3RENO AND
                FSFUL AND
                GPL-3.0-or-later AND
                X11
                }
URL:            https://ee.lbl.gov/
Requires:       /usr/sbin/sendmail
Requires:       python3
%if %{with autoreconf}
%endif
%{?sysuser_requires_compat}
Source0:        https://ee.lbl.gov/downloads/arpwatch/arpwatch-%{version}.tar.gz
Source1:        oui.csv
Source2:        arpwatch.service
Source3:        arpwatch.sysconfig
Source4:        arp2ethers.8
Source5:        massagevendor.8
Source6:        arpwatch.sysusers
Patch:          arpwatch-3.1-man-references.patch
Patch:          arpwatch-3.2-change-user.patch
Patch:          arpwatch-3.1-arp2ethers-sort-invocation.patch
Patch:          arpwatch-3.1-arpfetch-stray-rm.patch
Patch:          arpwatch-3.9-no-usr-local-path.patch
Patch:          arpwatch-3.1-configure-no-local-pcap.patch
Patch:          arpwatch-3.1-all-zero-bogon.patch
Patch:          arpwatch-3.5-exitcode.patch
Patch:          arpwatch-3.5-devlookup.patch
Patch:          arpwatch-3.3-c99.patch
ExcludeArch:    %{ix86}
%global pkgstatedir %{_sharedstatedir}/arpwatch
# oreon:deps
BuildRequires:  /usr/sbin/sendmail
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The arpwatch package contains arpwatch and arpsnmp. Arpwatch and arpsnmp are
both network monitoring tools. Both utilities monitor Ethernet or FDDI network
traffic and build databases of Ethernet/IP address pairs, and can report
certain changes via email.

Install the arpwatch package if you need networking monitoring devices which
will automatically keep track of the IP addresses on your network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Substitute absolute paths to awk scripts in shell scripts
sed -r -i 's|(-f *)([^[:blank:]+]\.awk)|\1%{_datadir}/arpwatch/\2|' arp2ethers

# Fix default directory in man pages to match ARPDIR in build section. This was
# formerly done by arpwatch-dir-man.patch. For thoroughness, do the same
# replacement in update-ethercodes.sh.in and bihourly.sh, even though they are
# not installed.
sed -r -i 's|/usr/local/arpwatch|%{pkgstatedir}|g' *.8.in *.sh.in *.sh

# Fix Python interpreter path (but note that this script is not installed)
sed -r -i 's|/usr/local/bin/python|%{python3}|g' update-ethercodes.sh.in

# Emailed upstream requesting a separate LICENSE/COPYING file 2022-07-30.
# For now, we extract it from the main source file’s “header” comment.
awk '/^ \* / { print substr($0, 4); } /^ \*\// { exit }' arpwatch.c |
  tee LICENSE

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

# Prior to version 3.4, this was handled by the configure script. If it is not
# defined, the build fails because time.h is not included in report.c. This
# regregression was reported upstream by email to arpwatch@ee.lbl.gov on
# 2023-09-06.
export CPPFLAGS="${CPPFLAGS-} -DTIME_WITH_SYS_TIME=1"

%configure --with-sendmail=/usr/sbin/sendmail PYTHON=%{python3}

%build

%make_build ARPDIR=%{pkgstatedir}
%install
install -p -D -m 0644 %{SOURCE6} '%{buildroot}%{_sysusersdir}/arpwatch.conf'
install -d %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_datadir}/arpwatch \
    %{buildroot}%{pkgstatedir} \
    %{buildroot}%{_unitdir} \
    %{buildroot}%{_prefix}/etc/rc.d
%make_install
chmod -v 0755 %{buildroot}%{_sbindir}/arpwatch %{buildroot}%{_sbindir}/arpsnmp
install -p -t %{buildroot}%{_datadir}/arpwatch -m 0644 *.awk
install -p -t %{buildroot}%{_sbindir} arp2ethers
install -p massagevendor.py %{buildroot}%{_sbindir}/massagevendor
install -p -t %{buildroot}%{pkgstatedir} -m 0644 *.dat
touch %{buildroot}%{pkgstatedir}/arp.dat- \
    %{buildroot}%{pkgstatedir}/arp.dat.new
install -p -t %{buildroot}%{_unitdir} -m 0644 %{SOURCE2}
%{python3} massagevendor.py < %{SOURCE1} \
    > %{buildroot}%{pkgstatedir}/ethercodes.dat
touch -r %{SOURCE1} ethercodes.dat
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/arpwatch
install -p -t %{buildroot}%{_mandir}/man8 -m 0644 %{SOURCE4} %{SOURCE5}
rm -rvf %{buildroot}%{_prefix}/etc/rc.d
%oreon_autofiles main

%check

if grep -FrnI '/usr/local/arpwatch' .
then
  echo 'Missed fixing ARPDIR in at least one file' 1>&2
  exit 1
fi
if grep -ErnI --exclude=mkdep --exclude='config.*' '^[^#].*/usr/local/s?bin' .
then
  echo 'Probably missed an uncommented PATH alteration with /usr/local' 1>&2
  exit 1
fi
%post

%systemd_post arpwatch.service
%postun

%systemd_postun_with_restart arpwatch.service
%preun

%systemd_preun arpwatch.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.9-1
- Prepare for Oreon 11 (RP1)
