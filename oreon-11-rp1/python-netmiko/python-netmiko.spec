%global source0_hash dbdfc20b6caaf8e5d7a570bb1b42a26b9a6f8d8234e91f5c65f4dbfe0c0e4f50

%global srcname netmiko
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-%{srcname}
Version:        4.5.0
Release:        6%{?dist}
Summary:        %{sum}

# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
# See prep section below on textfsm
Requires:       python3-textfsm >= 1.1.3
BuildRequires:  python3-textfsm
%if 0%{?rhel}
BuildRequires:  python3-importlib-resources
%endif
# TODO(dtantsur): one of the optional modules requires pysnmp, but it's not
# usable in Python 3.12. Add it when a version that does not require asyncore
# is uploaded.

%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

# FIXME: build the documentation, when upstream starts shipping its sources:
# https://github.com/ktbyers/netmiko/issues/507

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# NOTE(dtantsur): ntc-templates is not packaged, we're using python3-textfsm
# instead. Fixes https://bugzilla.redhat.com/show_bug.cgi?id=1927400.
sed -i '/^ntc-templates/d' pyproject.toml
# FIXME(dtantsur): auto-generating this dependency does not work. No idea why.
sed -i '/^textfsm/d' pyproject.toml
# NOTE(dtantsur): 1.17.0rc1 is not packaged yet but the required Python 3.13
# fix is already in Fedora.
sed -i '/^cffi/s/1.17.0rc1/1.16.0/' pyproject.toml
# Years after Python 2 removal, Fedora still considers just "python" ambiguous.
# Let's assume they shouldn't be invoked directly, only via generated scripts.
sed -si '/^#!\/usr\/bin\/env python/d' netmiko/cli_tools/netmiko_*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files netmiko

%check
# FIXME: run unit tests, when/if upstream creates them:
# https://github.com/ktbyers/netmiko/issues/509
%pyproject_check_import -e '*.snmp_autodetect'

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/netmiko-bulk-encrypt
%{_bindir}/netmiko-cfg
%{_bindir}/netmiko-encrypt
%{_bindir}/netmiko-grep
%{_bindir}/netmiko-show
%license LICENSE
%doc README.md

%changelog
%autochangelog
