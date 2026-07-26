%global source0_hash 7017ba80de387cddbdf403201e950b8667e37c5773796874a7750098edd33e70

%global pypi_name sphinx-last-updated-by-git

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        21%{?dist}
Summary:        Get the "last updated" time for each Sphinx page from Git

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_last_updated_by_git

%files -n python3-%{pypi_name} -f %pyproject_files
%license LICENSE
%doc README.rst

%changelog
%autochangelog
