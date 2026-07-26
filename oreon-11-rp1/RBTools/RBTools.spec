%global source0_hash 7efd4efa3966830532b71f8408ff2ed0d11c7aff9fdf6021f261b9380cfcd37a

Name:           RBTools
Version:        5.0
Release:        8%{?dist}
Summary:        Tools for use with ReviewBoard

License:        MIT
URL:            https://www.reviewboard.org/downloads/rbtools/
Source:         https://github.com/reviewboard/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz

Patch:          build_release.patch
# Use stdlib importlib.resources on Python >= 3.12
# https://reviews.reviewboard.org/r/13997/
Patch:          RBTools-5.0-Use-stdlib-importlib-resources.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  cvs
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  subversion

BuildRequires:  python3-pytest-env
BuildRequires:  python3-kgb >= 7.1.1
BuildRequires:  pytest
BuildRequires:  python3-pytest-env

%description
RBTools provides client tools for interacting with a ReviewBoard
code-review server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rbtools-release-%{version}

%generate_buildrequires
%pyproject_buildrequires

rm -Rf %{name}*.egg-info

%build
%pyproject_wheel

%check
# skip svn tests
rm -rf rbtools/clients/tests/test_svn.py \
  rbtools/clients/tests/test_scanning.py \
  rbtools/commands/tests/test_alias.py
%global test_keywords not GitPerforceClientTests and not GitSubversionClientTests
%if 0%{?fedora} >= 41
# `kgb` is not compatible with Python 3.13: https://github.com/beanbaginc/kgb/issues/11
%global test_keywords %{test_keywords} and not SetupRepoTest
%endif
# RunProcessTests.test_with_encoding depends on byte order.
# Exclude it always, as we cannot control or check builder arch for noarch packages.
%global test_keywords %{test_keywords} and not test_with_encoding
# we need git to function
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# Unbreak Mercurial (https://bugzilla.redhat.com/show_bug.cgi?id=2299346#c2)
export HGDEMANDIMPORT=disable
%pytest -k '%{test_keywords}'

%install
%pyproject_install
%pyproject_save_files -l rbtools

# Install bash and zsh completion scripts
install -D -pv -m 0755 rbtools/commands/conf/completions/bash \
    %{buildroot}%{bash_completions_dir}/rbt
install -D -pv -m 0755 rbtools/commands/conf/completions/zsh \
    %{buildroot}%{zsh_completions_dir}/_rbt

%files -f %{pyproject_files}
%doc AUTHORS NEWS README.md
%{_bindir}/rbt
%{bash_completions_dir}/rbt
%{zsh_completions_dir}/_rbt

%changelog
%autochangelog
