%global source0_hash fdc86bad6af9afa919cd107610c382f2546405ff5a5137547e51178552fa764c

%global __python        %__python3
%global python          python3
%global python_pfx      python3
%global rpm_python      python3-rpm
%global sitelib         %python3_sitelib

%global copr_common_version 1.1.1dev

# do not build debuginfo sub-packages
%define debug_package %nil

%define latest_requires() \
Requires: %1 \
%{expand: %%global latest_requires_packages %1 %%{?latest_requires_packages}}

Name:    copr-rpmbuild
Version: 1.6
Summary: Run COPR build tasks
Release: 3%{?dist}
URL: https://github.com/fedora-copr/copr
License: GPL-2.0-or-later

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz
 	

%if 0%{?fedora} > 41
ExcludeArch:   %{ix86}
%endif

BuildRequires: %{python}-copr-common >= %copr_common_version
BuildRequires: %{python}-daemon
BuildRequires: %{python}-devel
BuildRequires: %{python}-distro
BuildRequires: %{python}-httmock
BuildRequires: %{rpm_python}
BuildRequires: asciidoc
BuildRequires: dist-git-client
BuildRequires: git
BuildRequires: %{python}-setuptools
BuildRequires: %{python}-pytest
BuildRequires: %{python_pfx}-munch
BuildRequires: %{python}-requests
BuildRequires: %{python_pfx}-jinja2
BuildRequires: %{python_pfx}-specfile >= 0.21.0
BuildRequires: python3-backoff >= 1.9.0
BuildRequires: python3-pyyaml
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: subscription-manager
%endif

BuildRequires: /usr/bin/argparse-manpage
BuildRequires: python-rpm-macros
BuildRequires: systemd-rpm-macros

%if "%{?python}" == "python2"
BuildRequires: python2-configparser
BuildRequires: python2-mock
Requires: python2-configparser
%endif

Requires: %python
Requires: %{python}-copr-common >= %copr_common_version
Requires: %{python_pfx}-jinja2
Requires: %{python_pfx}-munch
Requires: %{python}-requests
Requires: %{python_pfx}-specfile >= 0.21.0
Requires: python3-backoff >= 1.9.0
Requires: python3-daemon
Requires: python3-pyyaml

Requires: mock >= 5.0
Requires(pre): mock-filesystem
Requires: git
Requires: git-svn
# for the /bin/unbuffer binary
Requires: expect
%if 0%{?openEuler} > 0 || 0%{?rhel} > 0
# qemu-user-static is not supported
%else
Requires: qemu-user-static
%endif
Requires: sed

%if 0%{?fedora} || 0%{?rhel} > 7
Recommends: rpkg
Recommends: python-srpm-macros
Recommends: dist-git-client
Suggests: tito
Suggests: rubygem-gem2rpm
Suggests: pyp2rpm
Suggests: pyp2spec >= 0.10.0
%endif

%description
Provides command capable of running COPR build-tasks.
Example: copr-rpmbuild 12345-epel-7-x86_64 will locally
build build-id 12345 for chroot epel-7-x86_64.

%package -n copr-builder
Summary: copr-rpmbuild with all weak dependencies
Requires: %{name} = %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} < 41
# replacement for yum/yum-utils, to be able to work with el* chroots
# bootstrap_container.
Requires: dnf-yum
Requires: dnf-utils
%endif
# selinux toolset to allow running ansible against the builder
Requires: python3-libselinux
Requires: python3-libsemanage
%if 0%{?openEuler}
# for mock to allow: config_opts['nosync'] = True
Requires: nosync
%endif
Requires: openssh-clients
Requires: podman
%if 0%{?openEuler} > 0 || 0%{?rhel} > 0
# not supported
%else
Requires: pyp2rpm
Requires: pyp2spec >= 0.10.0
Requires: rubygem-gem2rpm
Requires: scl-utils-build
Requires: fedora-review >= 0.8
Requires: fedora-review-plugin-java
%endif
# We need %%pypi_source defined, which is in 3-29+
Requires: python-srpm-macros >= 3-29
Requires: rpkg
Requires: rsync
Requires: tito
# yum* to allow mock to build against el* chroots without bootstrap_container
%if 0%{?rhel}
Requires: yum
Requires: yum-utils
%endif

# We want those to be always up-2-date
%latest_requires ca-certificates
%latest_requires distribution-gpg-keys
%if 0%{?fedora} >= 38
%latest_requires dnf5
%latest_requires dnf5-plugins
%endif

%latest_requires python3-dnf
%latest_requires dist-git-client
%latest_requires dnf-plugins-core
%latest_requires libdnf
%latest_requires librepo
%latest_requires libsolv
%latest_requires mock
%latest_requires mock-core-configs
%latest_requires system-rpm-config
%latest_requires rpm

%description -n copr-builder
Provides command capable of running COPR build-tasks.
Example: copr-rpmbuild 12345-epel-7-x86_64 will locally
build build-id 12345 for chroot epel-7-x86_64.

This package contains all optional modules for building SRPM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
for script in bin/copr-rpmbuild*; do
    sed -i '1 s|#.*python.*|#! /usr/bin/%python|' "$script"
done

%check
PYTHON=%{python} ./run_tests.sh -vv --no-coverage

%build
name="%{name}" version="%{version}" summary="%{summary}" %py_build
a2x -d manpage -f manpage man/copr-rpmbuild.1.asciidoc

%global mock_config_overrides %_sysconfdir/copr-rpmbuild/mock-config-overrides

cat > copr-update-builder <<'EOF'
#! /bin/sh

# Update the Copr builder machine, can be called anytime Copr build system
# decides to do so (please keep the script idempotent).

# install the latest versions of those packages
dnf update -y %latest_requires_packages *rpm-macros

# The mock-core-configs package was potentially updated above, and it provides
# "noreplace" %%config files.  It means that - if the builder cloud image had
# baked-in locally _changed_ configuration files - the updated official
# configuration files from mock-core-configs package wouldn't be used.  So now
# make sure that they _are_ used (those, if any, would reside in .rpmnew files).
find /etc/mock -name '*.rpmnew' | while read -r rpmnew_file; do
    config=${rpmnew_file%%.rpmnew}
    mv -f "$config" "$config.copr-builder-backup" && \
    mv "$rpmnew_file" "$config"
done

# And now use the overrides from %%mock_config_overrides directory
(
  cd %mock_config_overrides
  find . -name '*.tpl' -o -name '*.cfg' | while read -r file; do
    base=$(basename "$file")
    dir=%_sysconfdir/mock/$(dirname "$file")
    mkdir -p "$dir"
    cp "$file" "$dir"
  done
)
EOF

%install
install -d %{buildroot}%mock_config_overrides
install -d %{buildroot}%{_sharedstatedir}/copr-rpmbuild
install -d %{buildroot}%{_sharedstatedir}/copr-rpmbuild/results
install -d %{buildroot}%{_sharedstatedir}/copr-rpmbuild/workspace

install -d %{buildroot}%{_bindir}
install -m 755 main.py %{buildroot}%{_bindir}/copr-rpmbuild
install -m 644 main.ini %{buildroot}%{_sysconfdir}/copr-rpmbuild/main.ini
install -m 644 mock.cfg.j2 %{buildroot}%{_sysconfdir}/copr-rpmbuild/mock.cfg.j2
install -m 644 rpkg.conf.j2 %{buildroot}%{_sysconfdir}/copr-rpmbuild/rpkg.conf.j2
install -m 644 mock-source-build.cfg.j2 %{buildroot}%{_sysconfdir}/copr-rpmbuild/
install -m 644 mock-custom-build.cfg.j2 %{buildroot}%{_sysconfdir}/copr-rpmbuild/
install -m 644 copr-rpmbuild.yml %{buildroot}%{_sysconfdir}/copr-rpmbuild/copr-rpmbuild.yml

cat <<EOF > %buildroot%mock_config_overrides/README
Contents of this directory is used by %_bindir/copr-update-builder script.
When the script is executed, all files and directories (recursively) from here
are automatically copied to /etc/mock directory.  The files in /etc/mock are
overwritten if they already exist.
EOF

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/copr-rpmbuild.1 %{buildroot}/%{_mandir}/man1/
install -p -m 755 bin/copr-builder* %buildroot%_bindir
install -p -m 755 bin/copr-sources-custom %buildroot%_bindir
install -p -m 755 bin/copr-rpmbuild-cancel %buildroot%_bindir
install -p -m 755 bin/copr-rpmbuild-log %buildroot%_bindir
install -p -m 755 bin/copr-rpmbuild-loggify %buildroot%_bindir

name="%{name}" version="%{version}" summary="%{summary}" %py_install

install -p -m 755 copr-update-builder %buildroot%_bindir

(
  cd builder-hooks
  find -name README | while read line; do
    dir=%buildroot%_sysconfdir"/copr-builder/hooks/$(dirname "$line")"
    mkdir -p "$dir"
    install -p -m 644 "$line" "$dir"
  done
)

mkdir %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/copr-builder.conf <<EOF
d /run/copr-builder 0775 root mock -
EOF

%files
%{!?_licensedir:%global license %doc}
%license LICENSE

%sitelib/copr_rpmbuild*

%{_bindir}/copr-rpmbuild*
%{_bindir}/copr-sources-custom
%{_mandir}/man1/copr-rpmbuild.1*

%dir %attr(0775, root, mock) %{_sharedstatedir}/copr-rpmbuild
%dir %attr(0775, root, mock) %{_sharedstatedir}/copr-rpmbuild/results
%dir %attr(0775, root, mock) %{_sharedstatedir}/copr-rpmbuild/workspace

%dir %{_sysconfdir}/copr-rpmbuild
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/main.ini
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/mock.cfg.j2
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/rpkg.conf.j2
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/mock-source-build.cfg.j2
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/mock-custom-build.cfg.j2
%config(noreplace) %{_sysconfdir}/copr-rpmbuild/copr-rpmbuild.yml

%files -n copr-builder
%license LICENSE
%_bindir/copr-builder
%_bindir/copr-update-builder
%_bindir/copr-builder-cleanup
%_bindir/copr-builder-rhsm-subscribe
%_bindir/copr-builder-rhsm-subscribe-daemon
%_bindir/copr-builder-ready
%_sysconfdir/copr-builder
%dir %mock_config_overrides
%doc %mock_config_overrides/README
%ghost %attr(775,root,mock) %dir %_rundir/copr-builder
%_tmpfilesdir/copr-builder.conf

%changelog
%autochangelog
