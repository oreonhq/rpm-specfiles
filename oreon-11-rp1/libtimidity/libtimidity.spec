%global source0_hash 26447cbc049fb262e26b640e42c063e8694133aa92ff145e0d0b15a03a352e6a
%global libname timidity
Name:           lib%{libname}
Version:        0.2.7
Release:        1%{?dist}
Summary:        MIDI to WAVE converter library
License:        LGPL-2.1-or-later
URL:            http://libtimidity.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       timidity++-patches
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libao-devel
BuildRequires:  make
# /oreon:deps
%description
This library is based on the TiMidity decoder from SDL_sound library.
Purpose to create this library is to avoid unnecessary dependences.
SDL_sound requires SDL and some other libraries, that not needed to
process MIDI files. In addition libtimidity provides more suitable
API to work with MIDI songs, it enables to specify full path to the
timidity configuration file, and have function to retrieve meta data
from MIDI song.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
rm -vf %{buildroot}%{_libdir}/%{name}.la
%if 0%{?el7}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n libtimidity-devel -f %{oreon_filedir}/libtimidity-devel.list

%changelog

%autochangelog
