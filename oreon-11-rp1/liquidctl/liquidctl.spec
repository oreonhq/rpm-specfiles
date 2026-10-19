%global source0_hash b631a9f9c17980304c482ba72599b4089cc168d8c2edfdf65b0daa85cc614f8f
Name: liquidctl
%global pypi_name %{name}
Summary:        Tool for controlling liquid coolers, case fans and RGB LED strips
License: GPL-3.0-or-later
Version: 1.16.0
Release:        1%{?dist}
URL: https://github.com/jonasmalacofilho/liquidctl
Source0:        https://files.pythonhosted.org/packages/source/l/liquidctl/liquidctl-%{version}.tar.gz
BuildArch: noarch
ExcludeArch: s390 s390x
Requires: python3-%{name} = %{version}-%{release}
Suggests: %{name}-udev = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-liquidctl = %{version}-%{release}
# /oreon:deps
%description
liquidctl is a tool for controlling various settings of PC internals, such as:
- liquid cooler pump speed
- case fan speed
- RGB LED strip colors

For a full list of supported devices, visit:
https://github.com/liquidctl/liquidctl#supported-devices

%package -n python3-%{name}
Summary: Module for controlling liquid coolers, case fans and RGB LED devices
%description -n python3-%{name}
A python module providing classes for communicating with various cooling devices
and RGB LED solutions.

For a full list of supported devices, visit:
https://github.com/liquidctl/liquidctl#supported-devices

%package udev
Summary: Unprivileged device access rules for %{name}
Requires: %{name} = %{version}-%{release}
%description udev
This package contains udev rules which allow %{name} to access relevant devices
when ran by an unprivileged user.

%package doc
Summary: Documentation for %{name}
%description doc
This package contains documentation for %{name}, including
device-specific guides and developer docs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export DIST_NAME=$(source /etc/os-release && echo "${NAME} ${VERSION_ID}")
export DIST_PACKAGE="%{name}-%{version}-%{release}.%{_build_arch}"
%pyproject_wheel
%install
%pyproject_install
install -Dp -m 644 \
	liquidctl.8 \
	%{buildroot}%{_mandir}/man8/%{name}.8
install -Dp -m 644 \
	extra/completions/liquidctl.bash \
	%{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp -m 644 \
	extra/linux/71-%{name}.rules \
	%{buildroot}%{_udevrulesdir}/71-%{name}.rules
install -Dp -m 644 -t %{buildroot}%{_pkgdocdir} \
	CHANGELOG.md README.md
cp -a docs/ %{buildroot}%{_pkgdocdir}/
%oreon_autofiles main usr/lib/python3*/site-packages/liquidctl* usr/lib64/python3*/site-packages/liquidctl* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

mkdir ./test-run-dir
XDG_RUNTIME_DIR=$(pwd)/test-run-dir pytest-3
%files
%files -n python3-liquidctl -f %{oreon_filedir}/python3-liquidctl.list
%files -n liquidctl-udev -f %{oreon_filedir}/liquidctl-udev.list
%files -n liquidctl-doc -f %{oreon_filedir}/liquidctl-doc.list

%changelog

%autochangelog
