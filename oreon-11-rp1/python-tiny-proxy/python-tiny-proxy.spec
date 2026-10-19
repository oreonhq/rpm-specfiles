%global source0_hash e664e8969f8766dde1650c5cfa0070d87b487fc6c928561ea32e45ddcc1dc2b5
Name:           python-tiny-proxy
Version:        0.3.0
Release:        1%{?dist}
Summary:        Simple proxy server _SOCKS4_a_, SOCKS5_h_, HTTP CONNECT_
License:        Apache-2.0
URL:            https://github.com/romis2012/tiny-proxy
Source0:        https://files.pythonhosted.org/packages/source/t/tiny_proxy/tiny_proxy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tiny-proxy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tiny-proxy
Summary:        Simple proxy server _SOCKS4_a_, SOCKS5_h_, HTTP CONNECT_
# oreon:reqs
Requires:       python3dist(anyio) < 5.0.0
Requires:       python3dist(anyio) >= 3.6.1
# /oreon:reqs
%description -n python3-tiny-proxy

%prep
%global oreon_srcdir tiny_proxy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tiny-proxy usr/lib/python3*/site-packages/tiny_proxy* usr/lib64/python3*/site-packages/tiny_proxy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tiny_proxy* usr/lib64/python3*/site-packages/tiny_proxy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tiny-proxy -f %{oreon_filedir}/python3-tiny-proxy.list

%changelog

%autochangelog
