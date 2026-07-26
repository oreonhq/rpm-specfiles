%global source0_hash 5bddedec6fcf4e963a957c270532599ccab798f41dfb335f00abe9c4b291cf9c

%global         pypi_name       tinygrad
%global         forgeurl        https://github.com/tinygrad/tinygrad
Version:        0.12.0
%forgemeta

Name:           python-%{pypi_name}
Release:        2%{?dist}
Summary:        You like pytorch? You like micrograd? You'll love tinygrad!

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  gcc
# Needed for test
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)
BuildArch: noarch

%global common_description %{expand:
tinygrad: For something between PyTorch and karpathy/micrograd. Maintained
by tiny corp.

This may not be the best deep learning framework, but it is a deep learning
framework.

Due to its extreme simplicity, it aims to be the easiest framework to add new
accelerators to, with support for both inference and training. If XLA is CISC,
tinygrad is RISC.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package  -n python3-%{pypi_name}-examples
Summary:  Examples for tinygrad
Requires: %{name} = %{version}-%{release}
Requires: python3-tiktoken
Requires: python3-pyopencl
Requires: clang

%description -n python3-%{pypi_name}-examples
Examples for tinygrad

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%py3_check_import %{pypi_name}
# Run CPU tests that do not need dependencies not in Fedora
# Modified from
# https://github.com/tinygrad/tinygrad/blob/master/.github/workflows/test.yml
# Tests only run on these arches
%ifarch aarch64 x86_64
PYTHON=1 SKIP_SLOW_TEST=1 %python3 -m pytest \
          test/test_assign.py \
          test/test_dtype_alu.py \
          test/test_gc.py \
          test/test_graph.py \
          test/test_jit.py \
          test/test_linearizer.py \
          test/test_multitensor.py \
          test/test_symbolic_jit.py \
          test/test_symbolic_ops.py \
          test/test_uops.py \
          test/unit/test_conv.py \
          %{nil}
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/quickstart.md docs/env_vars.md docs/mnist.md docs/runtime.md
%doc docs/*pdf docs/showcase.md docs/*svg
%doc docs/developer/ docs/showcase/ docs/tensor/
%doc docs/abstractions*.py

%files -n python3-%{pypi_name}-examples
%doc examples

%changelog
%autochangelog
