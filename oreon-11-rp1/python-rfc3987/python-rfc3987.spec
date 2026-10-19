%global source0_hash d3c4d257a560d544e9826b38bc81db676890c79ab9d7ac92b39c7a253d5ca733
Name:           python-rfc3987
Version:        1.3.8
Release:        1%{?dist}
Summary:        Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
License:        GPL-3.0-or-later
URL:            https://codeberg.org/atufi/rfc3987
Source0:        https://files.pythonhosted.org/packages/source/r/rfc3987/rfc3987-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rfc3987 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rfc3987
Summary:        Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
%description -n python3-rfc3987

%install
%pyproject_install
sed -r -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/rfc3987.py
%oreon_autofiles python3-rfc3987 usr/lib/python3*/site-packages/rfc3987* usr/lib64/python3*/site-packages/rfc3987* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rfc3987* usr/lib64/python3*/site-packages/rfc3987* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%{py3_test_envvars} %{python3} -m doctest -v rfc3987.py
%files
%files -n python3-rfc3987 -f %{oreon_filedir}/python3-rfc3987.list

%changelog

%autochangelog
