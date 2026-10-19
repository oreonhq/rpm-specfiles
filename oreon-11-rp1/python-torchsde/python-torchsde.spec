%global source0_hash 7680ec86eb2a53918a66cead8ca0f6b50dd2fe36acfc909b546d336d269d2177
Name:           python-torchsde
Version:        0.2.6
Release:        1%{?dist}
Summary:        Differentiable SDE solvers with GPU support and efficient sensitivity analysis
License:        Apache-2.0
URL:            https://github.com/google-research/torchsde
Source0:        https://github.com/google-research/torchsde/archive/v%{version}/torchsde-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-torchsde = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-torchsde
Summary:        Differentiable SDE solvers with GPU support and efficient sensitivity analysis
%description -n python3-torchsde

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n torchsde-%{version}
# Should not have to do this...
sed -i -e 's@msg="CUDA not available."@reason="CUDA not available."@' tests/test*.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-torchsde usr/lib/python3*/site-packages/torchsde* usr/lib64/python3*/site-packages/torchsde* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/torchsde* usr/lib64/python3*/site-packages/torchsde* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-torchsde -f %{oreon_filedir}/python3-torchsde.list

%changelog

%autochangelog
