%global source0_hash 346b6642e0dbdde3b4ff5a930b664ca82abfa116356ed48cc42c7d6590d36f63

%global srcname pyotp

Name:           python-%{srcname}
Version:        2.9.0
Release:        %autorelease
Summary:        Python One Time Password library
BuildArch:      noarch

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/pyotp
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
PyOTP is a Python library for generating and verifying one-time passwords. It
can be used to implement two-factor (2FA) or multi-factor (MFA) authentication
methods in web applications and in other systems that require users to log in.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
PyOTP is a Python library for generating and verifying one-time passwords. It
can be used to implement two-factor (2FA) or multi-factor (MFA) authentication
methods in web applications and in other systems that require users to log in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%check
%{__python3} test.py

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
