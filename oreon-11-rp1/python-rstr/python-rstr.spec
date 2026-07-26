%global source0_hash d46eff542a1a1ddcf3d5d23a2cd4cbd476d3298f5e73fe7741963e5c6a90a5cd

# Created by pyp2rpm-3.3.5
%global pypi_name rstr
%global _description %{expand:
rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications.}

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        17%{?dist}
Summary:        Generate random strings in Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://files.pythonhosted.org/packages/source/r/rstr/%{name}-%{version}.tar.gz
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description %_description

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rstr

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
%autochangelog
