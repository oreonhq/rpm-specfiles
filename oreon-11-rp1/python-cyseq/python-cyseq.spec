%global source0_hash e41e2e9c7698f8239d0f53b0745c746630030d804d0283e5a6fee62d29cfd22f
Name:           python-cyseq
Version:        0.1.3
Release:        1%{?dist}
Summary:        _A Cython version of ScanCode-toolkit_s licensedcode.seq_
License:        Apache-2.0
URL:            https://github.com/aboutcode-org/cyseq
Source0:        https://files.pythonhosted.org/packages/source/c/cyseq/cyseq-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 50
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6
Requires:       python3-cyseq = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cyseq
Summary:        _A Cython version of ScanCode-toolkit_s licensedcode.seq_
%description -n python3-cyseq

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cyseq-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cyseq usr/lib/python3*/site-packages/cyseq* usr/lib64/python3*/site-packages/cyseq* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cyseq* usr/lib64/python3*/site-packages/cyseq* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cyseq -f %{oreon_filedir}/python3-cyseq.list

%changelog

%autochangelog
