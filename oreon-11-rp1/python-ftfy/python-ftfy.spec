%global source0_hash c3879706cd22ec5666523b65f2a00d0414888f45412bb41dc732d5c7ee4d35d0
%global pypi_name ftfy
%global github_name python-%{pypi_name}
Name:           python-%{pypi_name}
Version:        6.3.1
Release:        1%{?dist}
Summary:        Fixes mojibake and other glitches in Unicode text, after the fact
License:        Apache-2.0
URL:            https://github.com/rspeer/python-ftfy
Source0:        https://github.com/rspeer/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
ftfy fixes mojibake and other glitches in Unicode text, after the fact.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ftfy = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        Fixes mojibake and other glitches in Unicode text, after the fact
%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
License:        Apache-2.0 AND MIT AND BSD-2-Clause
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)
%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{github_name}-%{version}

%build

%pyproject_wheel
sphinx-build-3 -b html docs/ html
rm -rf html/.{doctrees,buildinfo}
%install
%pyproject_install
rm -rfv %{buildroot}%{python3_sitelib}/*.md
%oreon_autofiles main usr/lib/python3*/site-packages/ftfy* usr/lib64/python3*/site-packages/ftfy* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -rfv tests/test_cli.py
%pytest
%files
%files -n python3-ftfy -f %{oreon_filedir}/python3-ftfy.list
%files -n python-ftfy-doc -f %{oreon_filedir}/python-ftfy-doc.list

%changelog

%autochangelog
