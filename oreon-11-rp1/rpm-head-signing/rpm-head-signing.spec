%global source0_hash be4ec9a1dbdd9629979eaf0b05e982dbf4b44588287b6a17122c15875f2c7f01
%bcond_with tests
%define _lto_cflags %{nil}
%define debug_package %{nil}
%global pkgname rpm-head-signing
%global srcname rpm_head_signing
Name:           rpm-head-signing
Version:        1.7.4
Release:        1%{?dist}
Summary:        Small python module to extract RPM header and file digests
License:        MIT
URL:            https://github.com/fedora-iot/rpm-head-signing
Source0:        https://github.com/fedora-iot/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          https://github.com/fedora-iot/rpm-head-signing/pull/80.patch
ExcludeArch:    %{ix86}
%ifarch %{valgrind_arches}
%endif
Requires:  python%{python3_pkgversion}-koji
Requires:  python%{python3_pkgversion}-rpm
Requires:  python%{python3_pkgversion}-cryptography
Requires:  python%{python3_pkgversion}-pyxattr
%{?python_provide:%python_provide python3-%{pkgname}}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpm-head-signing = %{version}-%{release}
# /oreon:deps
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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main
%if %{with tests}
%check

mv rpm_head_signing rpm_head_signing.orig
PYTHONPATH=%{buildroot}%{python3_sitearch} SKIP_IMA_LIVE_CHECK=true python3 test.py
%endif
%files

%changelog

%autochangelog
