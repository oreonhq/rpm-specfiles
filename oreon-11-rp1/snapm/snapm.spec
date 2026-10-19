%global source0_hash 8ebe068a9ba716a0f3fcd23a1c232eec92a30d981959289227b41ff2d7c9f0c5
%global summary A set of tools for managing snapshots
Name:		snapm
Version:	0.7.0
Release:        1%{?dist}
Summary:        A set of tools for managing snapshots
License:	Apache-2.0
URL:		https://github.com/snapshotmanager/%{name}
Source0:        https://github.com/snapshotmanager/snapm/archive/refs/tags/v0.7.0.tar.gz#/snapm-0.7.0.tar.gz
BuildArch:	noarch
Requires: python3-snapm = %{version}-%{release}
Recommends: boom-boot
Recommends: python3-file-magic
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 53
Requires:       python3-snapm = %{version}-%{release}
# /oreon:deps
%package -n python3-snapm
Summary:        A set of tools for managing snapshots
%package -n python3-snapm-doc
Summary:        A set of tools for managing snapshots
%description
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

%description -n python3-snapm
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module.

%description -n python3-snapm-doc
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module documentation in HTML format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%{make_build} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -rf doc/html/_sources doc/_build
rm -f doc/*.rst doc/Makefile doc/conf.py
%install
%pyproject_install
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/schedule.d
%{__install} -p -m 644 etc/%{name}/snapm.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}
%{__install} -p -m 644 etc/%{name}/plugins.d/lvm2-cow.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
%{__install} -p -m 644 etc/%{name}/plugins.d/lvm2-thin.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
%{__install} -p -m 644 etc/%{name}/plugins.d/stratis.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man8/snapm.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
%{__install} -p -m 644 man/man5/snapm.conf.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man5/snapm-plugins.d.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man5/snapm-schedule.d.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-create@.service ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-create@.timer ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-gc@.service ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-gc@.timer ${RPM_BUILD_ROOT}/%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}/%{_tmpfilesdir}
%{__install} -p -m 644 systemd/tmpfiles.d/%{name}.conf ${RPM_BUILD_ROOT}/%{_tmpfilesdir}/
%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}
%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}/mounts
%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}/lock
%oreon_autofiles python3-snapm usr/lib/python3*/site-packages/snapm* usr/lib64/python3*/site-packages/snapm* usr/bin/*
%oreon_autofiles python3-snapm-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/snapm* usr/lib64/python3*/site-packages/snapm* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest --log-level=debug -v tests/
%files
%files -n python3-snapm -f %{oreon_filedir}/python3-snapm.list
%files -n python3-snapm-doc -f %{oreon_filedir}/python3-snapm-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-1
- Prepare for Oreon 11 (RP1)
