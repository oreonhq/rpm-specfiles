%global source0_hash a2c026226f1a1eaace81362fda27b3df479693aefe19f160d6c4c3a032add498
%global srcname %(echo %{name} | sed 's/^python-//')
Name:           python-fqdn
Version:        1.5.1
Release:        1%{?dist}
Summary:        Validates fully-qualified domain names against RFC 1123
BuildArch:      noarch
License:        MPL-2.0
URL:            https://github.com/ypcrts/fqdn
Source0:        https://github.com/ypcrts/fqdn/archive/refs/tags/v%{version}/fqdn-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fqdn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{srcname}
Summary:        Validates fully-qualified domain names against RFC 1123
BuildRequires:  python3-devel
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove coverage for fedora packaging.
sed -e '/pytest-cov/d' tox.ini
sed -e 's/--cov=[^[:blank:]]\+//' 'tox.ini'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/fqdn* usr/lib64/python3*/site-packages/fqdn* usr/bin/*

%check

%pytest
%files
%files -n python3-fqdn -f %{oreon_filedir}/python3-fqdn.list

%changelog

%autochangelog
