%global source0_hash eb42e2d9674e470935d98474b8502e675894cc8489362d8419fdd957319f2b3e
Name:           python-pykmip
Version:        0.11.0
Release:        1%{?dist}
Summary:        KMIP library
License:        ...
URL:            https://github.com/OpenKMIP/PyKMIP
Source0:        https://files.pythonhosted.org/packages/source/p/pykmip/pykmip-%{version}.tar.gz
BuildArch:      noarch
Patch0:         enum34.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pykmip = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pykmip
Summary:        KMIP library
%description -n python3-pykmip

%prep
%global oreon_srcdir pykmip-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pykmip usr/lib/python3*/site-packages/pykmip* usr/lib64/python3*/site-packages/pykmip* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pykmip* usr/lib64/python3*/site-packages/pykmip* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pykmip -f %{oreon_filedir}/python3-pykmip.list

%changelog

%autochangelog
