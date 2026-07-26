%global source0_hash e3d3cb90f35f6cf9afa9bc850334687170255bd273a8cd21c0e7b0bb26d2ecfc

Name:           mrack
Version:        1.25.0
Release:        2%{?dist}
Summary:        Multicloud use-case based multihost async provisioner

License:        Apache-2.0
URL:            https://github.com/neoave/mrack
Source0:        %{URL}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools

# coma separated list of provider plugins
%global provider_plugins aws,beaker,openstack,podman,virt

Requires:       %{name}-cli = %{version}-%{release}
Requires:       python3-%{name}lib = %{version}-%{release}
Requires:       python3-%{name}-aws = %{version}-%{release}
Requires:       python3-%{name}-beaker = %{version}-%{release}
Requires:       python3-%{name}-openstack = %{version}-%{release}
Requires:       python3-%{name}-podman = %{version}-%{release}
Requires:       python3-%{name}-virt = %{version}-%{release}

# We filter out the asyncopenstackclient dependency of this package
# so it is not forcing installation of missing dependencies in Fedora
# Once python3-AsyncOpenStackClient is in fedora we can drop this line
%global __requires_exclude asyncopenstackclient
%{?python_disable_dependency_generator}

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
%if 0%{?rhel} == 8
# c8s has missing beaker-client package
Recommends:     beaker-client
%else
Requires:       beaker-client
%endif

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

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md

%files cli
# the mrack man page RFE: https://github.com/neoave/mrack/issues/197
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/{,__pycache__/}run.*

%files -n python3-%{name}lib
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{name}/{,__pycache__/}run.*
%exclude %{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}osapi.*
%exclude %{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}testcloud.*
%exclude %{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}podman.*
%exclude %{python3_sitelib}/%{name}/providers/{,__pycache__/}{%{provider_plugins}}.*
%exclude %{python3_sitelib}/%{name}/transformers/{,__pycache__/}{%{provider_plugins}}.*

%files -n python3-%{name}-aws
%{python3_sitelib}/%{name}/transformers/{,__pycache__/}aws.*
%{python3_sitelib}/%{name}/providers/{,__pycache__/}aws.*

%files -n python3-%{name}-beaker
%{python3_sitelib}/%{name}/transformers/{,__pycache__/}beaker.*
%{python3_sitelib}/%{name}/providers/{,__pycache__/}beaker.*

%files -n python3-%{name}-openstack
%{python3_sitelib}/%{name}/transformers/{,__pycache__/}openstack.*
%{python3_sitelib}/%{name}/providers/{,__pycache__/}openstack.*
%{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}osapi.*

%files -n python3-%{name}-podman
%{python3_sitelib}/%{name}/transformers/{,__pycache__/}podman.*
%{python3_sitelib}/%{name}/providers/{,__pycache__/}podman.*
%{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}podman.*

%files -n python3-%{name}-virt
%{python3_sitelib}/%{name}/transformers/{,__pycache__/}virt.*
%{python3_sitelib}/%{name}/providers/{,__pycache__/}virt.*
%{python3_sitelib}/%{name}/providers/utils/{,__pycache__/}testcloud.*

%changelog
%autochangelog
