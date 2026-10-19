%global source0_hash ad756d2efd6ac85f464e2d071a0f0e9a213972f6a0a247b9bf44b064b39f67f5
Name: modulemd-tools
Version: 0.16
Release:        1%{?dist}
Summary:        Collection of tools for modular (in terms of Fedora Modularity origin) content creators
License: MIT
BuildArch: noarch
URL: https://github.com/rpm-software-management/modulemd-tools
Source0:        https://github.com/rpm-software-management/modulemd-tools/archive/refs/tags/modulemd-tools-%{version}-1.tar.gz#/modulemd-tools-%{version}.tar.gz
Patch0: 0001-createrepo_mod-fix-failing-tests-on-F39-because-of-n.patch
Requires: createrepo_c
Requires: python3-dnf
Requires: python3-hawkey
Requires: python3-createrepo_c
Requires: python3-pyyaml
Requires: python3-libmodulemd >= 2.9.3
Requires: python3-koji
# oreon:deps
BuildRequires:  argparse-manpage
BuildRequires:  createrepo_c
BuildRequires:  python3-createrepo_c
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
BuildRequires:  python3-hawkey
BuildRequires:  python3-koji
BuildRequires:  python3-libmodulemd
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
# /oreon:deps
%description
Tools provided by this package:

repo2module - Takes a YUM repository on its input and creates modules.yaml
    containing YAML module definitions generated for each package.

dir2module - Generates a module YAML definition based on essential module
    information provided via command-line parameters. The packages provided by
    the module are found in a specified directory or a text file containing
    their list.

createrepo_mod - A small wrapper around createrepo_c and modifyrepo_c to provide
    an easy tool for generating module repositories.

modulemd-add-platform - Add a new context configuration for a new platform
    into a modulemd-packager file.

modulemd-merge - Merge several modules.yaml files into one. This is useful for
    example if you have several yum repositories and want to merge them into one.

modulemd-generate-macros - Generate module-build-macros SRPM package, which is
    a central piece for building modules. It should be present in the buildroot
    before any other module packages are submitted to be built.

bld2repo - Simple tool for dowloading build required RPMs of a modular build from koji.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -n modulemd-tools-modulemd-tools-%{version}-1 -q
%patch 0 -p1

%build

%py3_build
PYTHONPATH=: ./man/generate-manpages.sh
%install
%py3_install
install -d %{buildroot}%{_mandir}/man1
cp man/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%{python3} -m pytest -vv
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
