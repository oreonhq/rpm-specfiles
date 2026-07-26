%global source0_hash 2a321e3239a42f83c8df34145df1be563da300a558ca4aac022afaee498dfdf4

Name:           worminator
Version:        3.0R2.1
Release:        48%{?dist}
Summary:        Sidescrolling platform and shoot'em up action-game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://downloads.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:        worminator.png
Source2:        worminator.desktop
Source3:        %{name}.appdata.xml
Patch0:         worminator-3.0R2.1-speed.patch
Patch1:         worminator-3.0R2.1-format-security.patch
Patch2:         worminator-3.0R2.1-c99.patch
Patch3:         worminator-3.0R2.1-remove-al-fix-aliases.patch
Patch4:         worminator-3.0R2.1-fix-compiler-warnings.patch
Patch5:         worminator-3.0R2.1-c23.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel desktop-file-utils libappstream-glib
Requires:       worminator-data >= 3.0R2.1-2, hicolor-icon-theme

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\r//' ReadMe.txt

%build
gcc $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs` -lm

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                           \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
        $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc ReadMe.txt changes.unix
%license license.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/worminator.desktop
%{_datadir}/icons/hicolor/64x64/apps/worminator.png

%changelog
%autochangelog
