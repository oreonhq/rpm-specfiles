%global source0_hash 36990209b94c2b834701cab243323044e6e77a2a9ea9f1ae86b039e4604d450f
Name:           python-datanommer-models
Version:        1.5.0
Release:        1%{?dist}
Summary:        SQLAlchemy models for datanommer
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-infra/datanommer
Source0:        https://files.pythonhosted.org/packages/source/d/datanommer_models/datanommer_models-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-datanommer-models = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-datanommer-models
Summary:        SQLAlchemy models for datanommer
%description -n python3-datanommer-models

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir datanommer_models-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-datanommer-models usr/lib/python3*/site-packages/datanommer_models* usr/lib64/python3*/site-packages/datanommer_models* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/datanommer_models* usr/lib64/python3*/site-packages/datanommer_models* usr/bin/*

%check

%pyproject_check_import -t
%files
%files -n python3-datanommer-models -f %{oreon_filedir}/python3-datanommer-models.list

%changelog

%autochangelog
