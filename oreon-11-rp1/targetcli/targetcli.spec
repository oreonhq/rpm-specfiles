%global source0_hash 711735915516975af34564b905bdf4a89be6344428932db724d78e8ff35f2c2e

%global oname targetcli-fb

Name:           targetcli
License:        Apache-2.0
Summary:        An administration shell for storage targets
Version:        3.0.1
Release:        5%{?dist}
URL:            https://github.com/open-iscsi/%{oname}
Source:        https://github.com/open-iscsi/targetcli-fb/archive/v3.0.1/targetcli-fb-3.0.1.tar.gz
# Proposed upstream
## From: https://github.com/open-iscsi/targetcli-fb/pull/176
BuildArch:      noarch
BuildRequires:  python3-devel, systemd-rpm-macros
Requires:       target-restore


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{oname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'targetcli*'
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli*.8 %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_unitdir}/
install -m 644 systemd/* %{buildroot}%{_unitdir}/

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%license COPYING
%{_bindir}/targetcli
%{_bindir}/targetclid
%{_mandir}/man8/targetcli*.8*
%{_unitdir}/*
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.1-5
- Prepare for Oreon 11 (RP1)
