%global source0_hash 499a0e399e353e0fb4a74e105ea2ad2aed89a15053a299f5fa93c027d721743a
Name:           python-metakernel
Version:        1.0.7
Release:        1%{?dist}
Summary:        A Jupyter/IPython Kernel base class in Python
License:        BSD-3-Clause
URL:            https://github.com/Calysto/metakernel
Source0:        https://files.pythonhosted.org/packages/source/m/metakernel/metakernel-%{version}.tar.gz
BuildArch:      noarch
Patch0:		0001-Clear-PS0-in-bash-REPL-wrapper.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0.0
Requires:       python3-metakernel = %{version}-%{release}
# /oreon:deps
%package -n       python3-metakernel+activity
Summary:        Metapackage for python3-metakernel activity extras
Requires:       python3-metakernel = %{version}-%{release}
Requires:       python3dist(portalocker) >= 2.8.0
Provides:       python3dist(metakernel[activity]) = %{version}-%{release}

%description -n python3-metakernel+activity
Metapackage for python3-metakernel activity extras.

%package -n       python3-metakernel+parallel
Summary:        Metapackage for python3-metakernel parallel extras
Requires:       python3-metakernel = %{version}-%{release}
Requires:       python3dist(ipyparallel) >= 8.5.1
Provides:       python3dist(metakernel[parallel]) = %{version}-%{release}

%description -n python3-metakernel+parallel
Metapackage for python3-metakernel parallel extras.

%description

%package -n     python3-metakernel
Summary:        A Jupyter/IPython Kernel base class in Python
# oreon:reqs
Requires:       python3dist(comm) >= 0.1.3
Requires:       python3dist(ipykernel) >= 6.22.0
Requires:       python3dist(jedi) >= 0.19.0
Requires:       python3dist(jupyter-core) >= 5.3.1
Requires:       python3dist(pexpect) >= 4.9.0
# /oreon:reqs
%description -n python3-metakernel

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir metakernel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-metakernel usr/lib/python3*/site-packages/metakernel* usr/lib64/python3*/site-packages/metakernel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/metakernel* usr/lib64/python3*/site-packages/metakernel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-metakernel -f %{oreon_filedir}/python3-metakernel.list

%changelog

%autochangelog
