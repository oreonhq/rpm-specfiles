%global source0_hash 39d97c3377e1630abff3a94d8c956980f77a3e809e27a0376dd7d30abe3b6959

%bcond check 0

%global srcname astroplan

Name:           python-%{srcname}
Version:        0.10.1
Release:        %autorelease
Summary:        Python package to help astronomers plan observations

License:        BSD-3-Clause
URL:            https://pypi.org/project/astroplan/
Source0:        %{pypi_source}
# https://github.com/astropy/astroplan/issues/416
Patch:          astroplan-fixed-apo.patch

BuildArch:   noarch
ExcludeArch: %{ix86}

%global _description %{expand:
astroplan is an observation planning package for 
astronomers that can help you plan for everything but the clouds.

It is an in-development Astropy affiliated package that seeks to make your 
life as an observational astronomer a little less infuriating.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files astroplan

%check
# Most test rely on an internet database of coordinates
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst

%changelog
%autochangelog
