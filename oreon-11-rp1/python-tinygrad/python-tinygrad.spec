%global source0_hash 437be6bb7481ec26e332e4f4342f6ea09e41258e62c5c09f4a9ed7aeb7829a07
Name:           python-tinygrad
Version:        0.14.0
Release:        1%{?dist}
Summary:        You like pytorch? You like micrograd? You love tinygrad! _3
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/t/tinygrad/tinygrad-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-tinygrad = %{version}-%{release}
# /oreon:deps
%package -n       python3-tinygrad+linting
Summary:        Metapackage for python3-tinygrad linting extras
Requires:       python3-tinygrad = %{version}-%{release}
Requires:       python3dist(mypy) == 1.19.1
Requires:       python3dist(ruff) == 0.14.10
Provides:       python3dist(tinygrad[linting]) = %{version}-%{release}

%description -n python3-tinygrad+linting
Metapackage for python3-tinygrad linting extras.

%package -n       python3-tinygrad+testing_minimal
Summary:        Metapackage for python3-tinygrad testing_minimal extras
Requires:       python3-tinygrad = %{version}-%{release}
Requires:       python3dist(torch) == 2.9.1
Requires:       python3dist(hypothesis) >= 6.148.9
Requires:       python3dist(z3-solver) < 4.15.4
Provides:       python3dist(tinygrad[testing_minimal]) = %{version}-%{release}

%description -n python3-tinygrad+testing_minimal
Metapackage for python3-tinygrad testing_minimal extras.

%package -n       python3-tinygrad+testing_unit
Summary:        Metapackage for python3-tinygrad testing_unit extras
Requires:       python3-tinygrad = %{version}-%{release}
Requires:       python3dist(gguf) >= 0.18
Provides:       python3dist(tinygrad[testing_unit]) = %{version}-%{release}

%description -n python3-tinygrad+testing_unit
Metapackage for python3-tinygrad testing_unit extras.

%package -n       python3-tinygrad+testing
Summary:        Metapackage for python3-tinygrad testing extras
Requires:       python3-tinygrad = %{version}-%{release}
Requires:       python3dist(onnx) == 1.19.0
Requires:       python3dist(numba) >= 0.55
Provides:       python3dist(tinygrad[testing]) = %{version}-%{release}

%description -n python3-tinygrad+testing
Metapackage for python3-tinygrad testing extras.

%package -n       python3-tinygrad+docs
Summary:        Metapackage for python3-tinygrad docs extras
Requires:       python3-tinygrad = %{version}-%{release}
Provides:       python3dist(tinygrad[docs]) = %{version}-%{release}

%description -n python3-tinygrad+docs
Metapackage for python3-tinygrad docs extras.

%package -n       python3-tinygrad+mesa
Summary:        Metapackage for python3-tinygrad mesa extras
Requires:       python3-tinygrad = %{version}-%{release}
Requires:       python3dist(tinymesa) == 25.2.7.2
Provides:       python3dist(tinygrad[mesa]) = %{version}-%{release}

%description -n python3-tinygrad+mesa
Metapackage for python3-tinygrad mesa extras.

%package -n       python3-tinygrad+autogen
Summary:        Metapackage for python3-tinygrad autogen extras
Requires:       python3-tinygrad = %{version}-%{release}
Provides:       python3dist(tinygrad[autogen]) = %{version}-%{release}

%description -n python3-tinygrad+autogen
Metapackage for python3-tinygrad autogen extras.

%description

%package -n     python3-tinygrad
Summary:        You like pytorch? You like micrograd? You love tinygrad! _3
%description -n python3-tinygrad

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tinygrad-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tinygrad usr/lib/python3*/site-packages/tinygrad* usr/lib64/python3*/site-packages/tinygrad* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tinygrad* usr/lib64/python3*/site-packages/tinygrad* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tinygrad -f %{oreon_filedir}/python3-tinygrad.list

%changelog

%autochangelog
