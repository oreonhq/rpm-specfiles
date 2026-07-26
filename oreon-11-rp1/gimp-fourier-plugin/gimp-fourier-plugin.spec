%global source0_hash 8406fa49b8d31444b5870063eaf0dbd89b6e909231b3fa57d083c05fd38c134a

Name:           gimp-fourier-plugin
Version:        0.4.5+gimp3rc1
%global srcversion %{gsub %{version} + -}
Release:        %autorelease
Summary:        Do direct and reverse Fourier Transforms on your image

License:        GPL-3.0-or-later
URL:            https://www.lprp.fr/gimp_plugin_en/
%global forgeurl https://github.com/rpeyron/plugin-gimp-fourier
Source:         %{forgeurl}/archive/v%{version}/plugin-gimp-fourier-%{srcversion}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# The gimp package dropped s390x support in
# https://src.fedoraproject.org/rpms/gimp/c/778e871c1051ea063ce679b18ae84f0a3c47b6f7.
# We have asked the maintainer to create a tracking bug.
ExcludeArch:    %{ix86} s390x

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gimp-3.0)

BuildRequires:  dos2unix

# Minimum version for plugin API/ABI compatibility
Requires:       gimp%{?_isa} >= 2:3.0.0~RC1

%description
GIMP Plugin to do forward and reverse Fourier Transform. The major advantage of
this plugin is to be able to work with the transformed image inside GIMP. You
can draw or apply filters in fourier space and get the modified image with an
inverse fourier transform. Useful in fixing moire patterns or fixing some
regular banding noise.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n plugin-gimp-fourier-%{srcversion} -p1
dos2unix --keepdate README.md

%conf
autoreconf --force --install --verbose
%configure --enable-gimp3-fourier

%build
%make_build

%install
%make_install
%find_lang gimp30-fourier

# Upstream provides no tests.

%files -f gimp30-fourier.lang
%license LICENSE
%doc README.md
%doc README.Moire

%{_libdir}/gimp/3.0/plug-ins/fourier

%changelog
%autochangelog
