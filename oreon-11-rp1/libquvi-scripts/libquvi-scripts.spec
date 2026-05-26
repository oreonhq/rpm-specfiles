%global debug_package %{nil}

Name:           libquvi-scripts
Version:        0.9.20131130
Release:        27%{?dist}
Summary:        Embedded lua scripts for parsing the media details
License:        AGPL-3.0-or-later
URL:            http://quvi.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       lua-expat
Requires:       lua-socket
Requires:       lua-json

# https://bugzilla.redhat.com/show_bug.cgi?id=1134853
Patch0: 0001-guardian.lua-Update-for-website-changes.patch
# oreon url source checksums begin
%global source0_sha256 17f21f9fac10cf60af2741f2c86a8ffd8007aa334d1eb78ff6ece130cb3777e3
%global source0_file libquvi-scripts-0.9.20131130.tar.xz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires: make
%description
libquvi-scripts contains the embedded lua scripts that libquvi
uses for parsing the media details. Some additional utility
scripts are also included.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libquvi-scripts-0.9.20131130.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "17f21f9fac10cf60af2741f2c86a8ffd8007aa334d1eb78ff6ece130cb3777e3" || { echo "oreon: Source0 SHA256 mismatch for libquvi-scripts-0.9.20131130.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1

%build
%configure --with-nsfw

%install
# Noarch fix.
make install DESTDIR=%{buildroot} pkgconfigdir=%{_datadir}/pkgconfig/

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/%{name}
%{_datadir}/pkgconfig/%{name}*.pc
%{_mandir}/man7/%{name}.7*
%{_mandir}/man7/quvi-modules*.7*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.20131130-27
- Prepare for Oreon 11 (RP1)
