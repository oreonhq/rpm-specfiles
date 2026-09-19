%global source0_hash 93d1b995ad7ce21e62db649f361048125dd6022563a0ae8a23909465f1fd25b7

%global srcname authres

Name:           python-%{srcname}
Version:        1.2.0
Release:        28%{?dist}
Summary:        Authentication Results Header Module
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://launchpad.net/authentication-results-python
Source0:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz.asc
Source2:	https://db.debian.org/fetchkey.cgi?fingerprint=E7729BFFBE85400FEEEE23B178D7DEFB9AD59AF1#/GPG-KEY-kitterman
BuildArch:      noarch
BuildRequires:	gnupg2

%global _description\
RFC 8601 Authentication-Results Headers generation and parsing for\
Python/Python3.  See README for extension RFCs implemented.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
BuildRequires: python3-devel python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} -m authres

%files -n python3-%{srcname}
%license COPYING
%doc CHANGES README
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
%autochangelog
