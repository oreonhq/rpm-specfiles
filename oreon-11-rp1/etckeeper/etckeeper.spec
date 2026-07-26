%global source0_hash ff0e95e3b6cf6f377b8a04f18f572b011e890eedc1a742b3c0e11ebc283f7a7e

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%if 0%{?fedora}
%global with_brz 1
%global with_dnf5 1
%endif

Name:      etckeeper
Version:   1.18.22
Release:   7%{?dist}
Summary:   Store /etc in a SCM system (git, mercurial, bzr or darcs)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       https://etckeeper.branchable.com/
Source0:   https://git.joeyh.name/index.cgi/etckeeper.git/snapshot/%{name}-%{version}.tar.gz
Source1:   README.fedora
Source2:   cron.daily
Source3:   etckeeper.actions
# build plugins separately
Patch0:    etckeeper-makefile-remove-python-plugins.patch
# see rhbz#1460461
Patch1:    etckeeper-1.18.7-fix-rpm-ignores.patch
# see rhbz#1480843
Patch2:    etckeeper-1.18.18-fix-hg-warnings.patch
# From https://bugs.launchpad.net/ubuntu/+source/etckeeper/+bug/1826855
Patch3:    etckeeper-add-breezy-python3-plugin.patch
# see rhbz#1762693 and https://github.com/ansible/ansible/issues/54949
# see also rhbz#1917461
Patch4:    etckeeper-1.18.18-fix-output-for-ansible.patch
# see rhbz#2203408 and pr#7
Patch5:    etckeeper-1.18.21-bz2203408.patch
BuildArch: noarch
BuildRequires: make
BuildRequires: %{_bindir}/markdown_py
Requires:  git-core
Requires:  perl-interpreter
Requires:  crontabs
Requires:  findutils
Requires:  hostname
Requires:  which
Requires:  %{name}-dnf = %{version}-%{release}
%if 0%{?with_dnf5}
Requires:  %{name}-dnf5 = %{version}-%{release}
%endif # with_dnf5
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The etckeeper program is a tool to let /etc be stored in a git,
mercurial, bzr or darcs repository. It hooks into yum to automatically
commit changes made to /etc during package upgrades. It tracks file
metadata that version control systems do not normally support, but that
is important for /etc, such as the permissions of /etc/shadow. It's
quite modular and configurable, while also being simple to use if you
understand the basics of working with version control.

The default backend is git, if want to use a another backend please
install the appropriate tool (mercurial, darcs or bzr).
%{?with_brz: To use breezy as bzr backend, please also install the %{name}-brz package.}

To start using the package please read %{_pkgdocdir}/README.

%if 0%{?with_brz}
%package brz
Summary:  Support for bzr with etckeeper (via breezy)
BuildRequires: python3-devel
BuildRequires: brz
Requires: %{name} = %{version}-%{release}
Requires: brz

%description brz
This package provides a brz (breezy) backend for etckeeper, if you want to use
etckeeper with (bzr) bazaar repositories, install this package.
%endif # with_brz

%package dnf
Summary:  DNF plugin for etckeeper support
BuildRequires: python3-devel
BuildRequires: python3-dnf
Requires: python3-dnf
BuildRequires: dnf-plugins-core
Requires: %{name} = %{version}-%{release}
Requires: dnf-plugins-core

%description dnf
This package provides a DNF plugin for etckeeper. If you want to use
etckeeper with DNF, install this package.

%if 0%{?with_dnf5}
%package dnf5
Summary:  DNF5 plugin for etckeeper support
Requires: %{name} = %{version}-%{release}
Requires: libdnf5-plugin-actions >= 5.2.11.0
Requires: sed

%description dnf5
This package provides a DNF5 plugin for etckeeper. If you want to use
etckeeper with DNF5, install this package.
%endif # with_dnf5

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -e 's|HIGHLEVEL_PACKAGE_MANAGER=.*|HIGHLEVEL_PACKAGE_MANAGER=dnf|' \
    -e 's|LOWLEVEL_PACKAGE_MANAGER=.*|LOWLEVEL_PACKAGE_MANAGER=rpm|' \
    -i etckeeper.conf
sed -e 's|^prefix=.*|prefix=%{_prefix}|' \
    -e 's|^bindir=.*|bindir=%{_bindir}|' \
    -e 's|^etcdir=.*|etcdir=%{_sysconfdir}|' \
    -e 's|^mandir=.*|mandir=%{_mandir}|' \
    -e 's|^vardir=.*|vardir=%{_localstatedir}|' \
    -e 's|^INSTALL=.*|INSTALL=install -p|' \
    -e 's|^CP=.*|CP=cp -pR|' \
    -e 's|^systemddir=.*|systemddir=%{_unitdir}|' \
    -i Makefile
# move each plugin in its own subdirectory, so each has its own build/
# directory
mkdir brz-plugin
mv etckeeper-brz brz-plugin
ln -snf etckeeper-brz/__init__.py brz-plugin/setup.py

mkdir dnf-plugin
mv etckeeper-dnf dnf-plugin
ln -snf etckeeper-dnf/etckeeper.py dnf-plugin/setup.py

cp -av %{SOURCE1} .

%generate_buildrequires
%if 0%{?with_brz}
cd brz-plugin
%pyproject_buildrequires
cd ..
%endif # with_brz

cd dnf-plugin
%pyproject_buildrequires
cd ..

%build
%make_build

%if 0%{?with_brz}
cd brz-plugin
%pyproject_wheel
cd ..
%endif # with_brz

cd dnf-plugin
%pyproject_wheel
cd ..

markdown_py -f README.html README.md

%install
%make_install

%if 0%{?with_brz}
cd brz-plugin
%pyproject_install
cd ..
%endif # with_brz

cd dnf-plugin
%pyproject_install
cd ..

install -D -p %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.daily/%{name}
install -d  %{buildroot}%{_localstatedir}/cache/%{name}

%if 0%{?with_dnf5}
install -D -p %{SOURCE3} %{buildroot}%{_sysconfdir}/dnf/libdnf5-plugins/actions.d/%{name}.actions
%endif # with_dnf5

%post
if [ $1 -gt 1 ] ; then
   %{_bindir}/%{name} update-ignore
fi
%systemd_post %{name}.service
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.service
%systemd_preun %{name}.timer

%postun
%systemd_postun %{name}.service
%systemd_postun %{name}.timer

%files
%doc README.html README.fedora
%license GPL
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*.d
%{_sysconfdir}/%{name}/daily
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_%{name}
%{_localstatedir}/cache/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%if 0%{?with_brz}
%files brz
# co-own the plugins directories
# breezy installs to sitearch
%dir %{python3_sitelib}/breezy/
%dir %{python3_sitelib}/breezy/plugins/
%{python3_sitelib}/breezy/plugins/%{name}/
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python3_sitelib}/brz_%{name}-*.dist-info
%endif # with_brz

%files dnf
%{python3_sitelib}/dnf-plugins/%{name}.py
%exclude %{python3_sitelib}/dnf-plugins/__init__.py
%{python3_sitelib}/dnf-plugins/__pycache__/%{name}.*
%exclude %{python3_sitelib}/dnf-plugins/__pycache__/__init__.*
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python3_sitelib}/dnf_%{name}-*.dist-info

%if 0%{?with_dnf5}
%files dnf5
%{_sysconfdir}/dnf/libdnf5-plugins/actions.d/%{name}.actions
%endif # with_dnf5

%changelog
%autochangelog
