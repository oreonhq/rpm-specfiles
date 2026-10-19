%global source0_hash c230ed462c5ed7d7403ceb6984c57c8d05de42386d796bcd893636c0b0ba222f
Name:           libdiscid
Version:        0.7.0
Release:        1%{?dist}
Summary:        C Library for creating MusicBrainz DiscIDs
License:        LGPL-2.1-or-later
URL:            https://musicbrainz.org/doc/libdiscid
Source0:        https://data.metabrainz.org/pub/musicbrainz/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This C library %{name} creates MusicBrainz DiscIDs from audio CDs. It
reads the table of contents (TOC) of a CD and generates an identifier
which can be used to lookup the CD at MusicBrainz. Additionally, it
provides a submission URL for adding the DiscID to the database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries, header files and documentation for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%make_build docs
%check

%make_build check
%install
%make_install
find %{buildroot} -name '*.la' -delete -print
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdiscid-devel -f %{oreon_filedir}/libdiscid-devel.list

%changelog

%autochangelog
