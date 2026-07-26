%global source0_hash c2862cf046147c02c2b6a1d40957c5e73d6fd5421cf43f087a9f67e0dacd2258

%global pypi_name minikerberos

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        20%{?dist}
Summary:        Kerberos manipulation library in Python

License:        MIT
URL:            https://github.com/skelsec/minikerberos
Source0:        %pypi_source
BuildArch:      noarch

%description
Kerberos manipulation library in pure Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Kerberos manipulation library in pure Python

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for Kerberos manipulations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove shebangs. https://github.com/skelsec/minikerberos/issues/7
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py,*/*/*.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.dist-info

%files -n %{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
%autochangelog
