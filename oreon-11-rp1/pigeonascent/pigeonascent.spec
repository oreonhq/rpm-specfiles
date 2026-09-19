%global source0_hash cb530893c27d57fa2c8854c70945a278dccedfecb6b502b6e97f5512a1fbca62

Summary: Take care of your own pigeon as they fight
Name: pigeonascent
Version: 1.5.2
Release: 14%{?dist}
License: MIT
Url: https://escada-games.itch.io/pigeon-ascent
Source0: http://www.identicalsoftware.com/pigeonascent/%{name}-%{version}.tgz
Source1: pigeonascent.desktop
Source2: pigeonascent.png
Source3: pigeonascent.metainfo.xml
BuildRequires: godot3-headless
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme
Requires: godot3-runner
BuildArch:      noarch
ExcludeArch:    ppc64le
ExcludeArch:    s390x

%description
Take care of your own pigeon as they fight increasingly stronger foes, and
then facing the legendary Pigeon God at the end… can you keep death far from
your bird?

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pigeonAscent

%build
godot3-headless --export-pack Linux64 pigeonascent.pck

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -p -m 644 pigeonascent.pck %{buildroot}%{_datadir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml

%files
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%license LICENSE
%{_datadir}/%{name}

%changelog
%autochangelog
