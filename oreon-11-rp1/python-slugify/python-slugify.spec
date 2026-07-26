%global source0_hash 09c8faf36b5703d0d9492ca68af71f09bd3d7d9e6761bf945ae261788fbebeeb

%global pypi_name slugify

Name:           python-slugify
Version:        8.0.4
Release:        4%{?dist}
Summary:        Python module to deal with unicode slugs

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/un33k/python-slugify
Source0:        %{url}/archive/v%{version}/python-%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
A Python slugify application that handles Unicode.

%package -n python3-%{pypi_name}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-text-unidecode
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python slugify application that handles Unicode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-%{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{__python3} test.py

%files -n python3-%{pypi_name}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
