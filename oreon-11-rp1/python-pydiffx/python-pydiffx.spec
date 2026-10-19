%global source0_hash 0986dbb0a87cbf79e244e2f1c0e2b696d8e86b3861ea2955757a61d38e139228
Name:           python-pydiffx
Version:        1.1
Release:        15%{?dist}
Summary:        Python implementation of the DiffX specification
License:        MIT
URL:            https://diffx.org/pydiffx/
Source0:        https://files.pythonhosted.org/packages/source/p/pydiffx/pydiffx-%{version}.tar.gz
BuildArch:      noarch
Patch:          add_requirements.patch
Patch:          pydiffx-1.1-Fix-Python-3.12-compatibility.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pydiffx = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pydiffx
Summary:        Python implementation of the DiffX specification
%description -n python3-pydiffx

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pydiffx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydiffx usr/lib/python3*/site-packages/pydiffx* usr/lib64/python3*/site-packages/pydiffx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydiffx* usr/lib64/python3*/site-packages/pydiffx* usr/bin/*

%check

%pytest
%files
%files -n python3-pydiffx -f %{oreon_filedir}/python3-pydiffx.list

%changelog

%autochangelog
