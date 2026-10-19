%global source0_hash 0ba244eb65a4c9db180b3223458acc9cce425ae5931ae4ccaad5a2cb351094aa
Name:           python-precis_i18n
Version:        1.1.2
Release:        2%{?dist}
Summary:        Python library for internationalized usernames and passwords
License:        MIT
URL:            https://github.com/byllyfish/precis_i18n
Source0:        https://github.com/byllyfish/precis_i18n/archive/v%{version}.tar.gz#/precis_i18n-%{version}.tar.gz
BuildArch:      noarch
%global desc %{expand:
If you want your application to accept Unicode user names and passwords, you
must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform Unicode strings into a canonical form, suitable for
comparison.
This Python module implements the PRECIS Framework as described in:
  PRECIS Framework: Preparation, Enforcement, and Comparison of
  Internationalized Strings in Application Protocols (RFC 8264)
  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)
  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-precis_i18n = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-precis_i18n
Summary:        Python library for internationalized usernames and passwords
%description -n python3-precis_i18n
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir precis_i18n-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-precis_i18n usr/lib/python3*/site-packages/precis_i18n* usr/lib64/python3*/site-packages/precis_i18n* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/precis_i18n* usr/lib64/python3*/site-packages/precis_i18n* usr/bin/*

%check

%pytest
%files
%files -n python3-precis_i18n -f %{oreon_filedir}/python3-precis_i18n.list

%changelog

%autochangelog
