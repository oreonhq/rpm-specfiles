%global source0_hash 47ef9e527681c8fb5930fdd3620606218310c6831e7ea09ada0bb5b3c2df04c8
%global git_commit 87a629072b8375ee7ce586f4cd30ac0cb352593a
%global git_date 20250610
%global version_tag Beta
%global version_date 2021-02-25
%global features \\\
  SOAPYSDR_INCLUDE=SOAPYSDR
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:		linhpsdr
Version:	0
Release:        1%{?dist}
Summary:        An HPSDR application for Linux
License:	GPL-2.0-or-later
URL:		https://github.com/g0orx/%{name}
Source0:        https://github.com/g%{version}orx/%{name}/archive/%{git_commit}/%{name}-%{git_date}git%{git_short_commit}.tar.gz
Source1:	io.github.g0orx.LinHPSDR.metainfo.xml
Requires:	hicolor-icon-theme
Patch:		linhpsdr-0-distro-makefile.patch
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libsoundio-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  unixcw-devel
BuildRequires:  wdsp-devel
# /oreon:deps
%description
An HPSDR (High Performance Software Defined Radio) application for controlling
HPSDR compatible radios, e.g. Orion, Angelia, Hermes, ...

%package doc
Summary:	Documentation files for linhpsdr
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation files for linhpsdr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{git_commit} -p1

%build

%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
  GIT_VERSION="%{version_tag}" GIT_DATE="%{version_date}" %{features}
%install
%make_install BINDIR="%{buildroot}%{_bindir}" DATADIR="%{buildroot}%{_datadir}" %{features}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/io.github.g0orx.LinHPSDR.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n linhpsdr-doc -f %{oreon_filedir}/linhpsdr-doc.list

%changelog

%autochangelog
