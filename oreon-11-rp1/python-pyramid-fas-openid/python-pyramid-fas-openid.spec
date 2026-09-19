%global source0_hash a2c3ebb8e2370ea6b830abce3de8b9416248dc7d3006e9b9867fa0a5cb57889a

%global modname pyramid_fas_openid
%global _description\
pyramid_fas_openid provides a view for the Pyramid framework that acts as\
an OpenID consumer for the Fedora Account System.

Name:               python-pyramid-fas-openid
Version:            0.4.0
Release:            22%{?dist}
Summary:            A view for pyramid that functions as an OpenID consumer for FAS

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                https://github.com/fedora-infra/pyramid_fas_openid
Source0:            %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-openid
BuildRequires:      python3-openid-cla
BuildRequires:      python3-openid-teams
BuildRequires:      python3-pyramid
BuildRequires:      python3-setuptools

%description %_description

%package -n python3-pyramid-fas-openid
Summary: %summary
Requires:           python3-pyramid
Requires:           python3-openid
Requires:           python3-openid-teams
Requires:           python3-openid-cla
%{?python_provide:%python_provide python3-pyramid-fas-openid}

%description -n python3-pyramid-fas-openid %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-pyramid-fas-openid
%doc README.txt
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
