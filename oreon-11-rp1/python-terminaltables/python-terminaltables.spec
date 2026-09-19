%global source0_hash c7aa01c2d2aa597773e34a21fb308cc976d627f50cec39aaae2c4f52f115d27f

%global        pypi_name terminaltables
%global        commit 8020b8cb8ae859891a999620085d34c8d8bfe1a3
Summary:       Generate tables in terminals from list of strings
Name:          python-terminaltables
Version:       3.1.10
Release:       20%{?dist}
License:       MIT
URL:           https://github.com/matthewdeanmartin/terminaltables
Source0:       https://github.com/matthewdeanmartin/terminaltables/archive/%{commit}.tar.gz
Patch0:        python-terminaltables-reqs.patch
Patch1:        python-terminaltables-fix-version.patch
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%global _description \
Easily draw tables in terminal/console applications (written in\
Python) from a list of lists of strings. Supports multi-line rows.
%description %_description

%package     -n python3-terminaltables
Summary:        %summary
%description -n python3-terminaltables %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n terminaltables-%{commit}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox || :

%files -n python3-terminaltables -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md

%changelog
%autochangelog
