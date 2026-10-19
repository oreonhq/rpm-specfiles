%global source0_hash b2e5b40261e20f354d198eae92afc10d750afb487ed5e50f9c4eaf07c184146f
Name:           python-html5lib
Summary:        A python based HTML parser/tokenizer
Version:        1.1
Release:        1%{?dist}
Epoch:          1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source0:        https://files.pythonhosted.org/packages/source/h/html5lib/html5lib-1.1.tar.gz
Patch:        https://github.com/html5lib/html5lib-python/pull/506.patch
Patch:        https://github.com/html5lib/html5lib-python/pull/573.patch
Patch:        https://github.com/html5lib/html5lib-python/pull/583.patch
Patch:        https://github.com/html5lib/html5lib-python/pull/591.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-html5lib = %{version}-%{release}
# /oreon:deps
%description
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%package -n python3-html5lib
Summary:        A python based HTML parser/tokenizer
%description -n python3-html5lib
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n html5lib-%{version}

# Use standard library unittest.mock instead of 3rd party mock
# From https://github.com/html5lib/html5lib-python/pull/536
sed -i 's/from mock import/from unittest.mock import/' html5lib/tests/test_meta.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-html5lib usr/lib/python3*/site-packages/html5lib* usr/lib64/python3*/site-packages/html5lib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/html5lib* usr/lib64/python3*/site-packages/html5lib* usr/bin/*

%check

%pytest
%files
%files -n python3-html5lib -f %{oreon_filedir}/python3-html5lib.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-1
- Prepare for Oreon 11 (RP1)
