%global source0_hash aab25d3ade9969b51cf3f197c2ecbc1ba2c10cb126a142798d54c275fe3178af

%global srcname rebulk

Name: python-%{srcname}
Version: 3.3.0
Release: 12%{?dist}
Summary: ReBulk is a python library that performs advanced searches in strings
# Everything licensed as MIT, except:
# rebulk/toposort.py: Apache (v2.0)
# rebulk/test/test_toposort.py: Apache (v2.0)
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-MIT AND Apache-2.0
URL: https://github.com/Toilal/rebulk
Source: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%global _description %{expand:
ReBulk is a python library that performs advanced searches in strings that
would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and
extendable API.}

%description %_description

%package -n python3-%{srcname}
Summary: %summary

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
