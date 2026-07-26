%global source0_hash 12edede84df48b9cfb00373723a8700744c1b61748cdbb567b380eedb9f1bb43

%global pypi_name phply
%global author viraptor

Name:           python-%{pypi_name}
Version:        1.2.5
Release:        18%{?dist}
Summary:        PHP parser written in Python using PLY 

License:        BSD-3-Clause
URL:            https://github.com/%{author}/%{pypi_name}
Source0:        https://github.com/%{author}/%{pypi_name}/archive/refs/tags/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3dist(ply)
BuildRequires:  pyproject-rpm-macros

%generate_buildrequires
%pyproject_buildrequires

%description
phply is a parser for the PHP programming language written using PLY.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
phply is a parser for the PHP programming language written using PLY

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}/%{python3_sitelib}/tests
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/phplex
%{_bindir}/phpparse
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{python3_sitelib}/%{pypi_name}*.pth

%changelog
%autochangelog
