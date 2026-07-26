%global source0_hash 85b0db113625314f0f44f3fe6ef0eb2564d6c34dd2ee5677b495d15142bb4973

Name:           python-genshi
Version:        0.7.10
Release:        2%{?dist}
Summary:        Toolkit for stream-based generation of output for the web

License:        BSD-3-Clause
URL:            https://genshi.edgewall.org/

Source0:        %{pypi_source genshi}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web. The major feature is
a template language, which is heavily inspired by Kid.

%package -n python3-genshi
Summary:        %{summary}

%description -n python3-genshi
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web. The major feature is
a template language, which is heavily inspired by Kid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n genshi-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

find examples -type f | xargs chmod a-x

%generate_buildrequires
%pyproject_buildrequires -x i18n

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files genshi

sed -i -e '/\/tests/d' %{pyproject_files}
sed -i -e '/_speedups.c/d' %{pyproject_files}

%check
%pytest

%files -n python3-genshi -f %{pyproject_files}
%{python3_sitearch}/genshi/_speedups.*.so
%exclude %{python3_sitearch}/genshi/{_speedups.c,tests}
%exclude %{python3_sitearch}/genshi/{filters,template}/tests
# COPYING file already listed in {pyproject_files}
%doc ChangeLog doc examples README.md

%changelog
%autochangelog
