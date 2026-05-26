# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 17f21f9fac10cf60af2741f2c86a8ffd8007aa334d1eb78ff6ece130cb3777e3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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

BuildRequires:  gcc
BuildRequires: make
%description
libquvi-scripts contains the embedded lua scripts that libquvi
uses for parsing the media details. Some additional utility
scripts are also included.

%prep
%oreon_verify_sources
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
