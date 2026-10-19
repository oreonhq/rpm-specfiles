%global source0_hash 348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325
Name:               python-mccabe
Version:            0.7.0
Release:        1%{?dist}
Summary:        McCabe complexity checker
License:            MIT
URL:                http://pypi.python.org/pypi/mccabe
Source0:        https://files.pythonhosted.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
Patch:              https://github.com/PyCQA/mccabe/pull/92.patch
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mccabe = %{version}-%{release}
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-mccabe
Summary:        McCabe complexity checker
%description -n python%{python3_pkgversion}-mccabe

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mccabe-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/mccabe* usr/lib64/python3*/site-packages/mccabe* usr/bin/*

%check

%pytest -r fEs
%files
%files -n python3-mccabe -f %{oreon_filedir}/python3-mccabe.list

%changelog

%autochangelog
