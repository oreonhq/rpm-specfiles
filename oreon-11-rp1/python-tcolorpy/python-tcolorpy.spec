%global source0_hash 0fbf6bf238890bbc2e32662aa25736769a29bf6d880328f310c910a327632614
Name:           python-tcolorpy
Version:        0.1.7
Release:        1%{?dist}
Summary:        tcolopy is a Python library to apply true color for terminal text.
License:        MIT
URL:            https://github.com/thombashi/tcolorpy
Source0:        https://files.pythonhosted.org/packages/source/t/tcolorpy/tcolorpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-tcolorpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tcolorpy
Summary:        tcolopy is a Python library to apply true color for terminal text.
%description -n python3-tcolorpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tcolorpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tcolorpy usr/lib/python3*/site-packages/tcolorpy* usr/lib64/python3*/site-packages/tcolorpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tcolorpy* usr/lib64/python3*/site-packages/tcolorpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tcolorpy -f %{oreon_filedir}/python3-tcolorpy.list

%changelog

%autochangelog
