%global source0_hash ca93be8964c92fe3a2c945640cd3e93c95ae7abe24290818f4fe7f6e5a7cd835

Name:           sfxr
Version:        1.2.1
Release:        23%{?dist}
Summary:        Sound effect generator
License:        MIT
URL:            http://www.drpetter.se/project_sfxr.html
Source0:        http://www.drpetter.se/files/sfxr-sdl-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         sfxr-sdl-gcc8x.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel gtk3-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
This little tool was made to provide a simple means of getting basic sound
effects into a game. You just need to hit a few buttons in this application
to get some largely randomized effects. All the parameters used to create
each sound are manually tweakable to allow fine-tuning if you feel like
getting your hands dirty.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sfxr-sdl-%{version}
sed -i 's/\r//g' readme.txt

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install
desktop-file-edit $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop \
  --set-key=Keywords --set-value="Sound;Audio;Effects;Generator;"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc readme.txt ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
