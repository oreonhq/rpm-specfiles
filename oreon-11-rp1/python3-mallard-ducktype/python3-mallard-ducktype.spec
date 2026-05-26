%global srcname mallard-ducktype

Name:    python3-mallard-ducktype
Version: 1.0.2
Release: 27%{?dist}
Summary: Parse Ducktype files and convert them to Mallard

License: MIT
URL:     https://pypi.python.org/pypi/%{srcname}
# The PyPI tarball does not have AUTHORS or COPYING.
Source0: https://github.com/projectmallard/%{srcname}/archive/%{version}/%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 73ac416376dd65c737594ab4b1037b0823390239f33672f1ee1e30725dcef4e9
%global source0_file 1.0.2.tar.gz
# oreon url source checksums end

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Parse Ducktype files and convert them to Mallard.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.0.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "73ac416376dd65c737594ab4b1037b0823390239f33672f1ee1e30725dcef4e9" || { echo "oreon: Source0 SHA256 mismatch for 1.0.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
