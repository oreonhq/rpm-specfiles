%global source0_hash cab9f54e382707c31eb5ad58e1ce3b371ecd0d5d4f3385f9cf01bd13a2e1d9ec

%global pkg_name flask-paranoid

Name:           python-%{pkg_name}
Version:        0.3.0
Release:        17%{?dist}
Summary:        Flask Simple user session protection
License:        MIT

URL:            https://github.com/miguelgrinberg/%{pkg_name}
Source0:        %{url}/archive/v%{version}/%{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
Flask Simple user session protection.

%package -n python3-%{pkg_name}
Summary:        Flask Simple user session protection

%description -n python3-%{pkg_name}
Flask Simple user session protection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

# Fix incorrect date format in test
sed -r -i 's/01-Jan-1970/01 Jan 1970/' tests/test_paranoid.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_paranoid

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
