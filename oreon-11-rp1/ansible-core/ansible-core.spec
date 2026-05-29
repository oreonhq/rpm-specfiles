%global source0_hash none

# SPDX-License-Identifier: MIT
# Copyright (C) Fedora Project Authors
# License Text: https://spdx.org/licenses/MIT.html

# several test dependencies are unwanted in RHEL
%bcond tests %{undefined rhel}

# controls whether to generate shell completions
# may be useful for bootstrapping purposes
%bcond argcomplete 1

# disable the python -s shbang flag as we want to be able to find non system modules
%undefine _py3_shebang_s

Name:           ansible-core
Version:        2.20.3
%global uversion %{version_no_tilde %{quote:%nil}}
Release:        1%{?dist}
Summary:        A radically simple IT automation system

# The main license is GPLv3+. Many of the files in lib/ansible/module_utils
# are BSD licensed. There are various files scattered throughout the codebase
# containing code under different licenses.
# The ssh-agent helper code is BSD-3-Clause.
License:        GPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND PSF-2.0 AND MIT AND Apache-2.0
URL:            https://ansible.com

Source0:        https://github.com/ansible/ansible/archive/v%{version_no_tilde/ansible-core-%{version_no_tilde.tar.gz
Source1:        https://github.com/ansible/ansible-documentation/archive/v%{version_no_tilde/ansible-documentation-%{version_no_tilde.tar.gz

BuildArch:      noarch

# Virtual provides for bundled libraries
# Search for `_BUNDLED_METADATA` to find them

# lib/ansible/module_utils/distro/*
# SPDX-License-Identifier: Apache-2.0
Provides:       bundled(python3dist(distro)) = 1.9.0

# lib/ansible/module_utils/six/*
# SPDX-License-Identifier: MIT
Provides:       bundled(python3dist(six)) = 1.17.0

# lib/ansible/_internal/_wrapt.py
# SPDX-License-Identifier: BSD-2-Clause
Provides:       bundled(python3dist(wrapt)) = 1.17.2

BuildRequires:  python%{python3_pkgversion}-devel
# This is only used in %%prep to relax the required setuptools version,
# which is not necessary in RHEL 10+.
# Not using it in RHEL avoids unwanted dependencies.
%if %{undefined rhel}
BuildRequires:  tomcli >= 0.3.0
%endif
# Needed to build manpages from source.
BuildRequires:  python%{python3_pkgversion}-docutils

%if %{with tests}
BuildRequires:  git-core
BuildRequires:  glibc-all-langpacks
BuildRequires:  python%{python3_pkgversion}-systemd
%endif

%if %{with argcomplete}
Requires:       python%{python3_pkgversion}-argcomplete
%endif
%if 0%{?fedora} >= 39
BuildRequires:  python3-libdnf5
Recommends:     python3-libdnf5
%endif


%global _description %{expand:
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.}

%description %_description

This is the base part of ansible (the engine).

%package doc
Summary:        Documentation for Ansible Core
Provides:       ansible-base-doc = %{version}-%{release}
Obsoletes:      ansible-base-doc < 2.10.6-1

%description doc %_description

This package installs extensive documentation for ansible-core


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n ansible-%{uversion} -a1
# Relax setuptools constraint on Fedora
# Future RHELs have new enough setuptools
%if %{undefined rhel}
tomcli-set pyproject.toml lists replace \
    'build-system.requires' 'setuptools >=.*' 'setuptools'
%endif

sed -i -s 's|/usr/bin/env python|%{python3}|' \
    bin/ansible-test \
    test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py


# TODO: Investigate why hostname is the only module that still has a shebang
# and file an upstream issue if needed.
sed -i -e '1{\@^#!.*@d}' lib/ansible/modules/hostname.py

sed '/^mock$/d' test/lib/ansible_test/_data/requirements/units.txt > _requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:_requirements.txt test/units/requirements.txt}
%if %{with argcomplete}
# Shell completions
echo 'python%{python3_pkgversion}-argcomplete'
%endif


%build
%pyproject_wheel

# Build manpages
mkdir -p docs/man/man1
%{python3} packaging/cli-doc/build.py man --output-dir docs/man/man1


%if %{with argcomplete}
# Build shell completions
(
    cd bin
    for shell in bash fish; do
        mkdir -p "../${shell}_completions"
        for bin in *; do
            if grep -q PYTHON_ARGCOMPLETE_OK "${bin}"; then
                case "${shell}" in
                    bash)
                        format="${bin}"
                        ;;
                    fish)
                        format="${bin}.${shell}"
                        ;;
                esac
                register-python-argcomplete --shell "${shell}" "${bin}" > "../${shell}_completions/${format}"
            else
                echo "Skipped generating completions for ${bin}"
            fi
        done
    done
)
%endif


%install
%pyproject_install
%pyproject_save_files ansible ansible_test

# These files are executable when they shouldn't be.
# Only the actual "binaries" in %%{_bindir} need to be executable
# and have shebangs.
while read -r file; do
    sed -i -e '1{\@^#!.*@d}' "${file}"
done < <(find \
    %{buildroot}%{python3_sitelib}/ansible/cli/*.py \
    %{buildroot}%{python3_sitelib}/ansible/cli/scripts/ansible_connection_cli_stub.py \
        -type f ! -executable)

%if %{with argcomplete}
install -Dpm 0644 bash_completions/* -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 fish_completions/* -t %{buildroot}%{fish_completions_dir}
%endif

# Create system directories that Ansible defines as default locations in
# ansible/config/base.yml
DATADIR_LOCATIONS='%{_datadir}/ansible/collections
%{_datadir}/ansible/collections/ansible_collections
%{_datadir}/ansible/plugins/doc_fragments
%{_datadir}/ansible/plugins/action
%{_datadir}/ansible/plugins/become
%{_datadir}/ansible/plugins/cache
%{_datadir}/ansible/plugins/callback
%{_datadir}/ansible/plugins/cliconf
%{_datadir}/ansible/plugins/connection
%{_datadir}/ansible/plugins/filter
%{_datadir}/ansible/plugins/httpapi
%{_datadir}/ansible/plugins/inventory
%{_datadir}/ansible/plugins/lookup
%{_datadir}/ansible/plugins/modules
%{_datadir}/ansible/plugins/module_utils
%{_datadir}/ansible/plugins/netconf
%{_datadir}/ansible/roles
%{_datadir}/ansible/plugins/strategy
%{_datadir}/ansible/plugins/terminal
%{_datadir}/ansible/plugins/test
%{_datadir}/ansible/plugins/vars'

UPSTREAM_DATADIR_LOCATIONS=$(grep -ri default lib/ansible/config/base.yml| tr ':' '\n' | grep '/usr/share/ansible')

if [ "$SYSTEM_LOCATIONS" != "$UPSTREAM_SYSTEM_LOCATIONS" ] ; then
  echo "The upstream Ansible datadir locations have changed.  Spec file needs to be updated"
  exit 1
fi

mkdir -p %{buildroot}%{_datadir}/ansible/plugins/
for location in $DATADIR_LOCATIONS ; do
    mkdir %{buildroot}"$location"
done
mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}%{_sysconfdir}/ansible/roles/

cp ansible-documentation-%{uversion}/examples/hosts %{buildroot}/etc/ansible/
cp ansible-documentation-%{uversion}/examples/ansible.cfg %{buildroot}/etc/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/

# We install licenses in this manner so we don't miss new licenses:
  # 1. Copy all files in licenses to %%{_pkglicensedir}.
  # 2. List the files explicitly in %%files.
  # 3. The build will fail with unpackaged file errors if license
  #    files aren't accounted for.
%global _pkglicensedir %{_licensedir}/ansible-core
install -Dpm 0644 licenses/* -t %{buildroot}%{_pkglicensedir}

%check
%if %{with tests}
%{python3} bin/ansible-test \
    units --local --python-interpreter %{python3} -vv
%endif


%files -f %{pyproject_files}
%license COPYING
%license %{_pkglicensedir}/{Apache-License,MIT-license,PSF-license,simplified_bsd,BSD-3-Clause}.txt
%doc README.md changelogs/CHANGELOG-v2.2?.rst
%dir %{_sysconfdir}/ansible/
%config(noreplace) %{_sysconfdir}/ansible/*
%{_bindir}/ansible*
%{_datadir}/ansible/
%if %{with argcomplete}
%{bash_completions_dir}/ansible*
%{fish_completions_dir}/ansible*.fish
%endif
%{_mandir}/man1/ansible*

%files doc
%doc ansible-documentation-%{uversion}/docs/docsite/rst
%if %{with docs}
%doc ansible-documentation-%{uversion}/docs/docsite/_build/html
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.3-1
- Prepare for Oreon 11 (RP1)
