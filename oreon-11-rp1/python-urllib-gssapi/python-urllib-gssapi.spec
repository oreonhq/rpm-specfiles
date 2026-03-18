%global sname urllib-gssapi
%global s_name urllib_gssapi

Name:           python-%{sname}
Version:        1.0.2
Release:        20%{?dist}
Summary:        A GSSAPI/SPNEGO authentication handler for urllib/urllib2

License:        Apache-2.0
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{s_name}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  git-core

BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-setuptools

%global _description\
urllib_gssapi is a backend for urllib.  It provides GSSAPI/SPNEGO\
authentication to HTTP servers.  urllib_gssapi replaces urllib_kerberos and\
behaves in the same ways.

%description %_description

%package -n python3-%{sname}
Summary:        %summary
Requires:       python3-gssapi
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description

%prep
%autosetup -S git -n %{s_name}-%{version}

%build
%py3_build


%install
%py3_install

%check
%py3_check_import %{s_name}

%files -n python3-%{sname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{s_name}*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-20
- Prepare for Oreon 11 (RP1)
