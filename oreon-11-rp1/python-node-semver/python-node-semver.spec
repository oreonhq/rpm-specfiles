%global source0_hash bda71f31c2453fd3698d47dd62e7e9a49ba9c46217fb9223e143348544ceda16

%global pypi_name node-semver

%global _description %{expand:
Python version of node-semver library.

A "version" is described by the v2.0.0 specification found at
https://semver.org/.

A leading "=" or "v" character is stripped off and ignored.}

Name: python-%{pypi_name}
Version: 0.9.0
Release: 12%{?dist}

License: MIT
Summary: Python version of node-semver
URL: https://github.com/podhmo/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-pytest

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nodesemver

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.txt README.rst

%changelog
%autochangelog
