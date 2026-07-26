%global source0_hash 2d3c0ce868085894c45c7436206cb3a1e376d6058a92daa3f7123afd4eda9732

# Tests are disabled by default. 😞
# Enable if https://bugzilla.redhat.com/show_bug.cgi?id=1949502 /
# https://github.com/bitprophet/pytest-relaxed/issues/12 is resolved:
%bcond_with     tests

%global         srcname     fabric

Name:           python-%{srcname}
Version:        3.2.2
Release:        %autorelease
Summary:        High level SSH command execution

License:        BSD-3-Clause
URL:            https://github.com/fabric/fabric
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Needed here since invoke's vendored decorator is not used.
# See RHBZ 2156956.
Requires:       python3dist(decorator)

%if %{with tests}
# Extra pytest (a superset of extra testing)
BuildRequires:  python3dist(pytest)
# Missing from setup.py (only in requirements-dev.txt), but still needed for
# testing:
BuildRequires:  python3dist(pytest-relaxed)
%endif

BuildRequires:  help2man

%global _description %{expand:
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Allow a slightly older invoke version.
sed -i 's/invoke>=2.0/invoke>=1.7/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/fab

%changelog
%autochangelog
