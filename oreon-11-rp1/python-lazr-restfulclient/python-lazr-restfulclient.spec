%global source0_hash 43f12a1d3948463b1462038c47b429dcb5e42e0ba7f2e16511b02ba5d2adffdb

%global pypi_name lazr.restfulclient
Name:           python-lazr-restfulclient
Version:        0.14.6
Release:        %autorelease
Summary:        Programmable client library for lazr.restful web services

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.restfulclient
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A programmable client library that takes advantage of the commonalities among
lazr.restful web services to provide added functionality on top of wadllib.}

%description %_description

%package -n     python3-lazr-restfulclient
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-lazr-restfulclient %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lazr

%check
%pyproject_check_import -e 'lazr.restfulclient.tests*'
#lazr.restful test dependency not packaged
#{python3} -m unittest ...

%files -n python3-lazr-restfulclient -f %{pyproject_files}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth

%changelog
%autochangelog
