%global source0_hash 7a9552711d23bf3ee27c45374097fc67f2276a8aebdbff155c5cf264f254e884
%global pypi_name pure-protobuf
Name:           python-%{pypi_name}
Version:        3.1.5
Release:        1%{?dist}
Summary:        Python implementation of Protocol Buffers data types with dataclasses support
License:        MIT
URL:            https://github.com/eigenein/protobuf
Source0:        https://github.com/eigenein/protobuf/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         poetry-strict.patch
BuildArch:      noarch
%if 0%{?el8}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pure-protobuf = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        Python implementation of Protocol Buffers data types with dataclasses support
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n protobuf-%{version} -p1

sed -i s/0.0.0/%{version}/g pyproject.toml

# Fix shebangs
pushd pure_protobuf
sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' \
    __init__.py
popd

%build

%pyproject_wheel
%install
%pyproject_install
pushd %{buildroot}%{python3_sitelib}/pure_protobuf/
chmod +x __init__.py
popd
%oreon_autofiles main usr/lib/python3*/site-packages/pure_protobuf* usr/lib64/python3*/site-packages/pure_protobuf* usr/bin/*

%files
%files -n python3-pure-protobuf -f %{oreon_filedir}/python3-pure-protobuf.list

%changelog

%autochangelog
