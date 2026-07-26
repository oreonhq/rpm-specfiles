%global source0_hash d4abe076858a3433b2d9c002d7196a5d39b78727cda8fd684873e7e0e8ea8112

%if %{defined el8}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:       compose-utils
Version:    0.1.51
Release:    1%{?dist}
Summary:    Utilities for working with composes

License:    GPL-2.0-only
URL:        https://pagure.io/compose-utils
Source0:    https://pagure.io/releases/compose-utils/%{name}-%{version}.tar.bz2

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-productmd >= 1.33
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-kobo
BuildRequires:  python%{python3_pkgversion}-kobo-rpmlib >= 0.10.0
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

Requires:       python3-%{name} = %{version}-%{release}

BuildArch:  noarch

%description
A set of tools for working with composes produced by pungi.

%package -n python%{python3_pkgversion}-%{name}
Summary:    Python 3 libraries supporting tools for working with composes
Requires:   python%{python3_pkgversion}-productmd >= 1.33
Requires:   python%{python3_pkgversion}-kobo
Requires:   python%{python3_pkgversion}-kobo-rpmlib >= 0.10.0
Requires:   rsync

%description -n python%{python3_pkgversion}-%{name}
Python 3 libraries supporting tools for working with composes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n compose_utils-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

%if %{with tests}
%check
%pyproject_check_import

%pytest
%endif

%files
%license COPYING GPL
%doc AUTHORS README.rst
%{_bindir}/*
%{_mandir}/man1/*

%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%license GPL
%doc AUTHORS README.rst

%changelog
%autochangelog
