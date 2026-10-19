%global source2_hash c476b73f0060944131cd9d31c83a4d6c8173b7097c69c763d67bfe5b650b6b79
%global source1_hash 65d05553add7197354cd74400a30ee0856d85a5e8a344c22be1624265c4e1eab
%global source0_hash 93d1b995ad7ce21e62db649f361048125dd6022563a0ae8a23909465f1fd25b7
%global srcname authres
Name:           python-%{srcname}
Version:        1.2.0
Release:        28%{?dist}
Summary:        Authentication Results Header Module
License:        Apache-2.0
URL:            https://launchpad.net/authentication-results-python
Source0:        https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz.asc
Source2:	https://db.debian.org/fetchkey.cgi?fingerprint=E7729BFFBE85400FEEEE23B178D7DEFB9AD59AF1#/GPG-KEY-kitterman
BuildArch:      noarch
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary: %summary
BuildRequires: python3-devel python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{python3} -m authres
%files -f %{oreon_filedir}/main.list
%files -n python3-authres -f %{oreon_filedir}/python3-authres.list

%changelog

%autochangelog
