%global source0_hash 429c6e8aa6916d5bad5c8a5eac50f3ea53c9ac22616f6cb21b18dcc71517d0d3
Name:           python-cloudscraper
Version:        1.2.71
Release:        1%{?dist}
Summary:        A Python module to bypass Cloudflare_s anti-bot page.
License:        MIT
URL:            https://github.com/venomous/cloudscraper
Source0:        https://files.pythonhosted.org/packages/source/c/cloudscraper/cloudscraper-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cloudscraper = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cloudscraper
Summary:        A Python module to bypass Cloudflare_s anti-bot page.
%description -n python3-cloudscraper

%prep
%global oreon_srcdir cloudscraper-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cloudscraper usr/lib/python3*/site-packages/cloudscraper* usr/lib64/python3*/site-packages/cloudscraper* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cloudscraper* usr/lib64/python3*/site-packages/cloudscraper* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cloudscraper -f %{oreon_filedir}/python3-cloudscraper.list

%changelog

%autochangelog
