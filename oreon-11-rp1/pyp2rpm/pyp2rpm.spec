%global source0_hash 032abacf9901eb648964d4eb9ba3b23f3439e8d4bef1e4a6af687b4182d26a50

Name:           pyp2rpm
Version:        3.3.10
Release:        %autorelease
Summary:        Convert Python packages to RPM SPECFILES

License:        MIT
URL:            https://pypi.python.org/pypi/pyp2rpm
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

# Replace pytest-runner with pytest for testing pyp2rpm
# https://github.com/fedora-python/pyp2rpm/pull/300
#
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
#
# This version of the patch does not include changes to tox.ini, which is not
# present in the PyPI sdist.
Patch:          0001-Replace-pytest-runner-with-pytest-for-testing-pyp2rp.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(virtualenv-api)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(click)

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flexmock) >= 0.9.3
BuildRequires:  python3dist(scripttest)
 
Requires:       python3dist(jinja2)
Requires:       python3dist(setuptools)
Requires:       python3dist(click)
Requires:       python3dist(virtualenv-api)
Requires:       python3-rpm
Requires:       rpmdevtools

# For Python 2 metadata extractor
Suggests:       python2dist(setuptools)

%description
Convert Python packages to RPM SPECFILES. The packages can be downloaded from
PyPI and the produced SPEC is in line with Fedora 201x-era Python Packaging
Guidelines or Mageia Python Policy.

Unfortunately, pyp2rpm does not generate spec files according to to the current
Fedora Python Packaging Guidelines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
# TestMetadataExtractor requires Python 2 setuptools
PYTHONPATH="." py.test-3 -vv -m "not webtest" -k "not TestMetadataExtractor"

%files
%license LICENSE
%doc README.md
%{_bindir}/pyp2rpm
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info

%changelog
%autochangelog
