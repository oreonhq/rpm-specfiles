%global source0_hash a1c141a34d19a59607ae81166a19864eb8c84cf86b155462fed31a6d56e1624a

Name:           chromium-bsu
Version:        0.9.16.1
Release:        26%{?dist}
Summary:        Fast paced, arcade-style, top-scrolling space shooter
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            http://chromium-bsu.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# Do not forget to save LDFLAGS (fixed in upstream autoconf-archive)
Patch0:         ax_check_gl_m4.patch
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils SDL2-devel alsa-lib-devel libvorbis-devel
BuildRequires:  SDL2_image-devel libpng-devel libglpng-devel quesoglc-devel
BuildRequires:  pkgconfig(gl) pkgconfig(glu) openal-soft-devel freealut-devel >= 1.1.0-10
BuildRequires:  libappstream-glib gettext
BuildRequires:  make autoconf automake gettext-devel
Requires:       hicolor-icon-theme

%description
You are captain of the cargo ship Chromium B.S.U., responsible for delivering
supplies to our troops on the front line. Your ship has a small fleet of
robotic fighters which you control from the relative safety of the Chromium
vessel. This is an OpenGL-based shoot 'em up game with fine graphics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# https://www.gnu.org/software/gettext/manual/html_node/autopoint-Invocation.html
sed -i -e 's|AM_GNU_GETTEXT_VERSION|AM_GNU_GETTEXT_REQUIRE_VERSION|' configure.ac
autoreconf -fiv

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
cp -a AUTHORS README NEWS $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz

%changelog
%autochangelog
