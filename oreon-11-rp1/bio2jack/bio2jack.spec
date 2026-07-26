%global source0_hash 1695b1713341279b80cb51c7d3d793102c19793546bfff5b73e882f2e5dec9e8

Name:		bio2jack
Version:	0.9
Release:	39%{?dist}
# The license file says GPLv2+ but the source files say LGPLv2+.
# The author of the software confirmed (via email) that it is 
# actually LGPLv2+.
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Summary:	A library for porting blocked io(OSS/ALSA) applications to jack
URL:		http://bio2jack.sourceforge.net/

Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool autoconf automake
BuildRequires: make

%description
Bio (blocked i/o) 2 jack is a library for enabling easy porting of blocked
io(OSS/ALSA) applications to the jack sound server. This library allows the 
person porting the code to simply replace the calls into OSS/ALSA with calls
into interface functions of this library. The library buffers a small amount of
audio data and takes care of the rest of the jack implementation including the
linked list of audio data buffers and the jack callback.

%package devel
Summary:	Development files for %{name}
Requires:	jack-audio-connection-kit-devel
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

# Remove precompiled binaries:
rm -fr .libs *.o

# Screws up the build if left alive
rm -f *.lo

%build
autoreconf -vif
%configure --enable-static=no --enable-shared=yes

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

# Kill libtool archive
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/lib%{name}.so.*

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
