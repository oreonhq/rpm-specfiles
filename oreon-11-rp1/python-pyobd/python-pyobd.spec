%global source0_hash 99b957c3fb05728c4cb542fd1f2168b69160a4179df8423a8c791684b4869df8
Name:           python-pyobd
Version:        0.3.0
Release:        1%{?dist}
Summary:        BYMA Market Data Library - Open Data API client
License:        ...
URL:            https://github.com/franco-lamas/PyOBD
Source0:        https://files.pythonhosted.org/packages/source/p/pyobd/pyobd-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-pyobd-0.9.3-pyobd-module.patch
Patch1:         python-pyobd-0.9.3-invalid-device-traceback-fix.patch
Patch2:         python-pyobd-0.9.3-configure-dialog-traceback-fix.patch
Patch3:         python-pyobd-0.9.3-python3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyobd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyobd
Summary:        BYMA Market Data Library - Open Data API client
%description -n python3-pyobd

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyobd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyobd usr/lib/python3*/site-packages/pyobd* usr/lib64/python3*/site-packages/pyobd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyobd* usr/lib64/python3*/site-packages/pyobd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyobd -f %{oreon_filedir}/python3-pyobd.list

%changelog

%autochangelog
