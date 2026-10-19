%global source0_hash 028936e9f663c877d6969ad25f145c7b420797e9a3e01c6c184815ed8309f481
Summary:        Web server access log visualizer
Name:          logstalgia
Version:       1.1.5
Release:        1%{?dist}
License:       GPL-3.0-or-later
URL:           https://github.com/acaudwell/Logstalgia
Source0:        https://github.com/acaudwell/Logstalgia/releases/download/logstalgia-%{version}/logstalgia-%{version}.tar.gz
Requires:      gnu-free-mono-fonts
Requires:      gnu-free-serif-fonts
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pcre2-devel
# /oreon:deps
%description
Logstalgia (aka ApachePong) replays or streams a standard website
access log (eg access.log) as a retro arcade game-like simulation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -f -i
%configure \
%ifarch ppc64le
  --with-boost-filesystem=boost_filesystem \
%endif
  --enable-ttf-font-dir=%{_datadir}/fonts/gnu-free/
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
