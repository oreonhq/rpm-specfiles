%global srcname mallard-ducktype

Name:    python3-mallard-ducktype
Version: 1.0.2
Release: 27%{?dist}
Summary: Parse Ducktype files and convert them to Mallard

License: MIT
URL:     https://pypi.python.org/pypi/%{srcname}
# The PyPI tarball does not have AUTHORS or COPYING.
Source0: https://github.com/projectmallard/%{srcname}/archive/%{version}/%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Parse Ducktype files and convert them to Mallard.


%prep
%setup -q -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
pushd tests
%{py3_test_envvars} ./runtests
popd


%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ducktype
%{python3_sitelib}/*



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-27
- Prepare for Oreon 11 (RP1)
