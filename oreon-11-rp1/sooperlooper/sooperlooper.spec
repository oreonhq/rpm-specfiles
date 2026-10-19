%global source0_hash 7d8f57a325bf2d1ead680c83f1d23e35a4ec748e81e7f962d02a7fa35f7da9f6
%global build_type_safety_c 0
Summary:        Realtime software looping sampler
Name: sooperlooper
Version: 1.7.9
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://sonosaurus.com/sooperlooper/
Source0:        https://github.com/essej/sooperlooper/archive/v1.7.9/%{name}-%{version}.tar.gz
Source1: sooperlooper.png
Source2: sooperlooper.desktop
Source3: sooperlooper.appdata.xml
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  liblo-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  rubberband-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
SooperLooper is a realtime software looping sampler in the spirit of
Gibson's Echoplex Digital Pro. If used with a low-latency kernel and
the proper audio buffer configuration it is capable of truly realtime
live looping performance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./autogen.sh
sed -i 's|OPT_FLAGS="$OPT_FLAGS -pipe"|OPT_FLAGS=""|g' configure
sed -i 's|OPT_FLAGS="$OPT_FLAGS -pipe"|OPT_FLAGS="%{optflags}"|g' \
  libs/pbd/configure libs/midi++/configure
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
