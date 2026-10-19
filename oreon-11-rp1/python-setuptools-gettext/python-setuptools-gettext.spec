%global source0_hash c92b0ae486def502686cd944f16559819e42f8dc0b9d683cf62e7415397f2b35
Name:           python-setuptools-gettext
Version:        0.1.18
Release:        1%{?dist}
Summary:        Setuptools gettext extension plugin
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Source0:        https://files.pythonhosted.org/packages/source/s/setuptools_gettext/setuptools_gettext-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-setuptools-gettext = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-setuptools-gettext
Summary:        Setuptools gettext extension plugin
%description -n python3-setuptools-gettext

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir setuptools_gettext-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-setuptools-gettext usr/lib/python3*/site-packages/setuptools_gettext* usr/lib64/python3*/site-packages/setuptools_gettext* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/setuptools_gettext* usr/lib64/python3*/site-packages/setuptools_gettext* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-setuptools-gettext -f %{oreon_filedir}/python3-setuptools-gettext.list

%changelog

%autochangelog
