%global source0_hash 6f55c265be5e03696c4770150c4388f5cffbdb3727606724cf88332baab429f7

# Because of the LuaJIT requirements:
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
%global luadep luajit
%else
%global luadep lua
%endif

Name:           love
Version:        11.5
Release:        7%{?dist}
Summary:        A free 2D game engine which enables easy game creation in Lua

License:        Zlib
URL:            http://love2d.org
Source0:        https://github.com/love2d/love/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  mesa-libGL
BuildRequires:  mpg123-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  %{luadep}-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires: make
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

#The following is bundled.
#Upstream will not unbundle this code as the
#code has been modified to work better with love
#As well, it's not clear if it would be worth unbundling
#See below for the correspondence:
#https://bitbucket.org/rude/love/issues/870/allow-for-shared-version-of-libraries
Provides: bundled(Box2D) = 2.3.0
Provides: bundled(enet) = 1.3.13
#Luasocket 3.0 rc1:
Provides: bundled(luasocket) = 3.0
Provides: bundled(lz4) = 1.8.0
Provides: bundled(physfs) = 3.0.1

#Big endian systems are not yet supported by love 11+
ExcludeArch:    ppc ppc64 s390x

%description
LOVE is an open source, cross platform 2D game engine which uses the
Lua scripting language. LOVE can be used to make games of any license
allowing it to be used for both free and non-free projects.

%package -n lib%{name}
Summary:        Library for Love, A free 2D game engine

%description -n lib%{name}
This package includes the library files for LOVE.
LOVE is an open source, cross platform 2D game engine which uses the
Lua scripting language. LOVE can be used to make games of any license
allowing it to be used for both free and non-free projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#Fixing line encoding:
sed -i 's/\r//' license.txt
#Fixing permissions:
chmod a-x src/libraries/*/*/*/*.* src/libraries/*/*.*

%build
platform/unix/automagic
%configure  --prefix=/usr --with-lua=%{luadep} --enable-static=no
%make_build

%install
%make_install
#Check Desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
#This seems to be built, despite disabling static libraries
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%ldconfig_scriptlets

%ldconfig_scriptlets -n lib%{name}

%files
%doc changes.txt readme.md
%license license.txt
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}-game.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.*

%files -n lib%{name}
%doc changes.txt readme.md
%license license.txt
#Note that liblove.so is just a symlink, so a devel package is useless
%{_libdir}/lib%{name}*.so

%changelog
%autochangelog
