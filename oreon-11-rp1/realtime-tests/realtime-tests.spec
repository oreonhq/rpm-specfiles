%global source0_hash c01ce99d4b86a99ef83fb75ddc97ddd7669eb85996a2c35bc9ad9e83ecad47bc

Name: realtime-tests
Summary: Programs that test various rt-features
Version: 2.11
Release: %autorelease
License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later
URL: https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git
Source0: https://www.kernel.org/pub/linux/utils/rt-tests/rt-tests-%{version}.tar.xz

ExcludeArch: %{arm}
BuildRequires: make
BuildRequires: gcc
BuildRequires: numactl-devel
BuildRequires: python3-devel
Requires: bash
Requires: bc

#Patches

%description
realtime-tests is a set of programs that test and measure various components of
real-time kernel behavior. This package measures timer, signal, and hardware
latency. It also tests the functioning of priority-inheritance mutexes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n rt-tests-%{version}

%build
%set_build_flags
%make_build

%install
%make_install prefix=%{_prefix}

%files
%pycached %{python3_sitelib}/hwlatdetect.py
%caps(cap_sys_rawio+ep) /usr/bin/cyclictest
%{_bindir}/pi_stress
%{_bindir}/signaltest
%{_bindir}/hwlatdetect
%{_bindir}/rt-migrate-test
%{_bindir}/pip_stress
%{_bindir}/ptsematest
%{_bindir}/sigwaittest
%{_bindir}/svsematest
%{_bindir}/pmqtest
%{_bindir}/hackbench
%{_bindir}/cyclicdeadline
%{_bindir}/deadline_test
%{_bindir}/queuelat
%{_bindir}/ssdd
%{_bindir}/oslat
%{_bindir}/determine_maximum_mpps.sh
%{_bindir}/get_cyclictest_snapshot
%pycached %{python3_sitelib}/get_cyclictest_snapshot.py
%doc
%{_mandir}/man8/cyclictest.8.*
%{_mandir}/man8/hackbench.8.*
%{_mandir}/man8/hwlatdetect.8.*
%{_mandir}/man8/pi_stress.8.*
%{_mandir}/man8/pmqtest.8.*
%{_mandir}/man8/ptsematest.8.*
%{_mandir}/man8/rt-migrate-test.8.*
%{_mandir}/man8/signaltest.8.*
%{_mandir}/man8/sigwaittest.8.*
%{_mandir}/man8/svsematest.8.*
%{_mandir}/man8/pip_stress.8.*
%{_mandir}/man8/queuelat.8.*
%{_mandir}/man8/deadline_test.8.*
%{_mandir}/man8/cyclicdeadline.8.*
%{_mandir}/man8/ssdd.8.*
%{_mandir}/man8/oslat.8.*
%{_mandir}/man8/get_cyclictest_snapshot.8.*
%{_mandir}/man8/determine_maximum_mpps.8.*

%changelog
%autochangelog
