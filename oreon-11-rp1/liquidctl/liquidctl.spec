%global source0_hash b631a9f9c17980304c482ba72599b4089cc168d8c2edfdf65b0daa85cc614f8f

Name: liquidctl
%global pypi_name %{name}

Summary: Tool for controlling liquid coolers, case fans and RGB LED strips
License: GPL-3.0-or-later

Version: 1.16.0
Release: 1%{?dist}

URL: https://github.com/jonasmalacofilho/liquidctl
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros

# i2c-tools are unavailable on s390{,x}
ExcludeArch: s390 s390x

# Require the python libs in the main package
Requires: python3-%{name} = %{version}-%{release}
# Suggest installing the -udev subpackage
Suggests: %{name}-udev = %{version}-%{release}

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

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
export DIST_NAME=$(source /etc/os-release && echo "${NAME} ${VERSION_ID}")
export DIST_PACKAGE="%{name}-%{version}-%{release}.%{_build_arch}"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

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

%check
mkdir ./test-run-dir
XDG_RUNTIME_DIR=$(pwd)/test-run-dir pytest-3

%files
%doc %{_pkgdocdir}/*.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.*
%{_datadir}/bash-completion/completions/%{name}

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE.txt

%files udev
%{_udevrulesdir}/71-%{name}.rules

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/docs

%changelog
%autochangelog
