%global source0_hash 7680ec86eb2a53918a66cead8ca0f6b50dd2fe36acfc909b546d336d269d2177

# Testing results 0.2.6 ~F42
#
# Install and run manually by executing pytest int the src dir, without test modes, on x86 with radeon 7900:
# 3171 passed, 140 warnings
#
# From mock on similar system
# 1625 passed, 73 skipped, 114 warnings.
#
# The skipped tests are the GPU tests.

Name:           python-torchsde
Version:        0.2.6
Release:        %autorelease
Summary:        Differentiable SDE solvers with GPU support and efficient sensitivity analysis
License:        Apache-2.0
URL:            https://github.com/google-research/torchsde
Source:         %{url}/archive/v%{version}/torchsde-%{version}.tar.gz

BuildArch:      noarch
# PyTorch is only on x86_64, aarch64
ExclusiveArch:  x86_64 aarch64

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
PyTorch Implementation of Differentiable SDE Solvers Python package
This library provides stochastic differential equation (SDE) solvers
with GPU support and efficient backpropagation.}

%description %_description

%package -n     python3-torchsde
Summary:        %{summary}

%description -n python3-torchsde %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n torchsde-%{version}
# Should not have to do this...
sed -i -e 's@msg="CUDA not available."@reason="CUDA not available."@' tests/test*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l torchsde

%check
%pyproject_check_import
%pytest

%files -n python3-torchsde -f %{pyproject_files}
%doc DOCUMENTATION.md
%doc examples

%changelog
%autochangelog
