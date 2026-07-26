%global source0_hash b11b7884a2b735c415a81f6b6aa3a2e233c68d012e12df9b6092d29737224f19

%global pypi_name cotyledon

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        6%{?dist}
Summary:        Cotyledon provides a framework for defining long-running services

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://cotyledon.readthedocs.io
Source0:        %{pypi_source}
# Upstream code already uses unittest.mock but the metadata still specifies mock
# Maintainers, please upstream
Patch0:         python-cotyledon-rm-python-mock-usage.diff

BuildArch:      noarch

%package -n python3-%{pypi_name}
Summary:        Cotyledon provides a framework for defining long-running services
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{pypi_name}
Cotyledon provides a framework for defining long-running services.

%package doc
Summary:    Documentation for %{name}

%description doc
Cotyledon provides a framework for defining long-running services.

This package contains documentation in HTML format.

%description
Cotyledon provides a framework for defining long-running services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test -x doc -x oslo

%build
%pyproject_wheel

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 -b html doc/source html
# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest ||:

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files doc
%doc html

%changelog
%autochangelog
