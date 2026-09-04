%global source0_hash a69a97bec6ffc904a6fd4f25d662e327950352c62adc51d78d47e5ff4637076f

%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

%global module koji_containerbuild

%global owner release-engineering
%global project koji-containerbuild

%global commit 1.0.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{project}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Koji support for building layered container images

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/%{owner}/%{project}
Source0:        https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires: python3-setuptools

%description
Koji support for building layered container images

%package hub
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2
Summary:    Hub plugin that extend Koji to build layered container images
Requires:   koji-containerbuild
Requires:   koji-hub

%description hub
Hub plugin that extend Koji to support building layered container images

%package builder
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2
Summary:    Builder plugin that extend Koji to build layered container images
Requires:   koji-builder
Requires:   koji-containerbuild
Requires:   osbs-client
Requires:   python3-urlgrabber
Requires:   python3-dockerfile-parse
Requires:   python3-jsonschema

%description builder
Builder plugin that extend Koji to communicate with OpenShift build system and
build layered container images.

%package -n python3-%{name}-cli
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2
Summary:    CLI that communicates with Koji to control building layered container images
Requires:   python%{python3_pkgversion}-koji >= 1.13

%description -n python3-%{name}-cli
Builder plugin that extend Koji to communicate with OpenShift build system and
build layered container images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_prefix}/lib/koji-hub-plugins
%{__install} -p -m 0644 %{module}/plugins/hub_containerbuild.py $RPM_BUILD_ROOT%{_prefix}/lib/koji-hub-plugins/hub_containerbuild.py
%{__install} -d $RPM_BUILD_ROOT%{_prefix}/lib/koji-builder-plugins
%{__install} -p -m 0644 %{module}/plugins/builder_containerbuild.py $RPM_BUILD_ROOT%{_prefix}/lib/koji-builder-plugins/builder_containerbuild.py
%{__install} -d $RPM_BUILD_ROOT%{python3_sitelib}/koji_cli_plugins
%{__install} -p -m 0644 %{module}/plugins/cli_containerbuild.py $RPM_BUILD_ROOT%{python3_sitelib}/koji_cli_plugins/cli_containerbuild.py

%files
%{python3_sitelib}/*
%doc docs AUTHORS README.rst
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?_licensedir:%global license %doc}
%endif
%license LICENSE

%files -n python%{python3_pkgversion}-%{name}-cli
%{python3_sitelib}/koji_cli_plugins

%files hub
%{_prefix}/lib/koji-hub-plugins/hub_containerbuild.py*

%files builder
%{_prefix}/lib/koji-builder-plugins/builder_containerbuild.py*

%changelog
%autochangelog
