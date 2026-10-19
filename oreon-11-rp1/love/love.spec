%global source0_hash 6f55c265be5e03696c4770150c4388f5cffbdb3727606724cf88332baab429f7
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
%global luadep luajit
%else
%global luadep lua
%endif
Name:           love
Version:        11.5
Release:        1%{?dist}
Summary:        A free 2D game engine which enables easy game creation in Lua
License:        Zlib
URL:            http://love2d.org
Source0:        https://github.com/love2d/love/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Provides: bundled(Box2D) = 2.3.0
Provides: bundled(enet) = 1.3.13
Provides: bundled(luasocket) = 3.0
Provides: bundled(lz4) = 1.8.0
Provides: bundled(physfs) = 3.0.1
ExcludeArch:    ppc ppc64 s390x
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  mesa-libGL
BuildRequires:  mpg123-devel
BuildRequires:  openal-soft-devel
# /oreon:deps
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
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_libdir}/lib%{name}.la
%ldconfig_scriptlets
%ldconfig_scriptlets -n lib%{name}
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liblove -f %{oreon_filedir}/liblove.list

%changelog

%autochangelog
