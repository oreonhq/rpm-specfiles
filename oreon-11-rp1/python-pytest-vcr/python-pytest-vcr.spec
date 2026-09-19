%global source0_hash 23ee51b75abbcc43d926272773aae4f39f93aceb75ed56852d0bf618f92e1896

%global pypi_name pytest-vcr
%global file_name pytest_vcr
%global desc Py.test plugin for managing VCR.py cassettes

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        28%{?dist}
Summary:        %{desc}

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-vcr
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
BuildRequires:  python3-setuptools_scm
Requires:       python3-pytest >= 2.7
Requires:       python3-vcrpy

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{file_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
