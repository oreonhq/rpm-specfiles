%global source0_hash f3418da7df29e6d9b11fd7d990289d16397dc1020e4e35192e11aee826922860
Name:           python-libnacl
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python bindings for libsodium based on ctypes
License:        Apache-2.0
URL:            https://libnacl.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/l/libnacl/libnacl-%{version}.tar.gz
BuildArch:      noarch
Requires:       libsodium
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libnacl = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-libnacl
Summary:        Python bindings for libsodium based on ctypes
%description -n python3-libnacl

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libnacl-%{version}
%oreon_prep
%build

%pyproject_wheel
make -C doc man html
%install
%pyproject_install
install -D -m 644 doc/_build/man/libnacl.1 %{buildroot}%{_mandir}/man1/libnacl.1
%oreon_autofiles python3-libnacl usr/lib/python3*/site-packages/libnacl* usr/lib64/python3*/site-packages/libnacl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libnacl* usr/lib64/python3*/site-packages/libnacl* usr/bin/*

%check

%{pytest}
%files
%files -n python3-libnacl -f %{oreon_filedir}/python3-libnacl.list

%changelog

%autochangelog
