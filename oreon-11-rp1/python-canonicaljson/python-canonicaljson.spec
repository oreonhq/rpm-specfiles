%global source0_hash c3c38d76aacdb2d29c61582d466850116affabe5186ae921f48bc5c8f720b10f
%bcond check 0
Name:           python-canonicaljson
Version:        2.0.0
Release:        1%{?dist}
Summary:        Canonical JSON
License:        Apache-2.0
URL:            https://github.com/matrix-org/python-canonicaljson
Source0:        https://github.com/matrix-org/%{name}/archive/v%{version}/canonicaljson-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 35.0.2
Requires:       python3-canonicaljson = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-canonicaljson
Summary:        Canonical JSON
%description -n python3-canonicaljson

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-canonicaljson usr/lib/python3*/site-packages/canonicaljson* usr/lib64/python3*/site-packages/canonicaljson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/canonicaljson* usr/lib64/python3*/site-packages/canonicaljson* usr/bin/*
%if %{with check}
%check

%tox -e py
%endif
%files
%files -n python3-canonicaljson -f %{oreon_filedir}/python3-canonicaljson.list

%changelog

%autochangelog
