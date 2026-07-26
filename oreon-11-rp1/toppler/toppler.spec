%global source0_hash af64a7aa3336b3019316823560322a400bf7426c3bf608c89d7e1f218cca448d

%global commit 5e3e581bb7b58098f54df9b634c7bd4a23ba66b5
%bcond_with rebuild_gfx

Name:           toppler
Version:        1.3
Release:        8%{?dist}
Summary:        Platform game
License:        GPL-3.0-only
URL:            https://gitlab.com/roever/toppler/
Source0:        https://gitlab.com/roever/toppler/-/archive/v%{version}/%{name}-%{version}.tar.bz2
Source1:        toppler.desktop
Patch2:         toppler-1.1.5-highscore.patch
Patch100:       toppler-1.3-fix_makefile.patch
Patch101:       toppler-1.3-format_security.patch
Patch102:       toppler-1.3-head.patch
Patch103:       toppler-1.3-missing_include.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  zlib-devel
# Needed to rebuild the graphics from source
# This is currently segfault'ing
%if 0%{with rebuild_gfx}
BuildRequires:  gimp
BuildRequires:  ImageMagick
BuildRequires:  povray
%endif

%description
Help a cute little green animal switch off some kind of "evil" mechanism. The
"power off switch" is hidden somewhere in high towers. On your way to the
target you need to avoid a lot of strange robots that guard the tower.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}-%{commit}
#patch -P2 -p1
%patch -P100 -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
# Building graphics is broken with Gimp 3
%if %{with rebuild_gfx} && 0%{?fedora} && 0%{?fedora} <= 40
rm -f toppler.dat
%endif

%build
%set_build_flags
%if %{with rebuild_gfx} && 0%{?fedora} && 0%{?fedora} <= 40
%make_build \
  GIMP="gimp-console --batch-interpreter plug-in-script-fu-eval" \
  toppler.dat
%endif
%make_build \
  CXXFLAGS="$CXXFLAGS" \
  LDFLAGS="$LDFLAGS" \
  STATEDIR=%{_localstatedir}/games \
  toppler translation

%install
%set_build_flags
%make_install \
  CXXFLAGS="$CXXFLAGS" \
  LDFLAGS="$LDFLAGS" \
  STATEDIR=%{_localstatedir}/games

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_localstatedir}/games/
touch %{buildroot}%{_localstatedir}/games/toppler.hsc

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -p -m 0644 dist/toppler*.xpm %{buildroot}%{_datadir}/pixmaps/

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md doc/changelog.md
%{_bindir}/toppler
%{_datadir}/toppler
%{_datadir}/applications/toppler.desktop
%{_datadir}/pixmaps/toppler*.xpm
%verify(not md5 size mtime) %config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/toppler.hsc
%{_mandir}/man6/toppler.6.*

%changelog
%autochangelog
