%global source0_hash 19d6dbd9c901c74441d9888c13cb1399f614fe8993d59062a72cfbceb00fed04

Name:           SFML2
Version:        2.6.2
Release:        %autorelease
Summary:        Simple and Fast Multimedia Library, 2.x compatibility version

# Assets used by SFML's example projects.
#
# All assets are under public domain (CC0):
#
# | Name                            | Author                    | Link                       |
# | ------------------------------- | ------------------------- | -------------------------- |
# | Tuffy 1.1 font                  | Thatcher Ulrich           | [Ulrich's fonts][1]        |
# | sounds/resources/doodle_pop.ogg | MrZeusTheCoder            | [public-domain][2]         |
# | tennis/resources/ball.wav       | MrZeusTheCoder            | [public-domain][2]         |
# | opengl/resources/background.jpg | Nidhoggn                  | [Open Game Art][3]         |
# | shader/resources/background.jpg | Arcana Dea                | [Public Domain Images][4]  |
# | shader/resources/devices.png    | Kenny.nl                  | [Game Icons Pack][5]       |
# | sound/resources/ding.flac       | Kenny.nl                  | [Interface Sounds Pack][6] |
# | sound/resources/ding.mp3        | Kenny.nl                  | [Interface Sounds Pack][6] |
# | win32/resources/image1.jpg      | Kenny.nl                  | [Toon Character Pack][7]   |
# | win32/resources/image2.jpg      | Kenny.nl                  | [Toon Character Pack][7]   |
# | sound/resources/killdeer.wav    | US National Park Services | [Bird sounds][8]           |
#
# [1]: http://tulrich.com/fonts/
# [2]: https://github.com/MrZeusTheCoder/public-domain
# [3]: https://opengameart.org/content/backgrounds-3
# [4]: https://www.publicdomainpictures.net/en/view-image.php?image=10979&picture=monarch-butterfly
# [5]: https://www.kenney.nl/assets/game-icons
# [6]: https://www.kenney.nl/assets/interface-sounds
# [7]: https://www.kenney.nl/assets/toon-characters-1
# [8]: https://www.nps.gov/subjects/sound/sounds-killdeer.htm
#
# Apache-2.0:
#   - extlibs/headers/vulkan/
# CC0-1.0:
#   - extlibs/headers/minimp3/
# MIT:
#   - extlibs/headers/glad/include/glad/gl.h
# (MIT AND Apache-2.0):
#   - extlibs/headers/glad/include/glad/egl.h
#
License:        Zlib AND Apache-2.0 AND CC0-1.0 AND MIT AND (MIT AND Apache-2.0) AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sfml-dev.org/
# for SFML 2.6.0 we've removed all the unclear/non-free assets from the source.
# See the asset_licenses.md for more details: https://github.com/SFML/SFML/blob/2.6.1/examples/asset_licenses.md
# And here's the PR that changed (most) of the things: https://github.com/SFML/SFML/pull/1718

Source0:        https://www.sfml-dev.org/files/SFML-%{version}-sources.zip

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  stb_image-devel >= 2.30^20251025gitf1c79c0-2
BuildRequires:  stb_image_write-devel
# BuildRequires:  vulkan-headers

%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
This is the 2.x series kept for applications not yet ported to SFML 3.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that still use the SFML 2.x API.
Headers are in %{_includedir}/SFML2, the CMake config in
%{_libdir}/cmake/SFML2 and pkg-config files in %{_libdir}/SFML2/pkgconfig.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n SFML-%{version} -p1
# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x

# use system-wide extlibs; so, delete everything except glad, minimp3 and vulkan header files
pushd extlibs
shopt -s extglob
rm -r !(headers)
cd headers/
rm -r !(glad|minimp3|vulkan)
shopt -u extglob
popd


%build
%cmake -DSFML_BUILD_DOC=FALSE -DCMAKE_INSTALL_INCLUDEDIR=include/SFML2 -DSFML_MISC_INSTALL_PREFIX=%{_datadir}/doc/SFML2
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_libdir}/cmake/SFML %{buildroot}%{_libdir}/cmake/SFML2
mkdir -p %{buildroot}%{_libdir}/SFML2
mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/SFML2/pkgconfig
sed -i 's|^libdir=.*|libdir=%{_libdir}/SFML2|;s|^includedir=.*|includedir=%{_includedir}/SFML2|' %{buildroot}%{_libdir}/SFML2/pkgconfig/*.pc
for l in %{buildroot}%{_libdir}/libsfml-*.so; do
  ln -s ../$(readlink $l) %{buildroot}%{_libdir}/SFML2/$(basename $l)
  rm $l
done

%files
%doc %{_datadir}/doc/SFML2/readme.md
%license %{_datadir}/doc/SFML2/license.md
%{_libdir}/libsfml-*.so.2*

%files devel
%{_libdir}/cmake/SFML2/
%{_includedir}/SFML2/
%{_libdir}/SFML2/

%changelog
%autochangelog
