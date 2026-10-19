%global source2_hash 0cdba4240cac049e5fdd6cff8cf2785c9fb2d69563f414b3d57c1324c42215b1
%global source1_hash 0789d87bdbfcd8ae27dffa6d80135343774a79a0cd1d8fc91d945756c60228df
%global source0_hash 48c578ecf8ea0bd4351b1752470e301a90a3761c7c21f00f953dcf6d6fa6ee5a
Name:           pyxattr
Summary:        Extended attributes library wrapper for Python
Version:        0.8.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://pyxattr.k1024.org/
Source0:        https://pyxattr.k1024.org/downloads/pyxattr-%{version}.tar.gz
Source1:        https://pyxattr.k1024.org/downloads/pyxattr-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libattr-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        Extended attributes library wrapper for Python
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export TEST_IGNORE_XATTRS=security.selinux
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
python3 -m pytest tests %{?copr_projectname:-k 'not (binary_payload or create_on_existing or empty_value or large_value or many_ops or mixed_access or set_get_remove)'}
%files -f %{oreon_filedir}/main.list
%files -n python3-pyxattr -f %{oreon_filedir}/python3-pyxattr.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-19
- Prepare for Oreon 11 (RP1)
