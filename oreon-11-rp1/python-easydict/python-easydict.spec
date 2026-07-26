%global source0_hash b1eaedab1d1a4c5d8fd24d6bf0adc2a7ea259bebff6680a1bddcbe99e204370d

%global         pypi_name       easydict
Version:        1.10
%global         forgeurl        https://github.com/makinacorpus/easydict
%global         tag             %{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        11%{?dist}
Summary:        Access dict values as attributes (works recursively) 

License:        LGPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource} 

BuildRequires:  python3-devel
BuildArch: noarch

%global _description %{expand:
EasyDict allows to access dict values as attributes (works recursively).
A Javascript-like properties dot notation for python dicts.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
# No tests available

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%doc CHANGES

%changelog
%autochangelog
