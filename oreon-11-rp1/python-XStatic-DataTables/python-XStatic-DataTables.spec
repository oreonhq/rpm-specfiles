%global source0_hash 140a77f3043bd69e758c9f7a7f03b32e43aa394865769662871c73ff431375f3
%global pypi_name XStatic-DataTables
Name:           python-%{pypi_name}
Version:        1.10.15.1
Release:        1%{?dist}
Summary:        DataTables jquery javascript framework (XStatic packaging standard)
License:        Apache-2.0
URL:            https://datatables.net/
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  web-assets-devel
# /oreon:deps
%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python3-%{pypi_name}
Summary:        DataTables jquery javascript framework (XStatic packaging standard)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-XStatic
Requires:       xstatic-datatables-common
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%package -n xstatic-datatables-common
Summary:        DataTables jquery javascript framework (XStatic packaging standard)
BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem
%description -n xstatic-datatables-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/datatables'|" xstatic/pkg/datatables/__init__.py

%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_jsdir}/datatables
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/datatables/data/* %{buildroot}%{_jsdir}/datatables
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/datatables/data/
chmod 644 %{buildroot}%{_jsdir}/datatables/js/*.js
%oreon_autofiles xstatic-datatables-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-XStatic-DataTables -f %{oreon_filedir}/python3-XStatic-DataTables.list
%files -n xstatic-datatables-common -f %{oreon_filedir}/xstatic-datatables-common.list

%changelog

%autochangelog
