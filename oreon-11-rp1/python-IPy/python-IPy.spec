%global source0_hash edeca741dea2d54aca568fa23740288c3fe86c0f3ea700344571e9ef14a7cc1a

%define oname IPy
Summary:        Python module for handling IPv4 and IPv6 Addresses and Networks
Name:           python-%{oname}
Version:        1.01
Release:        19%{?dist}
URL:            https://github.com/haypo/python-ipy
Source0:        https://files.pythonhosted.org/packages/source/I/IPy/IPy-%{version}.tar.gz
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%package -n python3-%{oname}
Summary: Python 3 module for handling IPv4 and IPv6 Addresses and Networks
%{?python_provide:%python_provide python3-%{oname}}

%description -n python3-%{oname}
IPy is a Python 3 module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{oname}-%{version} -p1

%build
%py3_build

%check
PYTHONPATH=$PWD %{__python3} test/test_IPy.py
#PYTHONPATH=$PWD %{__python3} test_doc.py  # FAILS

%install
%py3_install

%files -n python3-%{oname}
%license COPYING
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/%{oname}*
%{python3_sitelib}/__pycache__/%{oname}*

%changelog
%autochangelog
