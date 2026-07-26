%global source0_hash 243ea1b0962b0b6b1e717ac0e69dac9636e61ec65b37260c317b2360c6e30ca7

%global srcname ansible-pylibssh
%global _summary Python bindings specific to Ansible use case for libssh

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        %{_summary}

License:        LGPL-2.1-or-later
URL:            https://github.com/ansible/pylibssh
Source0:        %{pypi_source}
# Downstream patch to disable coverage tests
Patch0:         python-ansible-pylibssh-nocov.patch
# Force build inplace so that debuginfo can be generated
Patch1:         python-ansible-pylibssh-debug.patch

BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  /usr/bin/ssh
BuildRequires:  /usr/bin/ssh-keygen
# Use package instead of /usr/sbin/sshd to deal with sbin merge
BuildRequires:  openssh-server

%global _description %{expand:
Python bindings to client functionality of libssh specific to Ansible use
case.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{_summary}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -e just-pytest

%build
export PYTHONPATH=bin
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*pylibssh*'

%check
# Fails - need to disable cython coverage
%tox
# -- -- --deselect tests/unit/scp_test.py::test_get --deselect tests/unit/scp_test.py::test_put

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst README.rst

%changelog
%autochangelog
