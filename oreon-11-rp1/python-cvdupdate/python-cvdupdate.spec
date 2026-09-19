%global source0_hash 5b873cd8b88a45debeb5c2a13d82b329c9fd6010f5118da8807adbb23240bf0e

%global pypi_name cvdupdate

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        ClamAV Private Database Mirror Updater Tool

License:        Apache-2.0
URL:            https://github.com/Cisco-Talos/cvdupdate
# pypi_source is missing fixtures
Source0:        %{url}/archive/%{pypi_name}-%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A tool to download and update clamav databases and database patch files
for the purposes of hosting your own database mirror.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{pypi_name}-%{version}
sed -i -e '1{\@^#!@d}' cvdupdate/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}/tests
%pyproject_save_files cvdupdate

%check
%pytest -v

%files -n python3-cvdupdate -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/cvd
%{_bindir}/cvdupdate

%changelog
%autochangelog
