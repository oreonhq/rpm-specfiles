%global source0_hash 7aeab50f970d46c068e7a36dd162cb242591edf72a1d04efd21374772b931741
%bcond tests 1
Name:           python-webtest
Version:        3.0.7
Release:        1%{?dist}
Summary:        Helper to test WSGI applications
License:        MIT
URL:            https://github.com/Pylons/webtest
Source0:        https://files.pythonhosted.org/packages/source/w/webtest/webtest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-webtest = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-webtest
Summary:        Helper to test WSGI applications
%description -n python3-webtest

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n webtest-%{version}

# remove coverage dependencies
sed -e '/coverage/d' \
    -e '/pytest-cov/d' \
    -i setup.py

%build

%pyproject_wheel
rm -f docs/Makefile docs/conf.py docs/changelog.rst
%install
%pyproject_install
%oreon_autofiles python3-webtest usr/lib/python3*/site-packages/webtest* usr/lib64/python3*/site-packages/webtest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webtest* usr/lib64/python3*/site-packages/webtest* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-webtest -f %{oreon_filedir}/python3-webtest.list

%changelog

%autochangelog
