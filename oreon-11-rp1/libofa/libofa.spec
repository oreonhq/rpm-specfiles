%global source0_hash 0216466153e92058c5202dea03390ddc7601d916b983f71ce4f4d034405590a0

# Fedora Review: http://bugzilla.redhat.com/204954

Summary: 	Open Fingerprint Architecture library	
Name:		libofa	
Version:	0.9.3	
Release:	53%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Url:		http://code.google.com/p/musicip-libofa/
Source0:	http://musicip-libofa.googlecode.com/files/libofa-%{version}.tar.gz	

Patch1: libofa-0.9.3-gcc41.patch
# Use Libs.private
Patch2: libofa-0.9.3-pkgconfig.patch
Patch3: libofa-0.9.3-gcc44.patch
Patch4: libofa-0.9.3-curl.patch
Patch5: libofa-0.9.3-gcc47.patch
Patch6: libofa-configure-c99.patch

BuildRequires:	findutils
BuildRequires:  gcc-c++
BuildRequires:	pkgconfig sed
BuildRequires:	fftw3-devel 
# these are used only in the examples.
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires: make

%description
Currently, MusicDNS and the Open Fingerprint Architecture are being used to:
* identify duplicate tracks, even when the metadata is different, MusicIP
  identifies the master recording.
* fix metadata
* find out more about tracks by connecting to MusicBrainz

%package devel
Summary: Development headers and libraries for %{name}	
Requires: %{name}%{?_isa} = %{version}-%{release}
# removed by patch2
#Requires: expat-devel fftw3-devel 
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

find . -name README -or -name \*.cpp -or -name \*.h | xargs --no-run-if-empty sed -i -e 's|\r||'  ||:

%patch -P1 -p1 -b .gcc41
%patch -P2 -p1 -b .pkgconfig
%patch -P3 -p1 -b .gcc43
%patch -P4 -p1 -b .curl
%patch -P5 -p1 -b .gcc47
%patch -P6 -p1 -b .configure-c99

## pkg-config < 0.20.0 (apparently?) doesn't grok URL
%if "%(pkg-config --version 2>/dev/null)" < "0.20.0"
#if 0%{?fedora} < 4 && 0%{?rhel} < 5
#if 0%{?rhel} == 4
sed -i -e "s|^URL:|#URL:|" *.pc.in ||:
%endif

%build
%configure --disable-static

%make_build

%install
%make_install

# unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la

# prepare docs
make -C examples clean
rm -rf examples/.deps examples/Makefile examples/*.gcc43

%ldconfig_scriptlets

%files 
%doc AUTHORS README
%license COPYING
%{_libdir}/libofa.so.0*

%files devel
%doc examples/
%{_includedir}/ofa1/
%{_libdir}/pkgconfig/libofa.pc
%{_libdir}/libofa.so

%changelog
%autochangelog
