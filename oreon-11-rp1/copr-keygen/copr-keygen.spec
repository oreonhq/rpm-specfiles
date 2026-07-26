%global source0_hash 3086b6e35af0c9424e5ea4a9076070ff82a37f843e2d62fea63bbbc9e9a9b660

%global with_test 1
%global copr_common_version 0.16.3.dev

Name:       copr-keygen
Version:    2.2
Release:    4%{?dist}
Summary:    Part of Copr build system. Aux service that generate keys for signd

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch
BuildRequires: util-linux
BuildRequires: systemd

BuildRequires: python3-devel
BuildRequires: python3-copr-common >= %copr_common_version
BuildRequires: python3-flask

# doc
BuildRequires: make

# for tests
BuildRequires: python3-pytest

Requires:   crontabs
Requires:   haveged
Requires:   gnupg2
Requires:   python3-mod_wsgi
Requires:   httpd
Requires:   obs-signd
Requires:   passwd

Recommends: logrotate
Requires:   python3-copr-common >= %copr_common_version
Requires:   python3-setuptools
Requires:   python3-flask

# tests
Requires:   python3-pytest
Requires:   python3-pytest-cov

%description -n copr-keygen
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latest builds.

This package contains aux service that generate keys for package signing.

%if 0%{?fedora}
%package -n copr-keygen-doc
Summary:    Code documentation for copr-keygen component of Copr buildsystem
Obsoletes:  copr-doc < 1.38

BuildRequires: python3-devel
BuildRequires: python3-requests
BuildRequires: python3-flask
BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-httpdomain

%description doc
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latests builds.

This package contains document for copr-keygen service.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# We currently have FTBFS errors for F37/Rawhide, related issues:
# https://bugzilla.redhat.com/show_bug.cgi?id=2113156
# https://bugzilla.redhat.com/show_bug.cgi?id=2105348
# https://bugzilla.redhat.com/show_bug.cgi?id=2007282
%if 0%{?fedora} <= 36 && 0%{?fedora}
make -C docs %{?_smp_mflags} html
%endif

%install
%pyproject_install
find %{buildroot} -name '*.exe' -delete

install -d %{buildroot}%{_sysconfdir}/copr-keygen
install -d %{buildroot}%{_sysconfdir}/sudoers.d
install -d %{buildroot}%{_pkgdocdir}
install -d %{buildroot}%{_pkgdocdir}/httpd
install -d %{buildroot}%{_pkgdocdir}/sign
install -d %{buildroot}%{_datadir}/copr-keygen
install -d %{buildroot}%{_bindir}
install -d -m 500 %{buildroot}%{_sharedstatedir}/copr-keygen/phrases
install -d -m 500 %{buildroot}%{_sharedstatedir}/copr-keygen/gnupg
install -d %{buildroot}%{_localstatedir}/log/copr-keygen
install -d %{buildroot}%{_sysconfdir}/logrotate.d/
install -d %{buildroot}%{_sysconfdir}/cron.daily

%{__install} -p -m 0755 run/gpg_copr.sh %{buildroot}/%{_bindir}/gpg_copr.sh
%{__install} -p -m 0755 run/gpg-copr %{buildroot}/%{_bindir}/
%{__install} -p -m 0755 run/gpg-copr-prolong %{buildroot}/%{_bindir}/

%{__install} -p -m 0755 run/application.py %{buildroot}%{_datadir}/copr-keygen/
%{__install} -p -m 0644 configs/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/copr-keygen

%{__install} -p -m 0755 configs/cron.daily %{buildroot}%{_sysconfdir}/cron.daily/copr-keygen

cp -a configs/sudoers/copr_signer %{buildroot}%{_sysconfdir}/sudoers.d/copr_signer

# FTBFS - See above
%if 0%{?fedora} <= 36 && 0%{?fedora}
cp -a docs/_build/html %{buildroot}%{_pkgdocdir}/
%{__install} -p -m 0644 configs/httpd/copr-keygen.conf.example %{buildroot}%{_pkgdocdir}/httpd/
%{__install} -p -m 0644 configs/sign/sign.conf.example %{buildroot}%{_pkgdocdir}/sign/sign.conf.example
%endif

install -m0644 -D configs/copr-keygen.sysusers.conf %{buildroot}%{_sysusersdir}/copr-keygen.conf

%check
./run_tests.sh -vv --no-cov

%post
systemctl condrestart httpd &>/dev/null || :

%postun
systemctl condrestart httpd &>/dev/null || :

%files
%license LICENSE
%doc docs/INSTALL.rst docs/README.rst
%doc configs/local_settings.py.example

%{_datadir}/copr-keygen/*
%{python3_sitelib}/*

%{_bindir}/gpg_copr.sh
%{_bindir}/gpg-copr
%{_bindir}/gpg-copr-prolong

%config %{_sysconfdir}/cron.daily/*
%config %{_sysconfdir}/logrotate.d/copr-keygen
%config %{_sysconfdir}/sudoers.d/copr_signer

# Only copr-signer owned files go below!
%defattr(600, copr-signer, copr-signer, 700)
%{_sharedstatedir}/copr-keygen
%config(noreplace) %{_sysconfdir}/copr-keygen
%dir %{_localstatedir}/log/copr-keygen
%ghost %{_localstatedir}/log/copr-keygen/main.log
%{_sysusersdir}/copr-keygen.conf

%if 0%{?fedora}
%files -n copr-keygen-doc
%doc %{_pkgdocdir}
%endif

%changelog
%autochangelog
