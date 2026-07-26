%global source0_hash 5cac11c125b5cb72c2c95d63a5ea3ea8eb063885a8a14aa00d9ee040060ce932

%bcond check 0

Name: pew
Version: 1.2.0
Release: 30%{?dist}
Summary: Tool to manage multiple virtualenvs written in pure Python

License: MIT
URL: https://github.com/berdario/pew
Source0: https://github.com/berdario/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: README.md

# This patch removes Python version management on Fedora.
#
# NOTE: This removes the pythonz-bd dependency which is not available in Fedora
# anymore.
# Furthermore, there is strong support upstream to either remove Pew's
# Python version management or replace it with pyenv:
# https://github.com/berdario/pew/issues/195.
Patch0: 0001-Remove-Python-version-management-on-Fedora.patch

# Backport PR #214:
# Support Python 3.8, 3.9 and 3.10, drop EOL Python versions (2.7, 3.4, 3.5),
# use GitHub Actions for CI
# https://github.com/berdario/pew/pull/214
#
# NOTE: This enables Pew to be used on recent Fedora versions.
Patch1: 0002-Remove-remaining-references-to-Python-2.6-3.2-and-3..patch
Patch2: 0003-Add-support-for-Python-3.8-and-3.9.patch
Patch3: 0004-Unify-Pipfile-and-requirements.txt-with-dependencies.patch
Patch4: 0005-Replace-Travis-CI-and-AppVeyor-with-GitHub-Actions.patch
Patch5: 0006-Drop-support-for-Python-2-Python-3.4-and-3.5.patch
Patch6: 0007-Replace-PyPy-with-PyPy-3.patch
Patch7: 0008-Remove-test-for-testing-virtualenv-relocatable.patch
Patch8: 0009-Replace-obsolete-pytest.yield_fixture-with-pytest.fi.patch
Patch9: 0010-Explicilty-import-distutils.sysconfig-subpackage-in-.patch
Patch10: 0011-Replace-easy_install-with-setuptools-in-test_lssitep.patch
Patch11: 0012-Rewrite-test_restore-to-delete-setuptools-to-break-t.patch
Patch12: 0013-Register-pytest.marker.shell-custom-marker.patch
Patch13: 0014-Temporarily-disable-test_create_in_symlink-test-in-t.patch
Patch14: 0015-Add-support-for-Python-3.10.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(virtualenv) >= 1.11
BuildRequires: python3dist(virtualenv-clone) >= 0.2.5

%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pip)
%endif

%{?python_provide:%python_provide python3-%{name}}

%description
Python Env Wrapper is a set of commands to manage multiple virtual
environments. Pew can create, delete and copy your environments, using a
single command to switch to them wherever you are, while keeping them in a
single (configurable) location.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}-%{version}

# Rename the Fedora-specific README.md to avoid conflict with the upstream
# README.md.
# NOTE: The source file should stay named README.md so that Pagure renders it
# when one visits https://src.fedoraproject.org/rpms/pew.
cp -v %{SOURCE1} README.Fedora.md

# This script for shell completion can't be used for Fedora package
rm -rf %{name}/shell_config/complete_deploy

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pew

# Manually install shell completions scripts for Bash/Fish/Zsh.
install -m 0644 -p -D %{name}/shell_config/complete.bash %{buildroot}/%{bash_completions_dir}/pew
install -m 0644 -p -D %{name}/shell_config/complete.fish %{buildroot}/%{fish_completions_dir}/pew.fish
install -m 0644 -p -D %{name}/shell_config/complete.zsh %{buildroot}/%{zsh_completions_dir}/_pew

%check
%if %{with check}
# Temporarily disable tests failing with Python 3.12.
# For more details, see: https://github.com/pew-org/pew/issues/233.
k="not test_restore and not test_lssitepackages and not test_new_env_activated"
PATH=%{buildroot}%{_bindir}:$PATH \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
%{pytest} "${k:+-k $k}" -v tests
%endif

%files -f %{pyproject_files}
%doc README.md README.Fedora.md
%{_bindir}/pew
%{bash_completions_dir}/pew
%{fish_completions_dir}/pew.fish
%{zsh_completions_dir}/_pew

%changelog
%autochangelog
