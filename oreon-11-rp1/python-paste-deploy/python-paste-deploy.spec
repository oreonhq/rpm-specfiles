%global source0_hash 9ddbaf152f8095438a9fe81f82c78a6714b92ae8e066bed418b6a7ff6a095a95

%global desc This tool provides code to load WSGI applications and servers from\
URIs; these URIs can refer to Python Eggs for INI-style configuration\
files.  PasteScript provides commands to serve applications based on\
this configuration file.
%global sum Load, configure, and compose WSGI applications and servers
%global srcname PasteDeploy
# this has a circular dependency on python-paste and python-paste-script
%bcond tests 1

Name:           python-paste-deploy
Version:        3.1.0
Release:        13%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://github.com/Pylons/pastedeploy
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
#BuildRequires:  python3-pytest-cov
BuildRequires:  python3-paste-script
%endif

%description
%{desc}

%package -n python3-paste-deploy
Summary:        %{sum}

#Requires:       python3-paste
Requires:       python3-setuptools

%description -n python3-paste-deploy
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# disable coverage tests
sed -i 's/ --cov//' pytest.ini

%install
%pyproject_install
%pyproject_save_files paste
rm -rf %{buildroot}%{python3_sitelib}/test

%check
%pyproject_check_import -e paste.deploy.paster_templates
%if %{with tests}
%pytest
%endif

%files -n python3-paste-deploy -f %{pyproject_files}
%license license.txt
%{python3_sitelib}/PasteDeploy-%{version}-py*-nspkg.pth

%changelog
%autochangelog
