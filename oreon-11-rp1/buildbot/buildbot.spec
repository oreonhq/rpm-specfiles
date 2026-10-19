%global source0_hash cbf46a15004bb1229712285e4f2b98163a169868ea00783e5e0d7cf8d5e8d962
%bcond check 1
%bcond_with docs
%bcond_without ec2
%bcond_without container
%bcond_without libvirt
%bcond_without openstack
Name:           buildbot
Version:        4.3.0
Release:        7%{?dist}
Summary:        Build/test automation system
License:        GPL-2.0-only
URL:            https://buildbot.net
Source0:        https://files.pythonhosted.org/packages/source/b/buildbot/buildbot-%{version}.tar.gz
Source1:        %{pypi_source buildbot_worker}
Source2:        %{pypi_source buildbot_www}
Source3:        %{pypi_source buildbot_waterfall_view}
Source4:        %{pypi_source buildbot_grid_view}
Source5:        %{pypi_source buildbot_console_view}
Source6:        %{pypi_source buildbot_badges}
Source7:        %{pypi_source buildbot_wsgi_dashboards}
Source8:        %{pypi_source buildbot_pkg}
Source10:       buildbot-master@.service
Source11:       buildbot-worker@.service
Source12:       buildbot-master-fedora.conf
Source13:       buildbot-worker-fedora.conf
BuildArch:      noarch
%if %{with check}
%endif
%if %{with docs}
%endif
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
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-buildbot = %{version}-%{release}
# /oreon:deps
%description
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

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
%package www
Summary:        Build/test automation system web frontend
Requires:       %{name}-master = %{version}-%{release}
%description www
Provides web frontend for buildbot.

%package doc
Summary:        Buildbot documentation
%description doc
%{summary}.

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

%build

%pyproject_wheel
%if %{with docs}
pushd docs
make docs.tgz VERSION="%{version}" SPHINXBUILD=sphinx-build-3
popd
%endif
pushd ../%{name}_worker-%{version}
%pyproject_wheel
popd
export BUILDBOT_VERSION=%{version}
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
export BUILDBOT_VERSION=%{version}
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
pushd ../%{name}_worker-%{version}
%pyproject_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/buildbot-worker.1
install -m0644 -D buildbot.sysusers.conf %{buildroot}%{_sysusersdir}/buildbot.conf
install -m0644 -D buildbot-worker.sysusers.conf %{buildroot}%{_sysusersdir}/buildbot-worker.conf
popd
rm -vf %{buildroot}%{_bindir}/*windows*
mkdir -p %{buildroot}%{_unitdir}
cp -a %{S:10} %{S:11} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/buildbot-master@.service.d
install -m0644 %{S:12} %{buildroot}%{_unitdir}/buildbot-master@.service.d/fedora.conf
mkdir -p %{buildroot}%{_unitdir}/buildbot-worker@.service.d
install -m0644 %{S:13} %{buildroot}%{_unitdir}/buildbot-worker@.service.d/fedora.conf
mkdir -p %{buildroot}%{_sharedstatedir}/buildbot/{master,worker}
%oreon_autofiles buildbot-master usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-master-ec2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-master-container usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-master-libvirt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-master-openstack usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-worker usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-www usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles buildbot-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

trial buildbot.test
%endif
%files
%files -n buildbot-master -f %{oreon_filedir}/buildbot-master.list
%files -n buildbot-master-ec2 -f %{oreon_filedir}/buildbot-master-ec2.list
%files -n buildbot-master-container -f %{oreon_filedir}/buildbot-master-container.list
%files -n buildbot-master-libvirt -f %{oreon_filedir}/buildbot-master-libvirt.list
%files -n buildbot-master-openstack -f %{oreon_filedir}/buildbot-master-openstack.list
%files -n buildbot-worker -f %{oreon_filedir}/buildbot-worker.list
%files -n buildbot-www -f %{oreon_filedir}/buildbot-www.list
%files -n buildbot-doc -f %{oreon_filedir}/buildbot-doc.list

%changelog

%autochangelog
