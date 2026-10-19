%global source0_hash 380fd023cd6933b42d51b574a03c13cf8aa5ed6dd21f7e298c94dd9c3555a175
Name:		tucnak
Version:	4.74
Release:        1%{?dist}
Summary:        HF/VHF contest logging program
License:	GPL-2.0-only
URL:		http://tucnak.nagano.cz/
Source0:        http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Source1:	cz.nagano.Tucnak.metainfo.xml
ExcludeArch:    i686
Requires:	hicolor-icon-theme
Provides:	tucnak2 = %{version}-%{release}
Obsoletes:	tucnak2 < 2.31-21
Patch0:		tucnak-4.18-soundwrapper.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  hamlib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libsndfile-devel
BuildRequires:  libzia-devel
BuildRequires:  make
BuildRequires:  portaudio-devel
BuildRequires:  recode
BuildRequires:  rtl-sdr-devel
# /oreon:deps
%description
Tucnak is HF/VHF/UHF/SHF log for hamradio contests. It supports multi
bands, free input, networking, voice and CW keyer, WWL database and
much more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix encoding to UTF-8
recode ISO-8859-2..UTF-8 AUTHORS ChangeLog

%build

autoreconf -fi
%configure
  LIBS=""
%make_build LIBS="$LIBS"
%install
%make_install
install -D -p -m644 data/tucnak64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml
mv %{buildroot}%{_bindir}/soundwrapper %{buildroot}%{_bindir}/tucnak-soundwrapper 
rm -f %{buildroot}%{_datadir}/tucnak/doc/*
rmdir %{buildroot}%{_datadir}/tucnak/doc
rm -f %{buildroot}%{_prefix}/lib/tucnak/tucnak.d
rmdir %{buildroot}%{_prefix}/lib/tucnak
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
