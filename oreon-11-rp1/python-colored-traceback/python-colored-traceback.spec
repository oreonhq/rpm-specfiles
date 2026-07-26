%global source0_hash 6da7ce2b1da869f6bb54c927b415b95727c4bb6d9a84c4615ea77d9872911b05

Name:           python-colored-traceback
Version:        0.3.0
Release:        18%{?dist}
Summary:        A library to color exception traces

License:        ISC
URL:            https://github.com/staticshock/colored-traceback.py
Source0:        %{pypi_source colored-traceback}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Colored-traceback is a python library to color exception traces.}

%description %_description

%package -n python3-colored-traceback
Summary:        %{summary}

%description -n python3-colored-traceback %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n colored-traceback-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%py3_check_import colored_traceback

%files -n python3-colored-traceback
%doc README.rst
%{python3_sitelib}/colored_traceback-%{version}.dist-info/
%{python3_sitelib}/colored_traceback/

%changelog
%autochangelog
