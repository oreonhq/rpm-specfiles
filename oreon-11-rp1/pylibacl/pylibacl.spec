%global source2_hash 0cdba4240cac049e5fdd6cff8cf2785c9fb2d69563f414b3d57c1324c42215b1
%global source0_hash 56c15e867fe4c724531bbf97407589cbbf8dbd285a8d84fe7ecc90fc322378d7
Name:           pylibacl
Summary:        POSIX.1e ACLs library wrapper for Python
Version:        0.7.2
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pylibacl.k1024.org
Source0:        https://%{name}.k1024.org/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/downloads/%{name}-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc
Patch:          https://github.com/iustin/pylibacl/commit/64011b3c82746.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libacl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        POSIX.1e ACLs library wrapper for Python
%{?python_provide:%python_provide python3-%{name}}
Provides:  py3libacl = %{version}-%{release}
Obsoletes: py3libacl < 0.5.4
%description -n python3-%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
python3 -m pytest tests -v \
%ifarch s390x
  -k 'not TestAclExtensions and not test_acl_init_copy_ext_invalid'
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-pylibacl -f %{oreon_filedir}/python3-pylibacl.list

%changelog

%autochangelog
