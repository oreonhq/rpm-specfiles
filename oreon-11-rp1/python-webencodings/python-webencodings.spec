%global srcname webencodings
%global desc This is a Python implementation of the WHATWG Encoding standard.


Name: python-%{srcname}
Version: 0.5.1
Release: 33%{?dist}
BuildArch: noarch

License: BSD-3-Clause
Summary: Character encoding for the web
URL: https://github.com/gsnedders/python-%{srcname}
Source0:        https://github.com/gsnedders/python-webencodings/archive/v0.5.1/webencodings-0.5.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 082367f568a7812aa5f6922ffe3d9d027cd83829dc32bcaac4c874eeed618000
%global source0_file webencodings-0.5.1.tar.gz
# oreon url source checksums end

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-sphinx


%description
%{desc}


%package doc
Summary: Documentation for python-webencodings


%description doc
Documentation for python-webencodings.


%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3


%description -n python3-%{srcname}
%{desc}


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/webencodings-0.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "082367f568a7812aa5f6922ffe3d9d027cd83829dc32bcaac4c874eeed618000" || { echo "oreon: Source0 SHA256 mismatch for webencodings-0.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n python-%{srcname}-%{version}


%build
%py3_build

PYTHONPATH=. sphinx-build-3 docs docs/_build

# Remove unneeded build artifacts.
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/.doctrees


%install
%py3_install


%check
py.test-3


%files doc
%license LICENSE
%doc docs/_build


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-33
- Prepare for Oreon 11 (RP1)
