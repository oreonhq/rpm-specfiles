%global source0_hash 1918df902c221e2862b8576ea6e95adb4d2b621f849281862327806f970eca96
%global oname targetcli-fb
Name:           targetcli
License:        Apache-2.0
Summary:        An administration shell for storage targets
Version:        3.0.2
Release:        1%{?dist}
URL:            https://github.com/open-iscsi/%{oname}
Source0:        https://github.com/open-iscsi/targetcli-fb/archive/refs/tags/v3.0.2.tar.gz#/targetcli-fb-3.0.2.tar.gz
BuildArch:      noarch
Requires:       target-restore
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-targetcli = %{version}-%{release}
# /oreon:deps
%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{oname}-%{version}

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli*.8 %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_unitdir}/
install -m 644 systemd/* %{buildroot}%{_unitdir}/
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.1-5
- Prepare for Oreon 11 (RP1)
