%global source0_hash b21eb21a53557d197899e1bf3d8b7f4f264feb1c546327106fdfcc967cb3a704
Name:           python-pbs-installer
Version:        2026.9.1
Release:        1%{?dist}
Summary:        Installer for Python Build Standalone
License:        MIT
URL:            https://github.com/frostming/pbs-installer
Source0:        https://files.pythonhosted.org/packages/source/p/pbs_installer/pbs_installer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pbs-installer = %{version}-%{release}
# /oreon:deps
%package -n       python3-pbs-installer+download
Summary:        Metapackage for python3-pbs-installer download extras
Requires:       python3-pbs-installer = %{version}-%{release}
Requires:       python3dist(httpx) < 1
Requires:       python3dist(httpx) >= 0.27.0
Provides:       python3dist(pbs-installer[download]) = %{version}-%{release}

%description -n python3-pbs-installer+download
Metapackage for python3-pbs-installer download extras.

%package -n       python3-pbs-installer+install
Summary:        Metapackage for python3-pbs-installer install extras
Requires:       python3-pbs-installer = %{version}-%{release}
Requires:       python3dist(backports.zstd) >= 1.0.0
Provides:       python3dist(pbs-installer[install]) = %{version}-%{release}

%description -n python3-pbs-installer+install
Metapackage for python3-pbs-installer install extras.

%package -n       python3-pbs-installer+all
Summary:        Metapackage for python3-pbs-installer all extras
Requires:       python3-pbs-installer = %{version}-%{release}
Provides:       python3dist(pbs-installer[all]) = %{version}-%{release}

%description -n python3-pbs-installer+all
Metapackage for python3-pbs-installer all extras.

%description

%package -n     python3-pbs-installer
Summary:        Installer for Python Build Standalone
%description -n python3-pbs-installer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pbs_installer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pbs-installer usr/lib/python3*/site-packages/pbs_installer* usr/lib64/python3*/site-packages/pbs_installer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pbs_installer* usr/lib64/python3*/site-packages/pbs_installer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pbs-installer -f %{oreon_filedir}/python3-pbs-installer.list

%changelog

%autochangelog
