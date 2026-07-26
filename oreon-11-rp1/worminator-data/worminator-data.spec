%global source0_hash 80b0e7f410a291a62409c6cd9134d99cc738ffeebdca074a1f51f45ece12099a

Name:           worminator-data
Version:        3.0R2.1
Release:        34%{?dist}
Summary:        Data for worminator the game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://download.sourceforge.net/worminator/%{name}-%{version}.tar.gz
Source1:	license.txt
Source2:        license-change.txt
BuildArch:      noarch
Requires:       worminator

%description
Data for worminator the game where you play as The Worminator and fight your
way through many levels of madness and mayhem. Worminator features nine unique
weapons, visible character damage, full screen scrolling, sound and music, and
much more!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#put the docs where %doc wants them
install -p -m 0644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR

%build
#empty / notthing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/worminator
tar xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/worminator
rm $RPM_BUILD_ROOT%{_datadir}/worminator/ICON.ICO

%files
%doc license.txt license-change.txt
%{_datadir}/worminator

%changelog
%autochangelog
