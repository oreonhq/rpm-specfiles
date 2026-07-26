%global source0_hash eec49c296d41df39a6474d94ba4e3334e4c16dc180d3ea4a6defc2debfc39887

Name:           tuxmath
Version:        2.0.3
Release:        22%{?dist}
Summary:        Educational math tutor for children

License:        GPL-3.0-or-later AND CC-BY-1.0 AND OFL-1.1
URL:            http://tux4kids.alioth.debian.org/
Source0:        https://alioth.debian.org/frs/download.php/3271/%{name}_w_fonts-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch0:         tuxmath_w_fonts-2.0.1-gcc5.patch
Patch1:         pointer-types.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_net-devel
BuildRequires:  librsvg2-devel
BuildRequires:	t4k_common-devel
Requires:       hicolor-icon-theme

%description
TuxMath is an educational math tutor for children. It features several
different types of gameplay, at a variety of difficulty levels.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_w_fonts-%{version}
# remove unneeded font files
rm -f data/fonts/*.ttf
%patch -P 0 -p1
%patch -P 1 -p0

%build
export CPPFLAGS="$CPPFLAGS -fcommon -std=gnu17"
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 data/images/icons/icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/images/icons/tuxmath.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%{_pkgdocdir}
%{_bindir}/%{name}*
%{_bindir}/generate_lesson
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
%autochangelog
