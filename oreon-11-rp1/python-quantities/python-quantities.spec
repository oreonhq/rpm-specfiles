%global source0_hash 7dcc3fd3e58de1821d487f01841ee3724ef6c16d139b1ccae38b6ef9fa3c3177

%global forgeurl https://github.com/python-quantities/python-quantities/
Name:           python-quantities
Version:        0.16.4
Release:        %autorelease
Summary:        Support for physical quantities with units, based on numpy

%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

%global _description %{expand:
Quantities is designed to handle arithmetic and conversions of physical
quantities, which have a magnitude, dimensionality specified by various units,
and possibly an uncertainty. See the tutorial for examples. Quantities builds
on the popular numpy library and is designed to work with numpy ufuncs, many of
which are already supported. Quantities is actively developed, and while the
current features and API are stable, test coverage is incomplete so the package
is not suggested for mission-critical applications.}

%description %{_description}

%package -n python3-quantities
Summary:    Support for physical quantities with units, based on numpy

%description -n python3-quantities %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l quantities

%check
PY_IGNORE_IMPORTMISMATCH=1 %pytest

%files -n python3-quantities -f %{pyproject_files}
%doc CHANGES.txt README.rst

%changelog
%autochangelog
