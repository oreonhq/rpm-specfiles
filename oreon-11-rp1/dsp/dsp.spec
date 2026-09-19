%global source0_hash 0e98b9aea613b111c9d7cc2b9a0ce14c2b3ba4e90861b3cdcfcb8ec1ebfcab93

Name:           dsp
Version:        1.9
Release:        7%{?dist}
Summary:        An audio processing program with an interactive mode

# Everything is ISC
License:        ISC
URL:            https://github.com/bmc0/dsp
Source0:        https://github.com/bmc0/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  ladspa-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zita-convolver-devel
BuildRequires:  make

%description
dsp is an audio processing program with an interactive mode.

%package -n ladspa-dsp-plugin
Summary:        dsp's LADSPA frontend

Requires:       ladspa

%description -n ladspa-dsp-plugin
dsp's LADSPA frontend.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./configure --libdir=/%{_lib} --disable-ffmpeg

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n ladspa-dsp-plugin
%license LICENSE
%doc README.md
%{_libdir}/ladspa/ladspa_dsp.so

%changelog
%autochangelog
