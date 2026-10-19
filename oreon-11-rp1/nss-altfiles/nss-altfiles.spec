%global source0_hash 2ab9ff43ccb5b6f3f5d18e7eddb160828551eab7ac71beeca10727a1e8dcc2fc
Summary:        NSS module to look up from files in /usr/lib as well
Name: nss-altfiles
Version: 2.23.0
Release:        9%{?dist}
Source0:        https://github.com/flatcar/nss-altfiles/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: macros.altfiles
Patch1: 0001-build-sys-Inherit-LDFLAGS.patch
Patch2: 0003-deprecate-RES_USE_INET6.patch
License: LGPL-2.1-or-later and MIT
URL: https://github.com/flatcar/nss-altfiles
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glibc-devel
BuildRequires:  make
# /oreon:deps
%description
When installed, this package allows looking up users in %{_prefix}/lib/passwd,
and from respective files for all other NSS maps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./configure --with-types=all --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.altfiles
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.23.0-9
- Prepare for Oreon 11 (RP1)
