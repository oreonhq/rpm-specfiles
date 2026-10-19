%global source0_hash 9fc6197e1810c9e9cb4a7199a63847b199ba5ed7c90c5fdb81cbf5b8f260f910
Name:           python-xattr
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python wrapper for extended filesystem attributes
License:        MIT
URL:            https://github.com/xattr/xattr
Source0:        https://github.com/xattr/xattr/archive/v%{version}/v%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.16.0
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-xattr = %{version}-%{release}
# /oreon:deps
%package -n       python3-xattr+test
Summary:        Metapackage for python3-xattr test extras
Requires:       python3-xattr = %{version}-%{release}
Provides:       python3dist(xattr[test]) = %{version}-%{release}

%description -n python3-xattr+test
Metapackage for python3-xattr test extras.

%description

%package -n python3-xattr
Summary:        Python wrapper for extended filesystem attributes
# oreon:reqs
Requires:       python3dist(cffi) >= 1.16.0
# /oreon:reqs
%description -n python3-xattr

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir xattr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xattr usr/lib/python3*/site-packages/xattr* usr/lib64/python3*/site-packages/xattr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xattr* usr/lib64/python3*/site-packages/xattr* usr/bin/*

%check

%pytest %{?copr_projectname:-k 'not (test_attr_fs_encoding_ascii or test_attr_fs_encoding_unicode or test_update)'}
%files
%files -n python3-xattr -f %{oreon_filedir}/python3-xattr.list

%changelog

%autochangelog
