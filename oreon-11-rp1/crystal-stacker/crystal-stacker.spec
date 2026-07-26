%global source0_hash 7f4aa2878b71239e865ab32040240b6d94b04a41c5cb9ebff55e2311b7dfe23f

Name:           crystal-stacker
Version:        1.5
Release:        47%{?dist}
Summary:        Falling blocks, match 3 or more of the same color crystals
# Automatically converted from old format: Crystal Stacker - review is highly recommended.
License:        CrystalStacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://www.t3-i.com/games/crystal_stacker/downloads/crystal_stacker-1.5-src.zip
Source1:        %{name}.desktop
Source2:        %{name}-theme-editor.desktop
Source3:        %{name}-48.png
Source4:        %{name}-128.png
Source5:        %{name}.appdata.xml
Patch0:         crystal-stacker-1.5-ImplicitDSOLinking.patch
Patch1:         crystal-stacker-1.5-fcommon-fix.patch
BuildRequires:  gcc allegro-devel dumb-devel
BuildRequires:  ImageMagick desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
If you've played Columns then you know what Crystal Stacker is all about.
Match 3 or more of the same color crystals either horizontally, vertically,
or diagonally to destroy them. For every 45 crystals you destroy, the level
increases and the crystals fall faster. The higher the level, the more points
you are awarded for destroying crystals.

%package theme-editor
Summary:        Themes editor for Crystal Stacker
Requires:       %{name} = %{version}

%description theme-editor
Create new Themes for Crystal Stacker

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c
%{__sed} -i 's/\r//' ce/*.txt cs/*.txt

%build
pushd cs/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
popd

pushd ce/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-char-subscripts"
popd

convert cs/cs.ico %{name}.png
convert ce/ce.ico %{name}-theme-editor.png

%install
pushd cs/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

pushd ce/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{name}.png %{name}-theme-editor.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc cs/*.txt
%{_bindir}/crystal-stacker
%dir %{_datadir}/crystal-stacker
%{_datadir}/crystal-stacker/cs.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files theme-editor
%doc ce/*.txt
%{_bindir}/crystal-stacker-theme-editor
%{_datadir}/crystal-stacker/ce.dat
%{_datadir}/applications/%{name}-theme-editor.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}-theme-editor.png

%changelog
%autochangelog
