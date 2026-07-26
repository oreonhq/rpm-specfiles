%global source0_hash 9bc78b40143b4ef33bf569e515408c2996ffebefbb1a897616ebe8aa6f2d7e75

%global pypi_name stone
Name:           python-%{pypi_name}
Version:        3.2.1
Release:        22%{?dist}
Summary:        The Official Api Spec Language for Dropbox
License:        MIT

URL:            https://github.com/dropbox/stone
Source0:        %pypi_source

# Remove pytest-runner / setup.py test support
# https://github.com/dropbox/stone/pull/354
# Rebased on v3.2.1, without changes to CONTRIBUTING.md (not in the sdist)
Patch:          0001-Remove-pytest-runner-setup.py-test-support.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import -t

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/stone

%changelog
%autochangelog
