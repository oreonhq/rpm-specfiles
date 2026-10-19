%global source0_hash b81367d0d1d6b742a7d0a7f8403acb246a57cd7b9bf934d825cf1cdf67cef284
Name:           python-whois
Version:        1.20240129.2
Release:        1%{?dist}
Summary:        Python package for retrieving WHOIS information of domains.
License:        MIT
URL:            https://github.com/mboot-github/WhoisDomain/
Source0:        https://files.pythonhosted.org/packages/source/w/whois/whois-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-whois = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-whois
Summary:        Python package for retrieving WHOIS information of domains.
%description -n python3-whois

%prep
%global oreon_srcdir whois-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-whois usr/lib/python3*/site-packages/whois* usr/lib64/python3*/site-packages/whois* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/whois* usr/lib64/python3*/site-packages/whois* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-whois -f %{oreon_filedir}/python3-whois.list

%changelog

%autochangelog
