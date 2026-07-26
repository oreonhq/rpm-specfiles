%global source0_hash e012f0cc8401efcf2620332339011564738ae32be8c84b2e43ce8beaec1067b6

%global pypi_name cssmin

Name:       python-cssmin
Version:    0.2.0
Release:    42%{?dist}
Summary:    A Python port of the YUI CSS compression algorithm

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://github.com/zacharyvoase/cssmin
Source0:    https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:     python-cssmin-rename-bin.patch

BuildArch:  noarch
BuildRequires:  python3-devel python3-setuptools

%global _description\
A Python port of the YUI CSS compression algorithm. The library can be used for\
merging and compressing CSS files.

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}
Requires:   python3-setuptools

%description -n python3-%{pypi_name} %_description

This is the version for Python 3.x.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
%patch -P0 -p1

# remove shebang from non-executable
sed '1{\@^#!/usr/bin/env python@d}' src/cssmin.py > src/cssmin.py.new &&
touch -r  src/cssmin.py src/cssmin.py.new &&
mv src/cssmin.py.new src/cssmin.py

sed -i 's/^from distribute_setup/#/' setup.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build -O1 --root %{buildroot}

%check
cd src && \

%{__python3} -c 'import cssmin; cssmin.cssmin("""\
#href { \
  font-size: 3; \
}""")'; \

%files -n python3-cssmin
%{python3_sitelib}/cssmin.py
%{python3_sitelib}/__pycache__/cssmin.*.py*
%{python3_sitelib}/*.egg-info
%{_bindir}/*

%changelog
%autochangelog
