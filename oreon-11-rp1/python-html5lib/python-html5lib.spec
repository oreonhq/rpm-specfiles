Name:           python-html5lib
Summary:        A python based HTML parser/tokenizer
Version:        1.1
Release:        %autorelease
Epoch:          1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source:         %{pypi_source html5lib}

# Fix compatibility with pytest 6
Patch:        https://github.com/html5lib/html5lib-python/pull/506.patch
# Fix compatibility with pytest 7.4.0
Patch:        https://github.com/html5lib/html5lib-python/pull/573.patch
# Fix compatibility with Python 3.14+
Patch:        https://github.com/html5lib/html5lib-python/pull/583.patch
# Avoid ResourceWarning: Implicitly cleaning up <addinfourl ...>
Patch:        https://github.com/html5lib/html5lib-python/pull/591.patch
# oreon url source checksums begin
%global source0_sha256 b2e5b40261e20f354d198eae92afc10d750afb487ed5e50f9c4eaf07c184146f
%global source0_file html5lib-1.1.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python3-devel

# Test deps
# Upstream uses requirements-test.txt but it has tox, coverage, mock, flake8 in it
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-expect)

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.


%package -n python3-html5lib
Summary:        %{summary}

%description -n python3-html5lib
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%pyproject_extras_subpkg -n python3-html5lib lxml genshi chardet all


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/html5lib-1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b2e5b40261e20f354d198eae92afc10d750afb487ed5e50f9c4eaf07c184146f" || { echo "oreon: Source0 SHA256 mismatch for html5lib-1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n html5lib-%{version}

# Use standard library unittest.mock instead of 3rd party mock
# From https://github.com/html5lib/html5lib-python/pull/536
sed -i 's/from mock import/from unittest.mock import/' html5lib/tests/test_meta.py


%generate_buildrequires
%pyproject_buildrequires -x all

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files html5lib


%check
%pytest


%files -n python3-html5lib -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-1
- Prepare for Oreon 11 (RP1)
