%global source0_hash 2375379969541d82dd4fdd4bdced39d64716fbae52eb05ed9569c126d62aecad
Name:           python-brukerapi
Version:        0.4.6
Release:        1%{?dist}
Summary:        Python package providing I/O interface for Bruker data sets
License:        MIT
URL:            https://github.com/isi-nmr/brukerapi-python
Source0:        https://github.com/isi-nmr/brukerapi-python/archive/v%{version}/brukerapi-python-%{version}.tar.gz
Source10:       bruker.1
Source11:       bruker-filter.1
Source12:       bruker-report.1
Source13:       bruker-split.1
BuildArch:      noarch
%global common_description %{expand:
A Python package providing I/O interface for Bruker data sets.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-brukerapi = %{version}-%{release}
# /oreon:deps
%package -n       python3-brukerapi+dev
Summary:        Metapackage for python3-brukerapi dev extras
Requires:       python3-brukerapi = %{version}-%{release}
Requires:       python3dist(ruff) == 0.16.0
Provides:       python3dist(brukerapi[dev]) = %{version}-%{release}

%description -n python3-brukerapi+dev
Metapackage for python3-brukerapi dev extras.

%description %{common_description}

%package -n python3-brukerapi
Summary:        Python package providing I/O interface for Bruker data sets
Obsoletes:      python-brukerapi-doc < 0.1.10-1
# oreon:reqs
Requires:       python3dist(numpy) >= 2.1
# /oreon:reqs
%description -n python3-brukerapi %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'
%oreon_autofiles python3-brukerapi usr/lib/python3*/site-packages/brukerapi* usr/lib64/python3*/site-packages/brukerapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/brukerapi* usr/lib64/python3*/site-packages/brukerapi* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

mkdir test/zenodo_zips
for zip in '0.2H2.zip' \
    '20200612_094625_lego_phantom_3_1_2.zip' \
    '20210128_122257_LEGO_PHANTOM_API_TEST_1_1.zip'
do
    %{python3} -m zipfile -c "test/zenodo_zips/${zip}"
done
ignore="${ignore-} --ignore=test/test_split.py"
ignore="${ignore-} --ignore=test/test_jcampdx.py"
ignore="${ignore-} --ignore=test/test_random_access.py"
ignore="${ignore-} --ignore=test/test_dataset.py"
%pytest -v ${ignore-}
%files
%files -n python3-brukerapi -f %{oreon_filedir}/python3-brukerapi.list

%changelog

%autochangelog
