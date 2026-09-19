%global source0_hash bbb1c5e97f82953e2b4f72c97131d75a2e684b108a3d7a140c7f901512364b4c

# Enable Python dependency generation

# Missing dependencies for tests
%bcond check 1

# Missing dependencies for documentation
%bcond_with docs

# Offer support for various latent worker types
%bcond_without ec2
%bcond_without container
%bcond_without libvirt

%if 0%{?rhel} && 0%{?rhel} < 9
# Required client packages don't exist in RHEL or EPEL
%bcond_with openstack
%else
%bcond_without openstack
%endif

Name:           buildbot
Version:        4.3.0
Release:        7%{?dist}

Summary:        Build/test automation system
License:        GPL-2.0-only
URL:            https://buildbot.net
Source0:        %{pypi_source buildbot}
Source1:        %{pypi_source buildbot_worker}
Source2:        %{pypi_source buildbot_www}
Source3:        %{pypi_source buildbot_waterfall_view}
Source4:        %{pypi_source buildbot_grid_view}
Source5:        %{pypi_source buildbot_console_view}
Source6:        %{pypi_source buildbot_badges}
Source7:        %{pypi_source buildbot_wsgi_dashboards}
# Build-time only component for buildbot
Source8:        %{pypi_source buildbot_pkg}

# Service template units for buildbot instances
Source10:       buildbot-master@.service
Source11:       buildbot-worker@.service

# Fedora-specific systemd drop-ins (separate users, paths)
Source12:       buildbot-master-fedora.conf
Source13:       buildbot-worker-fedora.conf

BuildArch:      noarch

BuildRequires:  python3-devel

# For making the build work from source
BuildRequires:  python3dist(twisted) >= 17.9
BuildRequires:  python3dist(jinja2) >= 2.1
BuildRequires:  python3dist(zope-interface) >= 4.1.1
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(python-dateutil) >= 1.5
BuildRequires:  python3dist(txaio) >= 2.2.2
BuildRequires:  python3dist(autobahn) >= 0.16
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(pyyaml)

BuildRequires:  python3dist(treq)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(lz4)

%if %{with check}
BuildRequires:  bzr
BuildRequires:  cvs
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  subversion
BuildRequires:  darcs
%endif

%if %{with docs}
BuildRequires:  make
BuildRequires:  python3dist(sphinx) >= 1.4
BuildRequires:  python3dist(sphinxcontrib-blockdiag)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(pyenchant)
BuildRequires:  (python3dist(docutils) >= 0.8 with python3dist(docutils) < 0.13)
BuildRequires:  python3dist(sphinx-jinja)
BuildRequires:  python3dist(towncrier)
%endif

# For systemd units
BuildRequires:  systemd-rpm-macros

# Turns former package into a metapackage for installing everything
Requires:       %{name}-master = %{version}-%{release}
%if %{with ec2}
Recommends:     %{name}-master-ec2 = %{version}-%{release}
%endif
%if %{with container}
Recommends:     %{name}-master-container = %{version}-%{release}
%endif
%if %{with libvirt}
Recommends:     %{name}-master-libvirt = %{version}-%{release}
%endif
%if %{with openstack}
Recommends:     %{name}-master-openstack = %{version}-%{release}
%endif
Requires:       %{name}-worker = %{version}-%{release}
Requires:       %{name}-www = %{version}-%{release}
%if %{with docs}
Requires:       %{name}-doc = %{version}-%{release}
%else
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

%files
# Empty because metapackage
%exclude %{python3_sitelib}/*buildbot_pkg*
%exclude %{python3_sitelib}/__pycache__/*buildbot_pkg*

# ---------------------------------------------------------------------

%package master
Summary:        Build/test automation system master
Recommends:     %{name}-www = %{version}-%{release}
%if ! %{with docs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description master
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This package contains only the buildmaster implementation.
The buildbot-worker package contains the buildworker.

%post master
for master in $(systemctl list-units 'buildbot-master@*.service' --all --plain --no-legend | cut -d '@' -f 2 | cut -d '.' -f 1); do
  systemctl stop buildbot-master@"$master".service
  su - buildbot-master -s /bin/bash -c "buildbot upgrade-master /var/lib/buildbot/master/$master"
  systemctl start buildbot-master@"$master".service
done

%files master
%doc CREDITS NEWS UPGRADING
%license COPYING
%{_bindir}/buildbot
%{_mandir}/man1/buildbot.1*
%{python3_sitelib}/buildbot/
%{python3_sitelib}/buildbot-*dist-info/
%dir %{_sharedstatedir}/buildbot
%dir %attr(-, buildbot-master, buildbot-master) %{_sharedstatedir}/buildbot/master
%{_unitdir}/buildbot-master@.service
%{_unitdir}/buildbot-master@.service.d/fedora.conf

# ---------------------------------------------------------------------
%{_sysusersdir}/buildbot.conf

%if %{with ec2}
%package master-ec2
Summary:        Build/test automation system master -- AWS EC2 support
Requires:       %{name}-master = %{version}-%{release}
Requires:       python%{python3_version}dist(boto3)

%description master-ec2
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This is a metapackage to install the master with AWS EC2 dynamic
worker support.

%files master-ec2
# Empty because metapackage
%endif

# ---------------------------------------------------------------------

%if %{with container}
%package master-container
Summary:        Build/test automation system master -- Container support
Requires:       %{name}-master = %{version}-%{release}
Requires:       python%{python3_version}dist(docker)

%description master-container
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This is a metapackage to install the master with container worker support.

%files master-container
# Empty because metapackage
%endif

# ---------------------------------------------------------------------

%if %{with libvirt}
%package master-libvirt
Summary:        Build/test automation system master -- libvirt support
Requires:       %{name}-master = %{version}-%{release}
Requires:       python%{python3_version}dist(libvirt-python)

%description master-libvirt
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This is a metapackage to install the master with libvirt-driven dynamic
VM worker support.

%files master-libvirt
# Empty because metapackage
%endif

# ---------------------------------------------------------------------

%if %{with openstack}
%package master-openstack
Summary:        Build/test automation system master -- OpenStack support
Requires:       %{name}-master = %{version}-%{release}
Requires:       python%{python3_version}dist(keystoneauth1)
Requires:       python%{python3_version}dist(python-novaclient)

%description master-openstack
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This is a metapackage to install the master with OpenStack dynamic
worker support.

%files master-openstack
# Empty because metapackage
%endif

# ---------------------------------------------------------------------

%package worker
Summary:        Build/test automation system worker
%if ! %{with docs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description worker
This package contains only the buildworker implementation.
The buildbot-master package contains the buildmaster.

%post worker
for worker in $(systemctl list-units 'buildbot-worker@*.service' --all --plain --no-legend | cut -d '@' -f 2 | cut -d '.' -f 1); do
  systemctl restart buildbot-worker@"$worker".service
done

%files worker
%doc NEWS UPGRADING
%license COPYING
%{_bindir}/buildbot-worker
%{_mandir}/man1/buildbot-worker.1*
%{python3_sitelib}/buildbot_worker/
%{python3_sitelib}/buildbot_worker-*dist-info/
%dir %{_sharedstatedir}/buildbot
%dir %attr(-, buildbot-worker, buildbot-worker) %{_sharedstatedir}/buildbot/worker
%{_unitdir}/buildbot-worker@.service
%{_unitdir}/buildbot-worker@.service.d/fedora.conf
%{_sysusersdir}/buildbot-worker.conf

# ---------------------------------------------------------------------

%package www
Summary:        Build/test automation system web frontend
Requires:       %{name}-master = %{version}-%{release}

%description www
Provides web frontend for buildbot.

%files www
%license COPYING
%{python3_sitelib}/buildbot_www/
%{python3_sitelib}/buildbot_www-*.dist-info/
%{python3_sitelib}/buildbot_waterfall_view/
%{python3_sitelib}/buildbot_waterfall_view-*dist-info/
%{python3_sitelib}/buildbot_grid_view/
%{python3_sitelib}/buildbot_grid_view-*dist-info/
%{python3_sitelib}/buildbot_console_view/
%{python3_sitelib}/buildbot_console_view-*dist-info/
%{python3_sitelib}/buildbot_badges/
%{python3_sitelib}/buildbot_badges-*dist-info/
%{python3_sitelib}/buildbot_wsgi_dashboards/
%{python3_sitelib}/buildbot_wsgi_dashboards-*dist-info/

# ---------------------------------------------------------------------

%if %{with docs}
%package doc
Summary:        Buildbot documentation

%description doc
%{summary}.

%files doc
%{_pkgdocdir}/
%endif

# ---------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b0 -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8
cd ..
cd buildbot_worker-%{version}

# Create sysusers.d config files
cat >buildbot.sysusers.conf <<EOF
u buildbot-master - 'Service account for the Buildbot master' %{_sharedstatedir}/buildbot/master -
EOF

cat >buildbot-worker.sysusers.conf <<EOF
u buildbot-worker - 'Service account for the Buildbot worker' %{_sharedstatedir}/buildbot/worker -
EOF

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
#TODO create API documentation
pushd docs
make docs.tgz VERSION="%{version}" SPHINXBUILD=sphinx-build-3
popd
%endif

pushd ../%{name}_worker-%{version}
%pyproject_wheel
popd

# For buildbot_pkg build-time module to set version correctly
export BUILDBOT_VERSION=%{version}

# So that other modules can use buildbot-pkg import
export PYTHONPATH=%{_builddir}/%{name}-%{version}/build/lib:%{_builddir}/%{name}_pkg-%{version}/build/lib

bbweb_components=(pkg www waterfall_view grid_view console_view badges wsgi_dashboards)

for bbweb_component in ${bbweb_components[@]}; do
	pushd ../%{name}_${bbweb_component}-%{version}
	sed -e "s/^    setup_requires=.*$//" -i setup.py
	%pyproject_wheel
	popd
done

%install
%pyproject_install

# For buildbot_pkg build-time module to set version correctly
export BUILDBOT_VERSION=%{version}

# So that other modules can use buildbot-pkg import
export PYTHONPATH=%{_builddir}/%{name}-%{version}/build/lib:%{_builddir}/%{name}_pkg-%{version}/build/lib

bbweb_components=(www waterfall_view grid_view console_view badges wsgi_dashboards)

for bbweb_component in ${bbweb_components[@]}; do
	pushd ../%{name}_${bbweb_component}-%{version}
	%pyproject_install
	popd
done

install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/buildbot.1

%if %{with docs}
mkdir -p %{buildroot}%{_pkgdocdir}
tar xf docs/docs.tgz --strip-components=1 -C %{buildroot}%{_pkgdocdir}
%endif

# install worker files
pushd ../%{name}_worker-%{version}
%pyproject_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/buildbot-worker.1
install -m0644 -D buildbot.sysusers.conf %{buildroot}%{_sysusersdir}/buildbot.conf
install -m0644 -D buildbot-worker.sysusers.conf %{buildroot}%{_sysusersdir}/buildbot-worker.conf
popd

# Purge windows-only files
rm -vf %{buildroot}%{_bindir}/*windows*

# Install systemd units and Fedora drop-ins
mkdir -p %{buildroot}%{_unitdir}
cp -a %{S:10} %{S:11} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/buildbot-master@.service.d
install -m0644 %{S:12} %{buildroot}%{_unitdir}/buildbot-master@.service.d/fedora.conf
mkdir -p %{buildroot}%{_unitdir}/buildbot-worker@.service.d
install -m0644 %{S:13} %{buildroot}%{_unitdir}/buildbot-worker@.service.d/fedora.conf
mkdir -p %{buildroot}%{_sharedstatedir}/buildbot/{master,worker}

%if %{with check}
%check
trial buildbot.test
%endif

%changelog
%autochangelog
