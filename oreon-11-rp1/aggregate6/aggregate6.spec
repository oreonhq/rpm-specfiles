%global source0_hash 7bcaa326c84a8d81d6da4f50c0f80a2e6884b9b7a97ae7a1fccbe6259279929c

Summary:        Tool to compress an unsorted list of IPv4 and IPv6 prefixes
Name:           aggregate6
Version:        1.0.15
Release:        1%{?dist}
License:        BSD-2-Clause
URL:            https://github.com/job/aggregate6
Source0:        https://github.com/job/aggregate6/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
# Tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description
The aggregate6 tool takes a list of IPv4/IPv6 prefixes in conventional
format on STDIN, and performs two optimisations to attempt to reduce
the length of the prefix list, which can often be useful in context of
compressing firewall rules or BGP prefix-list filters.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python module to compress an unsorted list of IPv4 and IPv6 prefixes
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-py-radix >= 0.10.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
%endif

%description -n python%{python3_pkgversion}-%{name}
The aggregate6 Python module takes a list of IPv4/IPv6 prefixes in
conventional format as parameter, and performs two optimisations to
attempt to reduce the length of the prefix list, which can often be
useful in context of compressing firewall rules or BGP prefix-list
filters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_wheel
%else
%py3_build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_install
%pyproject_save_files %{name}
%else
%py3_install
%{?el8:%py3_shebang_fix $RPM_BUILD_ROOT%{_bindir}/%{name}}
%endif

# Correct man page installation path
install -D -p -m 0644 $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}/man7/%{name}.7
rm -rf $RPM_BUILD_ROOT%{_prefix}/man/

# Remove shebang from non-executable script
sed -e '1{\|^#![[:space:]]*/|d}' -i $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
touch -c -r %{name}/%{name}.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py

%check
%pytest

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man7/%{name}.7*

%if 0%{?fedora} || 0%{?rhel} >= 9
%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%else
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%endif
%license LICENSE

%changelog
%autochangelog
