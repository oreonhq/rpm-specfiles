%global source0_hash f64b123a0c8037ab46915996bc61364fd6160f0ed03f89cffcb7c3a5fc7b07d2

%define with_admin 1
%define with_client 1
%define with_django 1
%define with_hub 1
%define with_worker 1

Name:           kobo
Version:        0.41.0
Release:        2%{?dist}
License:        LGPL-2.1-only
Summary:        Python modules for tools development
URL:            https://github.com/release-engineering/kobo
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Kobo is a set of python modules designed for rapid tools development.

%if 0%{?with_admin}
%package admin
Summary:        Kobo admin script for instant project deployment
Requires:       python3-%{name}-admin

%description admin
Kobo admin provides templates for various kobo-based projects,
incl. CLI, hub client, worker and hub.
%endif

%package -n python3-%{name}
Summary:        Python modules for tools development
Requires:       %{py3_dist six}
%py_provides    python3-%{name}

%description -n python3-%{name}
Kobo is a set of python modules designed for rapid tools development.

%if 0%{?with_django}
%package -n python3-%{name}-django
Summary:        Django components
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(django) >= 1.11
Requires:       python3-setuptools
%py_provides    python3-%{name}-django

%description -n python3-%{name}-django
Django components.
%endif

%if 0%{?with_client}
%package -n python3-%{name}-client
Summary:        CLI client
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-requests-gssapi
%py_provides    python3-%{name}-client

%description -n python3-%{name}-client
CLI client.
%endif

%if 0%{?with_worker}
%package -n python3-%{name}-worker
Summary:        Worker daemon processing tasks submitted to the hub
Requires:       python3-%{name} = %{version}-%{release}
%py_provides    python3-%{name}-worker

%description -n python3-%{name}-worker
Worker daemon processing tasks submitted to the hub.
%endif

%if 0%{?with_hub}
%package -n python3-%{name}-hub
Summary:        XML-RPC and web interface to a task database
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(django) >= 1.11
Requires:       python3-setuptools
Requires:       gzip
%py_provides    python3-%{name}-hub

%description -n python3-%{name}-hub
Hub is a XML-RPC and web interface to a task database.
%endif

%package -n python3-%{name}-rpmlib
Summary:        Functions to manipulate with RPM files
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-rpm
Requires:       python3-koji
%py_provides    python3-%{name}-rpmlib

%description -n python3-%{name}-rpmlib
Rpmlib contains functions to manipulate with RPM files.

%if 0%{?with_admin}
%package -n python3-%{name}-admin
Summary:        Kobo admin script for instant project deployment
Requires:       python3-%{name} >= %{version}
Requires:       python3dist(django) >= 1.11
%py_provides    python3-%{name}-admin

%description -n python3-%{name}-admin
Python library for kobo-admin command.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%py3_shebang_fix kobo/admin/kobo-admin kobo/admin/templates/*/*

%build
%py3_build

%install
%py3_install

%if ! 0%{?with_admin}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/admin
rm -rf $RPM_BUILD_ROOT/%{_bindir}/kobo-admin
%endif

%if ! 0%{?with_client}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/client
%endif

%if ! 0%{?with_django}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/django
%endif

%if ! 0%{?with_hub}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/hub
%endif

%if ! 0%{?with_worker}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/worker
%endif

%if 0%{?with_admin}
%files admin
%{_bindir}/kobo-admin
%endif

%files -n python3-%{name}
%dir %{python3_sitelib}/kobo
%{python3_sitelib}/kobo/*.py*
%{python3_sitelib}/kobo/__pycache__
%exclude %{python3_sitelib}/kobo/rpmlib.py*
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%doc AUTHORS
%license COPYING LICENSE

%if 0%{?with_django}
%files -n python3-%{name}-django
%{python3_sitelib}/kobo/django
%endif

%if 0%{?with_client}
%files -n python3-%{name}-client
%{python3_sitelib}/kobo/client
%endif

%if 0%{?with_worker}
%files -n python3-%{name}-worker
%{python3_sitelib}/kobo/worker
%endif

%if 0%{?with_hub}
%files -n python3-%{name}-hub
%{python3_sitelib}/kobo/hub
%endif

%files -n python3-%{name}-rpmlib
%{python3_sitelib}/kobo/rpmlib.py*

%if 0%{?with_admin}
%files -n python3-%{name}-admin
%{python3_sitelib}/kobo/admin
%endif

%changelog
%autochangelog
