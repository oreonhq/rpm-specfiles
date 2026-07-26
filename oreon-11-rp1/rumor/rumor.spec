%global source0_hash f43565ea58c0c208c29bdf4d8e8a8835a8d4429b01444c580a22d62dfdef2cde

Name:		 rumor
Version:	 1.0.5
Release:	 35%{?dist}
Summary:	 Really Unintelligent Music transcriptOR 
License:	 GPL-2.0-or-later
URL:		 http://launchpad.net/rumor
Source0:	 http://launchpad.net/rumor/trunk/%{version}/+download/rumor-%{version}.tar.bz2
Patch0:	 rumor-gcc60.patch

BuildRequires: make
BuildRequires:	 alsa-lib-devel
BuildRequires:	 gcc-c++
BuildRequires:	 guile-devel
BuildRequires:   automake, autoconf, texinfo

%description
Rumor is a realtime monophonic (with chords) MIDI keyboard to Lilypond 
converter. It receives MIDI events, quantizes them according to its metronome
on the fly and outputs handwritten-like corresponding Lilypond notation. Tempo,
meter, key and other parameters can be set via command-line options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0

./autogen.sh
# Impose optflags
sed -i 's|-O0||' configure

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
# Remove unwanted file:
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_infodir}/%{name}.info*

%changelog
%autochangelog
