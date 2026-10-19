%global source0_hash ebde65f3f6bb9531a81016c6fef3eb95a61181adc47b7f949e9c0ea47911669e
Name:           python-looseversion
Version:        1.3.0
Release:        1%{?dist}
Summary:        Version numbering for anarchists and software realists
License:        PSF-2.0
URL:            https://pypi.org/pypi/looseversion
Source0:        https://files.pythonhosted.org/packages/source/l/looseversion/looseversion-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-looseversion = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-looseversion
Summary:        Version numbering for anarchists and software realists
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-looseversion

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir looseversion-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-looseversion usr/lib/python3*/site-packages/looseversion* usr/lib64/python3*/site-packages/looseversion* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/looseversion* usr/lib64/python3*/site-packages/looseversion* usr/bin/*

%check

%pytest -v tests.py
%files
%files -n python3-looseversion -f %{oreon_filedir}/python3-looseversion.list

%changelog

%autochangelog
