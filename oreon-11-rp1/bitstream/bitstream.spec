%global source0_hash dea67a9dca7eda0d72017359c8d649bd5a9d249f9f9a691b8daf739d16798029

Name:           bitstream
Version:        1.6
Release:        %autorelease
Summary:        Simpler access to binary structures such as specified by MPEG, DVB, IETF

License:        MIT
URL:            https://code.videolan.org/videolan/bitstream
Source0:        http://download.videolan.org/pub/videolan/bitstream/%{version}/bitstream-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  make

%description
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.

%package devel
Summary: Simpler access to binary structures such as specified by MPEG, DVB, IETF

%description devel
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
#Nothing to build

%install
%make_install PREFIX=%{_prefix}

%files devel
%doc AUTHORS NEWS README TODO
%license COPYING
%{_includedir}/bitstream
%{_datadir}/pkgconfig/bitstream.pc

%changelog
%autochangelog
