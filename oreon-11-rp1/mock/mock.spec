%global source0_hash e8e52342741d064dbdd126b0aed82fd970643b9012aa25c3aa9bf48b480494cf
%bcond_with lint
%bcond_without tests
%bcond_with sysusers_compat
%global __python %{__python3}
%global python_sitelib %{python3_sitelib}
Summary:        Builds packages inside chroots
Name: mock
Version: 6.8
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://github.com/rpm-software-management/%{name}/releases/download/%{name}-%{version}-1/%{name}-%{version}.tar.gz
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
Conflicts: mock-core-configs < 33
Requires: mock-configs
Requires: %{name}-filesystem = %{version}-%{release}
Suggests: mock-core-configs
Requires: systemd
Requires: coreutils
%if 0%{?mageia}
Suggests: iproute2
%endif
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-jinja2
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-rpm
Requires: python%{python3_pkgversion}-pyroute2
Requires: python%{python3_pkgversion}-templated-dictionary >= 1.5
Requires: python%{python3_pkgversion}-backoff
%if %{with lint}
%endif
Recommends: python3-dnf
Recommends: python3-dnf-plugins-core
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
%endif
Requires: util-linux
Requires: coreutils
Requires: procps-ng
Requires: shadow-utils
# oreon:deps
BuildRequires:  argparse-manpage
BuildRequires:  bash-completion
BuildRequires:  perl
BuildRequires:  python3-backoff
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-jinja2
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pyroute2
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-rpm
BuildRequires:  python3-rpmautospec-core
BuildRequires:  python3-templated-dictionary
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Mock takes an SRPM and builds it in a chroot.

%package scm
Summary: Mock SCM integration module
Requires: %{name} = %{version}-%{release}
Recommends: cvs
Recommends: git
Recommends: subversion
Recommends: tar
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with sysusers_compat}
%pre filesystem

getent group 'mock' >/dev/null || groupadd -f -g '135' -r 'mock' || :
%endif
%check

%if %{with lint}
pylint-3 py/mockbuild/ py/*.py py/mockbuild/plugins/* || :
%endif
%if %{with tests}
./run-tests.sh --no-cov
%endif
%files -f %{oreon_filedir}/main.list
%files -n mock-scm -f %{oreon_filedir}/mock-scm.list
%files -n mock-lvm -f %{oreon_filedir}/mock-lvm.list
%files -n mock-rpmautospec -f %{oreon_filedir}/mock-rpmautospec.list
%files -n mock-filesystem -f %{oreon_filedir}/mock-filesystem.list

%changelog

%autochangelog
