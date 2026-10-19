%global source0_hash ac5a11372d7325929c86966c7d2288a9276e65c43b29a50017c37a5e660ed80d
Summary:        Real-time Convolution Engine
Name:          jconvolver
Version:       1.1.0
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/linuxaudio/index.html
Source0:        https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Obsoletes:     jace <= 0.2.0
Provides:      jace = %{version}-%{release}
Obsoletes:     jconv <= 0.8.1
Provides:      jconv = %{version}-%{release}
Requires: zita-convolver >= 4.0.0
# oreon:deps
BuildRequires:  clthreads-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  zita-convolver-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a config-files/* %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
