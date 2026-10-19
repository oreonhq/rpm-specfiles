%global source0_hash f9916b269cb9c5d5ba61d7bf5c4bf1a0037cf934907622343df8d9edb1c6d11b
Name:           python-django-mailman3
Version:        1.3.15
Release:        1%{?dist}
Summary:        Django library to help interaction with Mailman
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/django-mailman3
Source0:        https://files.pythonhosted.org/packages/source/d/django_mailman3/django_mailman3-%{version}.tar.gz
Patch:          django-mailman3-localdeps.patch
Patch:          django-mailman3-django52.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-mailman3 = %{version}-%{release}
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-django-mailman3
Summary:        Django library to help interaction with Mailman
%description -n python%{python3_pkgversion}-django-mailman3

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir django_mailman3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/django_mailman3* usr/lib64/python3*/site-packages/django_mailman3* usr/bin/*

%check

PYTHONPATH=.:${PYTHONPATH} %pytest -v --deselect \
  django_mailman3/tests/test_signals.py::SignalsTestCase::test_social_account_added
%files
%files -n python3-django-mailman3 -f %{oreon_filedir}/python3-django-mailman3.list

%changelog

%autochangelog
