Name: ipcalc
Version: 1.0.3
Release: %autorelease
Summary: IP network address calculator
License: GPL-2.0-or-later
URL: https://gitlab.com/ipcalc/ipcalc
Source0: https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/ipcalc-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 451f323764f37ea6057e0ade60a0473938232ab2a92b97ffdc8c4860a8c76cfc
%global source0_file ipcalc-1.0.3.tar.gz
# oreon url source checksums end

BuildRequires: gcc, libmaxminddb-devel, meson, rubygem-ronn-ng
Recommends:    libmaxminddb, geolite2-city, geolite2-country

# Explicitly conflict with older initscript packages that ship ipcalc
Conflicts: initscripts < 9.63
# Obsolete ipcalculator
Obsoletes:  ipcalculator < 0.41-20


%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ipcalc-1.0.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "451f323764f37ea6057e0ade60a0473938232ab2a92b97ffdc8c4860a8c76cfc" || { echo "oreon: Source0 SHA256 mismatch for ipcalc-1.0.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%meson -Duse_maxminddb=enabled -Duse_runtime_linking=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files

%{_bindir}/ipcalc
%license COPYING
%doc README.md
%{_mandir}/man1/ipcalc.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-1
- Prepare for Oreon 11 (RP1)
