Summary: NSS module to look up from files in /usr/lib as well
Name: nss-altfiles
Version: 2.23.0
Release: 9%{?dist}
Source0: https://github.com/flatcar/nss-altfiles/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: macros.altfiles
Patch1: 0001-build-sys-Inherit-LDFLAGS.patch
# From https://github.com/flatcar/nss-altfiles/commit/de2b32289bf701ce3c8167a1b58436866922085e
Patch2: 0003-deprecate-RES_USE_INET6.patch
License: LGPL-2.1-or-later and MIT
URL: https://github.com/flatcar/nss-altfiles

BuildRequires: make
BuildRequires: glibc-devel
BuildRequires: gcc
BuildRequires: git

%description
When installed, this package allows looking up users in %{_prefix}/lib/passwd,
and from respective files for all other NSS maps.

%prep
%autosetup -Sgit

%build
./configure --with-types=all --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.altfiles

%files
%doc README.md
%{_libdir}/*.so.*
%{_rpmmacrodir}/macros.altfiles

%ldconfig_scriptlets

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.23.0-9
- Prepare for Oreon 11 (RP1)
