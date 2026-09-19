%global source0_hash ea029d6bcfc69c245fbebe6b4115fc513e6369e740ccce2fcb72829015b1b029

Name:           python-openid-cla
Version:        1.2
Release:        37%{?dist}
Summary:        CLA extension for python-openid

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/puiterwijk/python-openid-cla
Source:         https://github.com/puiterwijk/python-openid-cla/releases/download/v%{version}/python-openid-cla-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-openid

%global _description\
CLA extension implementation for python-openid

%description %_description

%package -n python3-openid-cla
Summary:        OpenID support for Flask
Requires:       python3-openid

%description -n python3-openid-cla
CLA extension implementation for python-openid

This package includes the python 3 version of the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

 
%files -n python3-openid-cla
# TODO: Upstream error: no COPYING in latest release
#%doc COPYING
%{python3_sitelib}/openid_cla/
%{python3_sitelib}/python_openid_cla*/

%changelog
%autochangelog
