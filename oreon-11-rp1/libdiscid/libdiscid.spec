%global source0_hash 72dbb493e07336418fe2056f0ebc7ce544eedb500bb896cc1cc04bd078c2d530

Name:           libdiscid
Version:        0.6.5
Release:        2%{?dist}
Summary:        C Library for creating MusicBrainz DiscIDs

License:        LGPL-2.1-or-later
URL:            https://musicbrainz.org/doc/libdiscid
Source0:        https://data.metabrainz.org/pub/musicbrainz/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make

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

%autosetup -p1

%build
%configure --disable-static
%make_build
%make_build docs

%check
%make_build check

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%doc docs/*
%{_includedir}/discid/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
