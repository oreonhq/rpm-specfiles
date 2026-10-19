%global source0_hash 0017591a5477066e90d26b0e696ddc143baafd87b588cfac8100bc6be9634de0
Name:           python-automat
Version:        25.4.16
Release:        1%{?dist}
Summary:        Self-service finite-state machines for the programmer on the go.
License:        MIT
URL:            https://github.com/glyph/automat/
Source0:        https://files.pythonhosted.org/packages/source/a/automat/automat-%{version}.tar.gz
BuildArch:      noarch
Patch:          sphinx-no-git.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 35.0.2
BuildRequires:  python3dist(wheel) >= 0.29.0
Requires:       python3-automat = %{version}-%{release}
# /oreon:deps
%package -n       python3-automat+visualize
Summary:        Metapackage for python3-automat visualize extras
Requires:       python3-automat = %{version}-%{release}
Requires:       python3dist(graphviz) > 0.5.1
Requires:       python3dist(twisted) >= 16.1.1
Provides:       python3dist(automat[visualize]) = %{version}-%{release}

%description -n python3-automat+visualize
Metapackage for python3-automat visualize extras.

%description

%package -n     python3-automat
Summary:        Self-service finite-state machines for the programmer on the go.
%description -n python3-automat

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir automat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-automat usr/lib/python3*/site-packages/automat* usr/lib64/python3*/site-packages/automat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/automat* usr/lib64/python3*/site-packages/automat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-automat -f %{oreon_filedir}/python3-automat.list

%changelog

%autochangelog
