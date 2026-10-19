%global source0_hash 3ac59f04fe694e920c887508d5c1df8006cebac3dc5d27cf869139d9f8c39e70
Name:           xpsk31
Version:        3.6.1
Release:        1%{?dist}
Summary:        GTK+ graphical version of lpsk31 for Ham Radio
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/psk31/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh
Patch0:         xpsk31-1.2-configure.patch
Patch1:         xpsk31-no_home.patch
Patch2:         xpsk31-configure-c99.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
xpsk31 is a GTK+ graphical version of lpsk31, using the same basic signal 
decoding and encoding engine but controlled by the user via the GUI. In 
addition it has a FFT-derived "waterfall" display of the incoming signal and a 
"magniphase" display that shows the magnitude, phase and frequency error of the
psk31 signal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#autoreconf -fiv
./autogen.sh

%build

%configure --program-suffix=.bin
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install %{SOURCE1} --dir=%{buildroot}%{_datadir}/applications/
install -pm 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
