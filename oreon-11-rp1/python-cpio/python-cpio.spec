%global source0_hash 522a5c07fc14b280bff9cb6adbb02d4626e65e926140f1d5662be088eeea2bd3
Name:           python-cpio
Version:        0.1
Release:        1%{?dist}
Summary:        A Python module for accessing cpio archives
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://sourceforge.net/projects/python-cpio.berlios/
Source0:        https://downloads.sourceforge.net/project/python-cpio.berlios/python-cpio-%{version}.tar.bz2
Patch0:        cpioarchive_supports_2_3.patch
Patch1:        cpioarchive_bytes_str_compatibility.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-cpio
Summary: %summary
%description -n python3-cpio

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0
%patch -P1

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-cpio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-cpio -f %{oreon_filedir}/python3-cpio.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-58
- Import
