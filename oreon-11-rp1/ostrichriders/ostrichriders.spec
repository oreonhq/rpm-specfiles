%global source0_hash e558d2172aaa3bd51d5b82651f8697903de2a945fa0e555103b1f9d06e609541

Summary: Knights flying on ostriches compete against other riders
Name: ostrichriders
Version: 0.6.5
Release: 18%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Url: http://www.identicalsoftware.com/ostrichriders
Source: http://www.identicalsoftware.com/ostrichriders/%{name}-%{version}.tgz
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: SFML-devel
BuildRequires: desktop-file-utils
BuildRequires: fontconfig-devel
BuildRequires: pkgconfig
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

%description
Enemy knights are invading the kingdom. As one of the elite ostrich riders,
it is your duty to defend the kingdom. With lance in hand you fly off.
Remember to stay above your opponent least you fall to his lance. Collect the
eggs least your opponent hatches stronger than before. Work together with
other knights.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%license LICENCE
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
