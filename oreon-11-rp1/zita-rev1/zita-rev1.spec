%global source0_hash 2776309fab02f0f0c6a3944745ab4a3c8a97044af60ce1d4cdcba38a1d088c4d
Summary:        Pro-audio reverb for JACK
Name:          zita-rev1
Version:       0.2.2
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       zita-rev1.desktop
Patch0:        zita-rev1-fsf-address.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXft-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
%{name} is a reworked version of the reverb originally developed for Aeolus. 
Its character is more 'hall' than 'plate', but it can be used on a wide 
variety of instruments or voices. 
It is not a spatialiser - the early reflections are different for the L and R 
inputs, but do not correspond to any real room. They have been tuned to match 
left and right sources to some extent.

In Stereo mode a dry/wet mix control is provided, so it can be used either as
an insert or in send/return mode. For mono just connect one of the two 
channels.

In Ambisonic mode (selected by the -B command line option) the only option is 
the send/return mode. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# use Fedora build flags
sed -e '/^CXXFLAGS += -march=native/d' -i source/Makefile

%build

%set_build_flags
cd source
%make_build PREFIX=%{_prefix}
%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_lib} install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
