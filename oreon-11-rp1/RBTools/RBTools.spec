%global source0_hash 648233b115cb9f29c2db7d530d9a303f8edbd0345ba0471b1e3272e00bfe5f5e
Name:           RBTools
Version:        6.0
Release:        1%{?dist}
Summary:        Tools for use with ReviewBoard
License:        MIT
URL:            https://www.reviewboard.org/downloads/rbtools/
Source0:        https://github.com/reviewboard/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Patch:          build_release.patch
Patch:          RBTools-5.0-Use-stdlib-importlib-resources.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 74
Requires:       python3-RBTools = %{version}-%{release}
# /oreon:deps
%description
RBTools provides client tools for interacting with a ReviewBoard
code-review server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rbtools-release-%{version}
%oreon_prep
%build

%pyproject_wheel
%check

rm -rf rbtools/clients/tests/test_svn.py \
  rbtools/clients/tests/test_scanning.py \
  rbtools/commands/tests/test_alias.py
%global test_keywords not GitPerforceClientTests and not GitSubversionClientTests
%global test_keywords %{test_keywords} and not test_with_encoding
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
export HGDEMANDIMPORT=disable
%pytest -k '%{test_keywords}'
%install
%pyproject_install
install -D -pv -m 0755 rbtools/commands/conf/completions/bash \
    %{buildroot}%{bash_completions_dir}/rbt
install -D -pv -m 0755 rbtools/commands/conf/completions/zsh \
    %{buildroot}%{zsh_completions_dir}/_rbt
%oreon_autofiles main

%files

%changelog

%autochangelog
