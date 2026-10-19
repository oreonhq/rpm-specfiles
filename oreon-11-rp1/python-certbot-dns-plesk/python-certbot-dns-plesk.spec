%global source0_hash 172cf8f9e29f6c5fb292d58d7120647c85fa5eacd7ad461ca9ee15d403d70777
Name:           python-certbot-dns-plesk
Version:        0.4.1
Release:        1%{?dist}
Summary:        plesk DNS Authenticator plugin for Certbot
License:        GPL-3.0-or-later
URL:            https://gitlab.com/spike77453/certbot-dns-plesk
Source0:        https://files.pythonhosted.org/packages/source/c/certbot_dns_plesk/certbot_dns_plesk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-certbot-dns-plesk = %{version}-%{release}
# /oreon:deps
%package -n       python3-certbot-dns-plesk+test
Summary:        Metapackage for python3-certbot-dns-plesk test extras
Requires:       python3-certbot-dns-plesk = %{version}-%{release}
Provides:       python3dist(certbot-dns-plesk[test]) = %{version}-%{release}

%description -n python3-certbot-dns-plesk+test
Metapackage for python3-certbot-dns-plesk test extras.

%description

%package -n     python3-certbot-dns-plesk
Summary:        plesk DNS Authenticator plugin for Certbot
# oreon:reqs
Requires:       python3dist(certbot) >= 2.7.0
Requires:       python3dist(dns-lexicon) >= 3.2.4
# /oreon:reqs
%description -n python3-certbot-dns-plesk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir certbot_dns_plesk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-certbot-dns-plesk usr/lib/python3*/site-packages/certbot_dns_plesk* usr/lib64/python3*/site-packages/certbot_dns_plesk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/certbot_dns_plesk* usr/lib64/python3*/site-packages/certbot_dns_plesk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-certbot-dns-plesk -f %{oreon_filedir}/python3-certbot-dns-plesk.list

%changelog

%autochangelog
