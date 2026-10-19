%global source0_hash 38f406bf21acc67e45f414b7980463b2e6e6270ba3616ffd41995d997078cbe6
%bcond xdist %[%{defined fedora} && %{undefined bootstrap}]
Name:           python-psutil
Version:        7.2.2
Release:        1%{?dist}
Summary:        A process and system utilities module for Python
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source0:        https://github.com/giampaolo/psutil/archive/refs/tags/release-7.2.2.tar.gz#/psutil-7.2.2.tar.gz
%if %{with xdist}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 43
Requires:       python3-psutil = %{version}-%{release}
# /oreon:deps
%description
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.

%package -n python%{python3_pkgversion}-psutil
Summary:        A process and system utilities module for Python
Obsoletes:      python%{python3_pkgversion}-psutil-tests < 7.0.0-10
%description -n python%{python3_pkgversion}-psutil
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python 3, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n psutil-release-%{version}

# Remove shebangs
find psutil -name \*.py | while read file; do
  sed -i.orig -e '1{/^#!/d}' $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

# When running tests on Zuul CI, "/" is not mounted, hence the test fail
# We want to run it on other build systems, hence the explicit skip for
# the particular buildhost
%if "%{_buildhost}" == "zuulci-mockbuild.redhat.com"
 sed -i "s/test_disk_partitions/notest_disk_partitions/" tests/test_system.py
%endif

%build

%pyproject_wheel
make build
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/psutil* usr/lib64/python3*/site-packages/psutil* usr/bin/*
%if ! 0%{?flatpak}
%check

k="${k-}${k+ and }not (TestProcessAgainstStatus and test_cpu_affinity and not eligible_cpus)"
k="${k-}${k+ and }not (TestSystemVirtualMemory and test_used)"
k="${k-}${k+ and }not (test_process_all and test_all)"
k="${k-}${k+ and }not (test_system and test_cpu_freq)"
k="${k-}${k+ and }not TestSystemCPUCountCores"
k="${k-}${k+ and }not TestSystemCPUStats"
k="${k-}${k+ and }not TestSystemNetIfAddrs"
k="${k-}${k+ and }not test_against_nproc"
k="${k-}${k+ and }not test_against_sysdev_cpu_"
k="${k-}${k+ and }not test_disk_partitions_mocked"
k="${k-}${k+ and }not test_emulate_use_cpuinfo"
k="${k-}${k+ and }not test_emulate_use_second_file"
k="${k-}${k+ and }not test_exe_mocked"
k="${k-}${k+ and }not test_debug"
k="${k-}${k+ and }not (test_system and test_sensors_temperatures and not fahreneit)"
%ifarch aarch64 ppc64le riscv64
k="${k-}${k+ and }not test_emulate_multi_cpu"
%endif
k="${k-}${k+ and }not emulate_energy_full_0"
k="${k-}${k+ and }not emulate_energy_full_not_avail"
k="${k-}${k+ and }not emulate_no_power"
k="${k-}${k+ and }not emulate_power_undetermined"
GITHUB_ACTIONS=1 %{pytest} -v %{?with_xdist:-n auto} "${k:+-k $k}" --pyargs tests \
  --deselect tests/test_system.py::TestDiskAPIs::test_disk_partitions \
  --deselect tests/test_system.py::TestMiscAPIs::test_heap_info \
  --ignore tests/test_memleaks.py \
  ;
%endif
%files
%files -n python3-psutil -f %{oreon_filedir}/python3-psutil.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.2.2-1
- Prepare for Oreon 11 (RP1)
