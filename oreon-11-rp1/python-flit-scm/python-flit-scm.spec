%global source0_hash 961bd6fb24f31bba75333c234145fff88e6de0a90fc0f7e5e7c79deca69f6bb2
Name:           python-flit-scm
Version:        1.7.0
Release:        1%{?dist}
Summary:        PEP 518 build backend that uses setuptools_scm and flit
License:        MIT
URL:            https://pypi.org/pypi/flit_scm
Source0:        https://files.pythonhosted.org/packages/source/f/flit_scm/flit_scm-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.5
BuildRequires:  python3dist(setuptools-scm) >= 6.4
Requires:       python3-flit-scm = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-flit-scm
Summary:        PEP 518 build backend that uses setuptools_scm and flit
BuildRequires:  python3-devel
# oreon:reqs
Requires:       python3dist(flit-core) >= 3.5
Requires:       python3dist(setuptools-scm) >= 6.4
# /oreon:reqs
%description -n python3-flit-scm

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir flit_scm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flit-scm usr/lib/python3*/site-packages/flit_scm* usr/lib64/python3*/site-packages/flit_scm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flit_scm* usr/lib64/python3*/site-packages/flit_scm* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-flit-scm -f %{oreon_filedir}/python3-flit-scm.list

%changelog

%autochangelog
