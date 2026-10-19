%global source0_hash 7bcaa326c84a8d81d6da4f50c0f80a2e6884b9b7a97ae7a1fccbe6259279929c
Summary:        Tool to compress an unsorted list of IPv4 and IPv6 prefixes
Name:           aggregate6
Version:        1.0.15
Release:        1%{?dist}
License:        BSD-2-Clause
URL:            https://github.com/job/aggregate6
Source0:        https://github.com/job/aggregate6/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aggregate6 = %{version}-%{release}
# /oreon:deps
%description
The aggregate6 tool takes a list of IPv4/IPv6 prefixes in conventional
format on STDIN, and performs two optimisations to attempt to reduce
the length of the prefix list, which can often be useful in context of
compressing firewall rules or BGP prefix-list filters.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python module to compress an unsorted list of IPv4 and IPv6 prefixes
%description -n python%{python3_pkgversion}-%{name}
The aggregate6 Python module takes a list of IPv4/IPv6 prefixes in
conventional format as parameter, and performs two optimisations to
attempt to reduce the length of the prefix list, which can often be
useful in context of compressing firewall rules or BGP prefix-list
filters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
%{?el8:%py3_shebang_fix $RPM_BUILD_ROOT%{_bindir}/%{name}}
install -D -p -m 0644 $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}/man7/%{name}.7
rm -rf $RPM_BUILD_ROOT%{_prefix}/man/
sed -e '1{\|^#![[:space:]]*/|d}' -i $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
touch -c -r %{name}/%{name}.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
%oreon_autofiles python3-aggregate6 usr/lib/python3*/site-packages/aggregate6* usr/lib64/python3*/site-packages/aggregate6* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aggregate6* usr/lib64/python3*/site-packages/aggregate6* usr/bin/*

%check

%pytest
%files
%files -n python3-aggregate6 -f %{oreon_filedir}/python3-aggregate6.list

%changelog

%autochangelog
