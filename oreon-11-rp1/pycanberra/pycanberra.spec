%global source0_hash d5ad9eb6bbc9c2a3ae2ded11986ec9e7972529aac16d917abb0fbd53afc0d184
%global commit 88c53cd44a626ede3b07dab0b548f8bcfda42867
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:          pycanberra
Summary:        A very basic (and incomplete) wrapper for libcanberra
URL:           https://github.com/psykoyiko/pycanberra/
License:       LicenseRef-Callaway-LGPLv2
Version:       0
Release:        1%{?dist}
Source0:        https://github.com/psykoyiko/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:     noarch
Requires:      libcanberra
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
A very basic (and incomplete) wrapper of libcanberra for Python 2.

%package -n python3-canberra
Summary:       A very basic (and incomplete) wrapper for libcanberra
%description -n python3-canberra
A very basic (and incomplete) wrapper of libcanberra for Python 3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pycanberra-%{commit}

%build

%install
install -D -p -m 0644 pycanberra.py -t %{buildroot}%{python3_sitelib}/
%oreon_autofiles python3-canberra usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-canberra -f %{oreon_filedir}/python3-canberra.list

%changelog

%autochangelog
