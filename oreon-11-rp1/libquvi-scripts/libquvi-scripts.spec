%global source0_hash 17f21f9fac10cf60af2741f2c86a8ffd8007aa334d1eb78ff6ece130cb3777e3
%global debug_package %{nil}
Name:           libquvi-scripts
Version:        0.9.20131130
Release:        1%{?dist}
Summary:        Embedded lua scripts for parsing the media details
License:        AGPL-3.0-or-later
URL:            http://quvi.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       lua-expat
Requires:       lua-socket
Requires:       lua-json
Patch0: 0001-guardian.lua-Update-for-website-changes.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
libquvi-scripts contains the embedded lua scripts that libquvi
uses for parsing the media details. Some additional utility
scripts are also included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1

%build

%configure --with-nsfw
%install
make install DESTDIR=%{buildroot} pkgconfigdir=%{_datadir}/pkgconfig/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.20131130-27
- Prepare for Oreon 11 (RP1)
