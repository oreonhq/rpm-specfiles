%global source0_hash e3d3cb90f35f6cf9afa9bc850334687170255bd273a8cd21c0e7b0bb26d2ecfc
Name:           mrack
Version:        1.25.0
Release:        2%{?dist}
Summary:        Multicloud use-case based multihost async provisioner
License:        Apache-2.0
URL:            https://github.com/neoave/mrack
Source0:        https://github.com/neoave/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%global provider_plugins aws,beaker,openstack,podman,virt
Requires:       %{name}-cli = %{version}-%{release}
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       python3-%{name}-aws = %{version}-%{release}
Requires:       python3-%{name}-beaker = %{version}-%{release}
Requires:       python3-%{name}-openstack = %{version}-%{release}
Requires:       python3-%{name}-podman = %{version}-%{release}
Requires:       python3-%{name}-virt = %{version}-%{release}
%global __requires_exclude asyncopenstackclient
%{?python_disable_dependency_generator}
# oreon:deps
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
# /oreon:deps
%description
mrack is a provisioning tool and a library for CI and local multi-host
testing supporting multiple provisioning providers (e.g. AWS, Beaker,
Openstack). But in comparison to other multi-cloud libraries,
the aim is to be able to describe host from application perspective.

%package        cli
Summary:        Command line interface for mrack
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       python3-click
%package -n     python3-%{name}lib
Summary:        Core mrack libraries
Requires:       python3-pyyaml
Recommends:     python3-gssapi
Requires:       sshpass
%{?python_provide:%python_provide python3-%{name}lib}
%package -n     python3-%{name}-aws
Summary:        AWS provider plugin for mrack
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       python3-boto3
Requires:       python3-botocore
%{?python_provide:%python_provide python3-%{name}-aws}
%package -n     python3-%{name}-beaker
Summary:        Beaker provider plugin for mrack
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       beaker-client
%{?python_provide:%python_provide python3-%{name}-beaker}
%package -n     python3-%{name}-openstack
Summary:        Openstack provider plugin for mrack
Requires:       python3-%{name}lib = %{version}-%{release}
Recommends:       python3-aiofiles
Recommends:       python3-os-client-config
Recommends:     python3-AsyncOpenStackClient
Recommends:     python3-async-timeout
%{?python_provide:%python_provide python3-%{name}-openstack}
%package -n     python3-%{name}-podman
Summary:        Podman provider plugin for mrack
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       podman
%{?python_provide:%python_provide python3-%{name}-podman}
%package -n     python3-%{name}-virt
Summary:        Virtualization provider plugin for mrack using testcloud
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       testcloud
%{?python_provide:%python_provide python3-%{name}-virt}
%description        cli
%{name}-cli contains mrack command which functionality
can be extended by installing mrack plugins

%description -n     python3-%{name}lib
python3-%{name}lib contains core mrack functionalities
and static provider which can be used as a library

%description -n     python3-%{name}-aws
%{name}-aws is an additional plugin with AWS provisioning
library extending mrack package

%description -n     python3-%{name}-beaker
%{name}-beaker is an additional plugin with Beaker provisioning
library extending mrack package

%description -n     python3-%{name}-openstack
%{name}-openstack is an additional plugin with OpenStack provisioning
library extending mrack package

%description -n     python3-%{name}-podman
%{name}-podman is an additional plugin with Podman provisioning
library extending mrack package

%description -n     python3-%{name}-virt
%{name}-virt is an additional plugin with Virualization provisioning
library extending mrack package using testcloud

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove bundled egg-info
rm -r src/%{name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mrack-cli -f %{oreon_filedir}/mrack-cli.list
%files -n python3-mracklib -f %{oreon_filedir}/python3-mracklib.list
%files -n python3-mrack-aws -f %{oreon_filedir}/python3-mrack-aws.list
%files -n python3-mrack-beaker -f %{oreon_filedir}/python3-mrack-beaker.list
%files -n python3-mrack-openstack -f %{oreon_filedir}/python3-mrack-openstack.list
%files -n python3-mrack-podman -f %{oreon_filedir}/python3-mrack-podman.list
%files -n python3-mrack-virt -f %{oreon_filedir}/python3-mrack-virt.list

%changelog

%autochangelog
