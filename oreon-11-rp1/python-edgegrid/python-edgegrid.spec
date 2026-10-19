%global source0_hash 4f3284ab357f4aae61f48f92023b4ed0b4ddfd966a3c6f569aa7ec0502d8cc4f
Name:           python-edgegrid
Version:        2.0.1
Release:        1%{?dist}
Summary:        Akamai EdgeGrid authentication handler for requests
License:        Apache-2.0
URL:            https://github.com/akamai/AkamaiOPEN-edgegrid-python
BuildArch:      noarch
Source0:        https://github.com/akamai/AkamaiOPEN-edgegrid-python/archive/v%{version}/edgegrid-python-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-edgegrid = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-edgegrid
Summary:        Akamai EdgeGrid authentication handler for requests
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-edgegrid

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir AkamaiOPEN-edgegrid-python-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-edgegrid usr/lib/python3*/site-packages/edgegrid* usr/lib64/python3*/site-packages/edgegrid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/edgegrid* usr/lib64/python3*/site-packages/edgegrid* usr/bin/*

%check

%pytest -v
%files
%files -n python3-edgegrid -f %{oreon_filedir}/python3-edgegrid.list

%changelog

%autochangelog
