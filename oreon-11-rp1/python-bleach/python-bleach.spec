%global source0_hash 4202482733d85cedd04e59fcb2f89f4e4c7c385a78d3c3c23c30446843a37452

%global modname bleach

Name:           python-%{modname}
Version:        6.4.0
Release:        1%{?dist}
Summary:        An easy whitelist-based HTML-sanitizing tool

License:        Apache-2.0
URL:            https://github.com/mozilla/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz

# As a result of fixed CVE-2023-24329, urllib.parse.urlsplit() now strips
# the leading C0 control and space characters.
# This breaks tests which expect those leading whitespace characters.
# Upstream vendors an ancient parse.py from Python 3.6.14 and doesn't
# experience this issue.
# Discussed upstream: https://github.com/mozilla/bleach/issues/707
Patch:          Strip-leading-whitespaces-from-expected-values.patch

BuildArch:      noarch

%global _description \
Bleach is an HTML sanitizing library that escapes or strips markup and\
attributes based on a white list.

%description %{_description}

%package -n python3-%{modname}
Summary:        An easy whitelist-based HTML-sanitizing tool
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-html5lib
Requires:       python3-html5lib

%description -n python3-%{modname}
%{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

# Remove pregenerated egg-info
rm -rf bleach.egg-info

# Remove vendored libraries which were added for https://github.com/mozilla/bleach/issues/386
rm -r bleach/_vendor/
# Bleach has a shim layer that references the vendored html5lib and urllib.parse we just deleted.
# Let's patch up the imports to use the real html5lib and urllib.parse.
sed -i "s/bleach._vendor.html5lib/html5lib/g" bleach/html5lib_shim.py tests/test_clean.py
sed -i "s/bleach._vendor.parse/urllib.parse/g" bleach/parse_shim.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
! find %{buildroot}%{python3_sitelib}/bleach/ -type d | grep vendor

if [ $? -ne 0 ]; then
    echo "Detected vendored libraries; please remove them."
    /usr/bin/false
fi;

%pytest -k 'not test_uri_value_allowed_protocols and not test_css_parsing_gauntlet_regex_backtracking'

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
