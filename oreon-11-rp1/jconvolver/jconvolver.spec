%global source0_hash e88cc61b792a7497544aa227861d38a39ac465021a793ba004dbbfbace8abbd3

Summary:       Real-time Convolution Engine
Name:          jconvolver
Version:       1.0.3
Release:       17%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/linuxaudio/index.html
Source0:       https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Demo reverbs
# Don't bundle until license is cleared up
#Source1:      https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-reverbs.tar.bz2

Obsoletes:     jace <= 0.2.0
Provides:      jace = %{version}-%{release}
Obsoletes:     jconv <= 0.8.1
Provides:      jconv = %{version}-%{release}

BuildRequires: clthreads-devel >= 2.4.0
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-convolver-devel >= 4.0.0
BuildRequires: make

Requires: zita-convolver >= 4.0.0

%description
Jconvolver is a real-time convolution engine. It can execute up to a 64 by 64
convolution matrix (i.e. 4096 simultaneous convolutions) as long as your CPU(s)
can handle the load. It is designed to be efficient also for sparse (e.g.
diagonal) matrices. Unused matrix elements do not take any CPY time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#setup -q -a 1
%setup -q

# fix paths of configuration files
find config-files/ -name \*.conf \
  -exec sed -i -e "s|/audio/reverbs|%{_datadir}/%{name}/reverbs|g" {} \; \
  -exec sed -i -e "s|^#/cd |/cd |g" {} \;

# Force Fedora's flags
sed -i -e '/^CXXFLAGS += -march=native/d' source/Makefile

# Preserve timestamps
sed -i 's|install |install -p |' source/Makefile

%build
%set_build_flags
%make_build PREFIX=%{_prefix} -C source

%install
%make_install PREFIX=%{_prefix} -C source

# install configuration files and demo reverbs
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a config-files/* %{buildroot}%{_datadir}/%{name}
#cp -a reverbs/ %%{buildroot}%%{_datadir}/%%{name}/

%files
%doc AUTHORS README*
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
%autochangelog
