%global source0_hash 34fb47193b15390fbee1cd49c1cb560d4928d8154c0f03bd67620cd8e9554f52

%{?python_enable_dependency_generator}

%global modname fauxquests

# TODO: commit is actually release, but has not been pushed as git tag
# https://github.com/lukesneeringer/fauxquests/issues/1
%global commit 16d1f71547279fc7862c4b6597fab5524f70b082

Name:           python-%{modname}
Version:        1.1
Release:        36%{?dist}
Summary:        Mock HTTP requests sent with the requests package

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/lukesneeringer/fauxquests
Source0:        %{url}/archive/%{commit}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-requests
BuildRequires:  python3-dict-sorted

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{commit}

%build
%py3_build

%install
%py3_install

%check
# https://github.com/lukesneeringer/fauxquests/issues/3
%{__python3} tests/runtests.py -v || :

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
%autochangelog
