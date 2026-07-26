%global source0_hash d56eeaa48fbc3e2ec4bd0e089983e7fa3f70ddba137c5c3786edd2aebc2e2e65

Name:           python-pydaraja
Version:        0.3.7
Release:        %autorelease
Summary:        Python wrapper for Mpesa's Daraja API

License:        MIT
URL:            https://github.com/raykipkorir/pydaraja
Source:         %{url}/archive/v%{version}/pydaraja-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This Python wrapper allows developers to seamlessly interact with the MPESA's
Daraja API and manage payment requests within their Python applications.

It streamlines and abstracts the complexity of integrating with the MPESA's
Daraja API, providing developers with a convenient and efficient means of
handling payment transactions.}

%description %_description

%package -n     python3-pydaraja
Summary:        %{summary}

%description -n python3-pydaraja %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pydaraja-%{version}
# Relax setuptools version
sed -i 's/"setuptools>=80.8.0", "setuptools_scm==8.3.1"/"setuptools", "setuptools_scm"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pydaraja

%check
%pyproject_check_import
%pytest

%files -n python3-pydaraja -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md

%changelog
%autochangelog
