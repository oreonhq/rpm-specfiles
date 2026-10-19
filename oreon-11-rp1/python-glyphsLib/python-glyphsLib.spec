%global source0_hash 275bda269a5868c9d7ab0ab098892fee2b68dc087443dbc58e409ad1e2218f2a
Name:           python-glyphslib
Version:        6.14.0
Release:        1%{?dist}
Summary:        A bridge from Glyphs source files _.glyphs_ to UFOs
License:        ...
URL:            https://github.com/googlefonts/glyphsLib
Source0:        https://files.pythonhosted.org/packages/source/g/glyphslib/glyphslib-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/1073.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.0
Requires:       python3-glyphslib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-glyphslib
Summary:        A bridge from Glyphs source files _.glyphs_ to UFOs
%description -n python3-glyphslib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir glyphslib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-glyphslib usr/lib/python3*/site-packages/glyphslib* usr/lib64/python3*/site-packages/glyphslib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/glyphslib* usr/lib64/python3*/site-packages/glyphslib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-glyphslib -f %{oreon_filedir}/python3-glyphslib.list

%changelog

%autochangelog
