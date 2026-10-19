%global source0_hash 464303645bafafd72418898368b2429458f709cf1eb6a15372fbcc396b64da63
%bcond_without tests
Name:           pytz
Version:        2026.4
Release:        1%{?dist}
Summary:        World Timezone Definitions for Python
License:        MIT
URL:            http://pytz.sourceforge.net/
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch:          pytz-zoneinfo.patch
Patch:          remove_tzinfo_test.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytz = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        %summary
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif
Requires:       tzdata
%description -n python3-%{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}/pytz/zoneinfo
%oreon_autofiles main usr/lib/python3*/site-packages/pytz* usr/lib64/python3*/site-packages/pytz* usr/bin/*
%if %{with tests}
%check

%pytest -v
%endif
%doc README.rst
%{python3_sitelib}/pytz/
%{python3_sitelib}/pytz-%{version}.dist-info
%files
%files -n python3-pytz -f %{oreon_filedir}/python3-pytz.list

%changelog

%autochangelog
