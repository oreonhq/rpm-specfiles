%global source0_hash 73ac416376dd65c737594ab4b1037b0823390239f33672f1ee1e30725dcef4e9

%global srcname mallard-ducktype

Name:    python3-mallard-ducktype
Version: 1.0.2
Release: 27%{?dist}
Summary: Parse Ducktype files and convert them to Mallard

License: MIT
URL:     https://pypi.python.org/pypi/%{srcname}
# The PyPI tarball does not have AUTHORS or COPYING.
Source0:        https://github.com/projectmallard/mallard-ducktype/archive/1.0.2/1.0.2.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Parse Ducktype files and convert them to Mallard.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
