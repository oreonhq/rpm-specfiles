%global source0_hash b4c25890bb75050d54c08123d2733156b78a59a2555f5461f69b0e44cd91242f

%global pypi_name launchpadlib
Name:           python-%{pypi_name}
Version:        2.1.0
Release:        %autorelease
Summary:        Script Launchpad through its web services interfaces

License:        LGPL-3.0-only
URL:            https://launchpad.net/launchpadlib 
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Launchpadlib is an open-source Python library that lets you treat the HTTP
resources published by Launchpad's web service as Python objects responding
to a standard set of commands. With launchpadlib you can integrate your
applications into Launchpad without knowing a lot about HTTP client
programming.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x keyring,testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest src/%{pypi_name}/tests/*py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
