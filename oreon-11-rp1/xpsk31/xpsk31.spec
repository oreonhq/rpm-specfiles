%global source0_hash 3ac59f04fe694e920c887508d5c1df8006cebac3dc5d27cf869139d9f8c39e70

Name:           xpsk31
Version:        3.6.1
Release:        17%{?dist}
Summary:        GTK+ graphical version of lpsk31 for Ham Radio

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/

Source0:        http://www.5b4az.org/pkg/psk31/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh

Patch0:         xpsk31-1.2-configure.patch
Patch1:         xpsk31-no_home.patch
Patch2:         xpsk31-configure-c99.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils

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

# no upstream .desktop or icon yet
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install %{SOURCE1} --dir=%{buildroot}%{_datadir}/applications/

# Install wrapper to desl with config files needed in $HOME.
install -pm 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS README doc/{*.html,*.pdf}
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
