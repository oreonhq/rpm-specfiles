%global source0_hash 64bf5c699611dd3fad2e28df2eebd2bf60f6b3b48ce51f84efa92f250ab3cf4a

Name:           linpsk
Version:        1.3.5
Release:        21%{?dist}
Summary:        Psk31 and RTTY program for Linux

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://linpsk.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Add .desktop file
Source1:        %{name}.desktop
# Install wrapper
Source2:        %{name}.sh.in
# Hi-res icon, rhbz#1157554
Source3:        %{name}_64x64.png

# Patch asoundrc file for default sound card (device 0)
Patch0:         linpsk-1.1-3.sound.conf.patch
Patch1:         linpsk-comparison.patch

BuildRequires:  fftw-devel
BuildRequires:  qt-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires: make

#Requires:

# Spelling error in desc. is intentional. Hobby jargon ignore rpmlint warnings.
%description
LinPsk is a program for operating on digital modes running on Linux.
LinPsk supports BPSK, QPSK and RTTY at the moment.
Main features are:
* the simultaneous decoding of up to four channels.
* The different digital modes may be mixed
* You can define a trigger on each channel to be notified if a text of your
  choice is detected.
* You can log each received channel at a file.
* For easy qso'ing you can define macros and for larger texts to be send you
  can use two files.
* You can view the signal as spectrum or in a waterfall display. Both are
  scale-able in the frequency domain.
At the Moment RTTY only supports 45 baud and 1.5 stop-bits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#fix permissions for debuginfo files
chmod 0644 src/{rttydemodulator.cpp,rttydemodulator.h}

%patch -P0 -p1 -b 3.sound.conf
%patch -P1 -p1 -b comparison

%build
%{qmake_qt4} -unix -o Makefile %{name}.pro
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

# Move original binary to libexecdir
mkdir -p %{buildroot}/%{_libexecdir}/
install -m 755 %{name} %{buildroot}%{_libexecdir}/%{name}-bin

# Install wrapper script
install -p -D -m 0755 %{SOURCE2} %{buildroot}/%{_bindir}/%{name}

# Install default sound configuration file
mkdir -p %{buildroot}/%{_sysconfdir}/skel/.%{name}/
install -p -D -m 0644 asoundrc %{buildroot}/%{_sysconfdir}/skel/.%{name}/asoundrc

# Install provided icon
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
# no upstream .desktop
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
# --vendor obsolete per new guidlines but leaving it in because
# this is an existing package with vendor previously installed

#Remove development files
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%config(noreplace) %{_sysconfdir}/skel/.%{name}/asoundrc
%{_libexecdir}/%{name}-bin

%changelog
%autochangelog
