%global source0_hash 3f18c5d059517aa62c155f3b0e647eec57325b9aae1b1e1a560b6dae0cb8cfae

%global commit c0abd473857106cd13459fe04f4444099e0d0b59
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           numptyphysics
# Last known version number
Version:        0.4
Release:        0.34.20151231git%{shortcommit}%{?dist}
Summary:        A crayon-drawing based physics puzzle game 

License:        GPL-3.0-or-later
URL:            http://thp.io/2015/numptyphysics/
Source0:        https://github.com/thp/numptyphysics/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/thp/numptyphysics/pull/17.patch#/%{name}-qsort.patch
Patch1:         include.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Provides:       bundled(Box2D) = 2.0.1
ExcludeArch:    ppc64le

%description
Harness gravity with your crayon and set about creating blocks, ramps,
levers, pulleys and whatever else you fancy to get the little red thing to
the little yellow thing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/numptyphysics.desktop

%files
%{_bindir}/numptyphysics
%{_datadir}/numptyphysics
%{_datadir}/applications/numptyphysics.desktop
%{_datadir}/icons/hicolor/256x256/apps/numptyphysics.png
%{_mandir}/man6/numptyphysics.6*

%changelog
%autochangelog
