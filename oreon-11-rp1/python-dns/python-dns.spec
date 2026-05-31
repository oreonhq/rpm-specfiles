%global source0_hash none

%global pypi_name dnspython
%global rctag %{nil}

%if 0%{?rhel}
%bcond_with trio
%bcond_with doh
%bcond_with doq
%else
%bcond_without trio
%bcond_without doh
%bcond_without doq
%endif

Name:           python-dns
Version:        2.8.0
Release:        3%{?dist}
Summary:        DNS toolkit for Python

# The entire package is licensed with both licenses, see LICENSE file
License:        ISC
URL:            http://www.dnspython.org

Source0:        https://github.com/rthalley/%{pypi_name}/archive/v%{version}%{rctag}/%{pypi_name}-%{version}%{rctag}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%global _description %{expand:
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.
}

%description %_description
%package -n python3-dns
Summary:        %{summary}
%if ! 0%{?rhel}
Obsoletes:      python3-dns+curio < 2.3.0-6
%endif

# Duplicate package python3-dnspython
# https://bugzilla.redhat.com/show_bug.cgi?id=2361734
Provides:       python3-dnspython = %{version}-%{release}
# This makes sure all subpackages obsolete the replaced subpackages of python-dns
%define _local_file_attrs dnspython
%define __dnspython_obsoletes() %{gsub %{name} ^python3%%-dns python3-dnspython} < 2.7.0-3
%define __dnspython_path .*\.dist-info$

%description -n python3-dns %_description

%generate_buildrequires
%pyproject_buildrequires -r -x dnssec -x idna %{?with_trio:-x trio} %{?with_doh:-x doh} %{?with_doq:-x doq}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}%{rctag}
# strip exec permissions so that we don't pick up dependencies from docs
find examples -type f | xargs chmod a-x

# Allow newer cryptography and requests-toolbelt
sed -i 's/cryptography = {version=">=2.6,<40.0"/cryptography = {version=">=2.6,<42.0"/' pyproject.toml
sed -i 's/requests-toolbelt = {version=">=0.9.1,<0.11.0"/requests-toolbelt = {version=">=0.9.1,<=1.0.0"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dns

%check
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%pytest

%files -n python3-dns -f %{pyproject_files}
%license LICENSE
%doc README.md examples
%pycached %exclude %{python3_sitelib}/dns/_trio_backend.py

%pyproject_extras_subpkg -n python3-dns dnssec idna

%if %{with doh}
%pyproject_extras_subpkg -n python3-dns doh
%endif

%if %{with doq}
%pyproject_extras_subpkg -n python3-dns doq
%endif

%if %{with trio}
%pyproject_extras_subpkg -n python3-dns trio
%pycached %{python3_sitelib}/dns/_trio_backend.py
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-3
- Prepare for Oreon 11 (RP1)
