%global source0_hash be4ec9a1dbdd9629979eaf0b05e982dbf4b44588287b6a17122c15875f2c7f01

# Currently broken in koji
%bcond_with tests

# Without this, the resulting insertlib will segfault
%define _lto_cflags %{nil}

%define debug_package %{nil}

%global pkgname rpm-head-signing
%global srcname rpm_head_signing

Name:           rpm-head-signing
Version:        1.7.4
Release:        12%{?dist}
Summary:        Small python module to extract RPM header and file digests
License:        MIT
URL:            https://github.com/fedora-iot/rpm-head-signing
Source0:        %url/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Make this build with RPM 6
Patch:          https://github.com/fedora-iot/rpm-head-signing/pull/80.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Plus, python3dist(xattr) is missing on i686
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  ima-evm-utils
BuildRequires:  ima-evm-utils-devel
BuildRequires:  rpm-devel
BuildRequires:  rpm-sign
BuildRequires:  cpio
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  zstd
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-koji
BuildRequires:  python%{python3_pkgversion}-rpm
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-pyxattr

Requires:  python%{python3_pkgversion}-koji
Requires:  python%{python3_pkgversion}-rpm
Requires:  python%{python3_pkgversion}-cryptography
Requires:  python%{python3_pkgversion}-pyxattr

%{?python_provide:%python_provide python3-%{pkgname}}

%description
A small Python module (with C helper) to extract a RPM header and file
digests and reinsert the signature and signed file digests. This is
used for when you want to retrieve the parts to sign if you have a
remote signing server without having to transmit the entire RPM over
to the server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for lib in rpm_head_signing/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new
 mv $lib.new $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
# To make sure we get to use the installed version
mv rpm_head_signing rpm_head_signing.orig

PYTHONPATH=%{buildroot}%{python3_sitearch} SKIP_IMA_LIVE_CHECK=true python3 test.py
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/verify-rpm-ima-signatures

%changelog
%autochangelog
