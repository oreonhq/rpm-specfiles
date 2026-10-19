%global source0_hash 6b094264c8d235178daf6249fb1e25561d35cdef8820097ff7aa582eb0a3be6d
%bcond tests 1
Name:           python-tcx2gpx
Version:        0.1.6
Release:        1%{?dist}
Summary:        Convert Garmin TPX to GPX
License:        GPL-3.0-only
URL:            https://gitlab.com/nshephard/tcx2gpx
Source0:        https://files.pythonhosted.org/packages/source/t/tcx2gpx/tcx2gpx-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-tcx2gpx = %{version}-%{release}
# /oreon:deps
%package -n       python3-tcx2gpx+dev
Summary:        Metapackage for python3-tcx2gpx dev extras
Requires:       python3-tcx2gpx = %{version}-%{release}
Provides:       python3dist(tcx2gpx[dev]) = %{version}-%{release}

%description -n python3-tcx2gpx+dev
Metapackage for python3-tcx2gpx dev extras.

%package -n       python3-tcx2gpx+docs
Summary:        Metapackage for python3-tcx2gpx docs extras
Requires:       python3-tcx2gpx = %{version}-%{release}
Provides:       python3dist(tcx2gpx[docs]) = %{version}-%{release}

%description -n python3-tcx2gpx+docs
Metapackage for python3-tcx2gpx docs extras.

%package -n       python3-tcx2gpx+pypi
Summary:        Metapackage for python3-tcx2gpx pypi extras
Requires:       python3-tcx2gpx = %{version}-%{release}
Provides:       python3dist(tcx2gpx[pypi]) = %{version}-%{release}

%description -n python3-tcx2gpx+pypi
Metapackage for python3-tcx2gpx pypi extras.

%package -n       python3-tcx2gpx+test
Summary:        Metapackage for python3-tcx2gpx test extras
Requires:       python3-tcx2gpx = %{version}-%{release}
Provides:       python3dist(tcx2gpx[test]) = %{version}-%{release}

%description -n python3-tcx2gpx+test
Metapackage for python3-tcx2gpx test extras.

%description

%package -n python3-tcx2gpx
Summary:        Convert Garmin TPX to GPX
%description -n python3-tcx2gpx

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tcx2gpx-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem tool.pytest.ini_options.addopts \
    '^--cov.*'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tcx2gpx usr/lib/python3*/site-packages/tcx2gpx* usr/lib64/python3*/site-packages/tcx2gpx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tcx2gpx* usr/lib64/python3*/site-packages/tcx2gpx* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%files
%files -n python3-tcx2gpx -f %{oreon_filedir}/python3-tcx2gpx.list

%changelog

%autochangelog
