%global source0_hash 72f3fe8fce36b70d4a5b612f899090cd0401deddc4ea90e1572b9f4bfb058c79
Name:           python-matplotlib-inline
Version:        0.2.2
Release:        1%{?dist}
Summary:        Inline Matplotlib backend for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/matplotlib-inline
Source0:        https://files.pythonhosted.org/packages/source/m/matplotlib_inline/matplotlib_inline-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-matplotlib-inline = %{version}-%{release}
# /oreon:deps
%package -n       python3-matplotlib-inline+test
Summary:        Metapackage for python3-matplotlib-inline test extras
Requires:       python3-matplotlib-inline = %{version}-%{release}
Provides:       python3dist(matplotlib-inline[test]) = %{version}-%{release}

%description -n python3-matplotlib-inline+test
Metapackage for python3-matplotlib-inline test extras.

%description

%package -n     python3-matplotlib-inline
Summary:        Inline Matplotlib backend for Jupyter
%description -n python3-matplotlib-inline

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir matplotlib_inline-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-matplotlib-inline usr/lib/python3*/site-packages/matplotlib_inline* usr/lib64/python3*/site-packages/matplotlib_inline* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/matplotlib_inline* usr/lib64/python3*/site-packages/matplotlib_inline* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-matplotlib-inline -f %{oreon_filedir}/python3-matplotlib-inline.list

%changelog

%autochangelog
