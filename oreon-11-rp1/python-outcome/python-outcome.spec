%global source0_hash 9dcf02e65f2971b80047b377468e72a268e15c0af3cf1238e6ff14f7f91143b8
Name:           python-outcome
Version:        1.3.0.post0
Release:        1%{?dist}
Summary:        Capture the outcome of Python function calls
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/outcome
Source0:        https://files.pythonhosted.org/packages/source/o/outcome/outcome-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-outcome = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-outcome
Summary:        Capture the outcome of Python function calls
BuildRequires:  python3-devel
%description -n python3-outcome

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n outcome-%{version}
sed -i '/^pytest-cov\b/d' test-requirements.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-outcome usr/lib/python3*/site-packages/outcome* usr/lib64/python3*/site-packages/outcome* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/outcome* usr/lib64/python3*/site-packages/outcome* usr/bin/*

%check

%pytest
%files
%files -n python3-outcome -f %{oreon_filedir}/python3-outcome.list

%changelog

%autochangelog
