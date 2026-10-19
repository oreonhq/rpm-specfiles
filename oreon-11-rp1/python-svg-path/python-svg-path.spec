%global source0_hash 1cd254c974dc96cbee3a0cfc6528356866356b712f241b4e9066043ab8703d9b
Name:           python-svg-path
Version:        7.1
Release:        1%{?dist}
Summary:        SVG path objects and parser
License:        MIT
URL:            https://github.com/regebro/svg.path
Source0:        https://files.pythonhosted.org/packages/source/s/svg_path/svg_path-%{version}.tar.gz
BuildArch:      noarch
Patch0:             https://patch-diff.githubusercontent.com/raw/regebro/svg.path/pull/105.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-svg-path = %{version}-%{release}
# /oreon:deps
%package -n       python3-svg-path+test
Summary:        Metapackage for python3-svg-path test extras
Requires:       python3-svg-path = %{version}-%{release}
Provides:       python3dist(svg-path[test]) = %{version}-%{release}

%description -n python3-svg-path+test
Metapackage for python3-svg-path test extras.

%description

%package -n     python3-svg-path
Summary:        SVG path objects and parser
%description -n python3-svg-path

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir svg_path-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-svg-path usr/lib/python3*/site-packages/svg_path* usr/lib64/python3*/site-packages/svg_path* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/svg_path* usr/lib64/python3*/site-packages/svg_path* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-svg-path -f %{oreon_filedir}/python3-svg-path.list

%changelog

%autochangelog
