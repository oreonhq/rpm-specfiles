%global source0_hash f15f90133ab424c59dcdb5032c83d6a07c658ab9fd8132c3ef22b39dd354408a
%global git_commit c3ff82b00fad81eea1622faf2d36f55710231ad3
%global git_date 20250610
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
%global features \\\
  GPIO_INCLUDE= \\\
  LOCALCW_INCLUDE=LOCALCW \\\
  SOAPYSDR_INCLUDE=SOAPYSDR \\\
  MIDI_INCLUDE=MIDI \\\
  PTT_INCLUDE=PTT \\\
Name:		pihpsdr
Version:	2.0.8~rc1^%{git_suffix}
Release:        1%{?dist}
Summary:        Raspberry Pi standalone code for HPSDR
License:	GPL-2.0-or-later
URL:		https://github.com/g0orx/%{name}
Source0:        https://github.com/g0orx/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:	pihpsdr.desktop
Source2:	io.github.g0orx.pihpsdr.metainfo.xml
%ifnarch s390x
%endif
Requires:	hicolor-icon-theme
Patch:		pihpsdr-2.0.8-distro-makefile.patch
Patch:		pihpsdr-2.0.8-compile-fix.patch
Patch:		pihpsdr-2.0.8-wdsp-in-home-dir.patch
Patch:		pihpsdr-2.0.8-icon-system-path.patch
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libi2c-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  wdsp-devel
# /oreon:deps
%description
The pihpsdr (Pi High Performance Software Defined Radio) is a port of PowerSDR
which works with the radios based on the OpenHPSDR project. These radios use
Ethernet to communicate with the software.

%package doc
Summary:	Documentation files for linhpsdr
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation files for linhpsdr.

%prep

%autosetup -n %{name}-%{git_commit} -T -b0 -p1

# drop binaries, save useful files
mv release/documentation .
pushd release/pihpsdr
mv -t ../.. hpsdr.png hpsdr_icon.png README.MIDI
popd
rm -rf release

%build

%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{features}
%install
%make_install BINDIR="%{buildroot}%{_bindir}" DATADIR="%{buildroot}%{_datadir}" %{features}
install -Dpm 0644 hpsdr.png %{buildroot}%{_datadir}/%{name}/hpsdr.png
install -Dpm 0644 hpsdr_icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/hpsdr_icon.png
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dm 0644 %{SOURCE2} \
    %{buildroot}%{_metainfodir}/io.github.g0orx.pihpsdr.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pihpsdr-doc -f %{oreon_filedir}/pihpsdr-doc.list

%changelog

%autochangelog
