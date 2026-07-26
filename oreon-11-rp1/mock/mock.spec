%global source0_hash 6093c779f1950a1a5afd8fcb2cda3e0f67031a03bf4b115972af9464da138e40

%bcond_with lint
%bcond_without tests

# Modern distributions (using RPM v4.20+; for example, Fedora 42+) do not
# require the %%pre scriptlet for creating users/groups because the sysusers
# feature is now built directly into RPM.  Simply including the sysusers
# `mock.conf` file in a package payload is sufficient to leverage this feature.
# However, for older distributions that lack this capability, we still define
# the %%pre scriptlet.
%if 0%{?fedora} < 42 || (0%{?rhel} && 0%{?rhel} <= 10) || (0%{?mageia} && 0%{?mageia} < 10) || (0%{?suse_version} && 0%{?suse_version} < 1660)
%bcond_without sysusers_compat
%else
%bcond_with sysusers_compat
%endif

%global __python %{__python3}
%global python_sitelib %{python3_sitelib}

Summary: Builds packages inside chroots
Name: mock
Version: 6.7
Release: 1%{?dist}
License: GPL-2.0-or-later
# Source is created by
# git clone https://github.com/rpm-software-management/mock.git
# cd mock
# git reset --hard %%{name}-%%{version}
# tito build --tgz
Source: https://github.com/rpm-software-management/%{name}/releases/download/%{name}-%{version}-1/%{name}-%{version}.tar.gz
URL: https://github.com/rpm-software-management/mock/
BuildArch: noarch
Requires: tar
Requires: pigz
%if 0%{?mageia}
Requires: usermode-consoleonly
%else
Requires: usermode
%endif
Requires: createrepo_c

# We know that the current version of mock isn't compatible with older variants,
# and we want to enforce automatic upgrades.
Conflicts: mock-core-configs < 33

# Requires 'mock-core-configs', or replacement (GitHub PR#544).
Requires: mock-configs
Requires: %{name}-filesystem = %{version}-%{release}
# This is still preferred package providing 'mock-configs'
Suggests: mock-core-configs

Requires: systemd
%if 0%{?fedora} || 0%{?rhel}
Requires: systemd-container
%endif
Requires: coreutils
%if 0%{?fedora}
Suggests: iproute
%endif
%if 0%{?mageia}
Suggests: iproute2
%endif
BuildRequires: bash-completion
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-jinja2
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-rpm
Requires: python%{python3_pkgversion}-pyroute2
Requires: python%{python3_pkgversion}-templated-dictionary >= 1.5
Requires: python%{python3_pkgversion}-backoff
BuildRequires: python%{python3_pkgversion}-backoff
BuildRequires: python%{python3_pkgversion}-devel
%if %{with lint}
BuildRequires: python%{python3_pkgversion}-pylint
%endif
BuildRequires: python%{python3_pkgversion}-rpm
BuildRequires: python%{python3_pkgversion}-rpmautospec-core

BuildRequires: argparse-manpage

%if 0%{?fedora} >= 38 || 0%{?rhel} >= 11 || 0%{?mageia} >= 10 || 0%{?suse_version} >= 1600
# DNF5 stack
Recommends: dnf5
Recommends: dnf5-plugins
%endif

# DNF4 stack
Recommends: python3-dnf
Recommends: python3-dnf-plugins-core

# YUM stack, dnf-utils replace yum-utils
Recommends: yum
Recommends: dnf-utils

Recommends: btrfs-progs
Suggests: qemu-user-static
Suggests: procenv
Recommends: buildah
Recommends: podman
Recommends: skopeo
Recommends: fuse-overlayfs

%if %{with tests}
BuildRequires: python%{python3_pkgversion}-distro
BuildRequires: python%{python3_pkgversion}-jinja2
BuildRequires: python%{python3_pkgversion}-jsonschema
BuildRequires: python%{python3_pkgversion}-pyroute2
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-templated-dictionary
%endif

%if 0%{?fedora} || 0%{?rhel}
BuildRequires: perl-interpreter
%else
BuildRequires: perl
%endif
# hwinfo plugin
Requires: util-linux
Requires: coreutils
Requires: procps-ng
Requires: shadow-utils

%description
Mock takes an SRPM and builds it in a chroot.

%package scm
Summary: Mock SCM integration module
Requires: %{name} = %{version}-%{release}
Recommends: cvs
Recommends: git
Recommends: subversion
Recommends: tar

# We could migrate to 'copr-distgit-client'
Recommends: rpkg

%description scm
Mock SCM integration module.

%package lvm
Summary: LVM plugin for mock
Requires: %{name} = %{version}-%{release}
Requires: lvm2

%description lvm
Mock plugin that enables using LVM as a backend and support creating snapshots
of the buildroot.

%package rpmautospec
Summary: Rpmautospec plugin for mock
Requires: %{name} = %{version}-%{release}
# This lets mock determine if a spec file needs to be processed with rpmautospec.
Requires: python%{python3_pkgversion}-rpmautospec-core

%description rpmautospec
Mock plugin that preprocesses spec files using rpmautospec.

%package filesystem
Summary:  Mock filesystem layout
Requires(pre):  shadow-utils
BuildRequires:  systemd-rpm-macros

%if %{with sysusers_compat}
Requires(pre): shadow-utils
%endif

%description filesystem
Filesystem layout and group for Mock.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
for file in py/mock.py py/mock-parse-buildlog.py; do
  sed -i 1"s|#!/usr/bin/python3 |#!%{__python} |" $file
done

%build
for i in py/mockbuild/constants.py py/mock-parse-buildlog.py; do
    perl -p -i -e 's|^VERSION\s*=.*|VERSION="%{version}"|' $i
    perl -p -i -e 's|^SYSCONFDIR\s*=.*|SYSCONFDIR="%{_sysconfdir}"|' $i
    perl -p -i -e 's|^PYTHONDIR\s*=.*|PYTHONDIR="%{python_sitelib}"|' $i
    perl -p -i -e 's|^PKGPYTHONDIR\s*=.*|PKGPYTHONDIR="%{python_sitelib}/mockbuild"|' $i
done
for i in docs/mock.1 docs/mock-parse-buildlog.1; do
    perl -p -i -e 's|\@VERSION\@|%{version}"|' $i
done

./precompile-bash-completion "mock.complete"

argparse-manpage --pyfile ./py/mock-hermetic-repo.py --function _argparser > mock-hermetic-repo.1

%install
#base filesystem
mkdir -p %{buildroot}%{_sysconfdir}/mock/eol/templates
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libexecdir}/mock
install mockchain %{buildroot}%{_bindir}/mockchain
install py/mock-hermetic-repo.py %{buildroot}%{_bindir}/mock-hermetic-repo
install py/mock-parse-buildlog.py %{buildroot}%{_bindir}/mock-parse-buildlog
install py/mock.py %{buildroot}%{_libexecdir}/mock/mock
ln -s consolehelper %{buildroot}%{_bindir}/mock
 
install -d %{buildroot}%{_sysconfdir}/pam.d
cp -a etc/pam/* %{buildroot}%{_sysconfdir}/pam.d/

install -d %{buildroot}%{_sysconfdir}/mock
cp -a etc/mock/* %{buildroot}%{_sysconfdir}/mock/

install -d %{buildroot}%{_sysconfdir}/security/console.apps/
cp -a etc/consolehelper/mock %{buildroot}%{_sysconfdir}/security/console.apps/%{name}

install -d %{buildroot}%{_datadir}/bash-completion/completions/
cp -a etc/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/
cp -a mock.complete %{buildroot}%{_datadir}/bash-completion/completions/mock
ln -s mock %{buildroot}%{_datadir}/bash-completion/completions/mock-parse-buildlog

install -d %{buildroot}%{_sysconfdir}/pki/mock
cp -a etc/pki/* %{buildroot}%{_sysconfdir}/pki/mock/

install -d %{buildroot}%{python_sitelib}/
cp -a py/mockbuild %{buildroot}%{python_sitelib}/

install -d %{buildroot}%{_mandir}/man1
cp -a docs/mock.1 docs/mock-parse-buildlog.1 mock-hermetic-repo.1 %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_datadir}/cheat
cp -a docs/mock.cheat %{buildroot}%{_datadir}/cheat/mock

install -d %{buildroot}/var/lib/mock
install -d %{buildroot}/var/cache/mock

mkdir -p %{buildroot}%{_pkgdocdir}
install -p -m 0644 docs/buildroot-lock-schema-*.json %{buildroot}%{_pkgdocdir}
install -p -m 0644 docs/site-defaults.cfg %{buildroot}%{_pkgdocdir}

mkdir -p %{buildroot}%{_sysusersdir}
install -p -D -m 0644 %{name}.conf %{buildroot}%{_sysusersdir}

sed -i 's/^_MOCK_NVR = None$/_MOCK_NVR = "%name-%version-%release"/' \
    %{buildroot}%{_libexecdir}/mock/mock

%if %{with sysusers_compat}
%pre filesystem
# Some of these older distributions do not ship with the %%sysusers_*_compat.
# Instead of another ifdef/else here, we prefer to hardcode the scriptlet
# content here.
getent group 'mock' >/dev/null || groupadd -f -g '135' -r 'mock' || :
%endif

%check
%if %{with lint}
# ignore the errors for now, just print them and hopefully somebody will fix it one day
pylint-3 py/mockbuild/ py/*.py py/mockbuild/plugins/* || :
%endif

%if %{with tests}
./run-tests.sh --no-cov
%endif

%files
%dir %{_pkgdocdir}/
%doc %{_pkgdocdir}/site-defaults.cfg
%doc %{_pkgdocdir}/buildroot-lock-schema-*.json
%{_datadir}/bash-completion/completions/mock
%{_datadir}/bash-completion/completions/mock-parse-buildlog

# executables
%{_bindir}/mock
%{_bindir}/mockchain
%{_bindir}/mock-hermetic-repo
%{_bindir}/mock-parse-buildlog
%{_libexecdir}/mock

# python stuff
%{python_sitelib}/*
%exclude %{python_sitelib}/mockbuild/scm.*
%exclude %{python_sitelib}/mockbuild/__pycache__/scm.*
%exclude %{python_sitelib}/mockbuild/plugins/lvm_root.*
%exclude %{python_sitelib}/mockbuild/plugins/__pycache__/lvm_root.*
%exclude %{python_sitelib}/mockbuild/plugins/rpmautospec.*
%exclude %{python3_sitelib}/mockbuild/plugins/__pycache__/rpmautospec.*.py*

# config files
%config(noreplace) %{_sysconfdir}/%{name}/*.ini
%config(noreplace) %{_sysconfdir}/%{name}/hermetic-build.cfg
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}

# directory for personal gpg keys
%dir %{_sysconfdir}/pki/mock
%config(noreplace) %{_sysconfdir}/pki/mock/*

# docs
%{_mandir}/man1/mock.1*
%{_mandir}/man1/mock-parse-buildlog.1*
%{_mandir}/man1/mock-hermetic-repo.1*
%{_datadir}/cheat/mock

%files scm
%{python_sitelib}/mockbuild/scm.py*
%{python3_sitelib}/mockbuild/__pycache__/scm.*.py*

%files lvm
%{python_sitelib}/mockbuild/plugins/lvm_root.*
%{python3_sitelib}/mockbuild/plugins/__pycache__/lvm_root.*.py*

%files rpmautospec
%{python_sitelib}/mockbuild/plugins/rpmautospec.*
%{python3_sitelib}/mockbuild/plugins/__pycache__/rpmautospec.*.py*

%files filesystem
%license COPYING
%dir  %{_sysconfdir}/mock
%dir  %{_sysconfdir}/mock/eol
%dir  %{_sysconfdir}/mock/eol/templates
%dir  %{_sysconfdir}/mock/templates
%dir  %{_datadir}/cheat
%config(noreplace) %{_sysusersdir}/mock.conf

# cache & build dirs, writeable by mock group
%defattr(0775, root, mock, 0775)
%dir %{_localstatedir}/cache/mock
%dir %{_localstatedir}/lib/mock

%changelog
%autochangelog
