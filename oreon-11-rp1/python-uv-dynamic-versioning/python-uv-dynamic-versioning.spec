%global source0_hash 8642db686ce5c50417035e7a257ac73b7e5c3a7a32c33e45bd7e36ba22eeb648
Name:           python-uv-dynamic-versioning
Version:        0.14.1
Release:        1%{?dist}
Summary:        Dynamic versioning based on VCS tags for uv/hatch project
License:        ...
URL:            https://github.com/ninoseki/uv-dynamic-versioning/
Source0:        https://files.pythonhosted.org/packages/source/u/uv_dynamic_versioning/uv_dynamic_versioning-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-uv-dynamic-versioning = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-uv-dynamic-versioning
Summary:        Dynamic versioning based on VCS tags for uv/hatch project
%description -n python3-uv-dynamic-versioning

%prep
%global oreon_srcdir uv_dynamic_versioning-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uv-dynamic-versioning usr/lib/python3*/site-packages/uv_dynamic_versioning* usr/lib64/python3*/site-packages/uv_dynamic_versioning* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uv_dynamic_versioning* usr/lib64/python3*/site-packages/uv_dynamic_versioning* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-uv-dynamic-versioning -f %{oreon_filedir}/python3-uv-dynamic-versioning.list

%changelog

%autochangelog
