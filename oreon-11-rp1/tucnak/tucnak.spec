%global source0_hash 4dd76d7a3ac3d1c31ae093a15dc9e6f2d805fc9ae89b18e87f47b108b164b3ce

Name:		tucnak
Version:	4.71
Release:	1%{?dist}
Summary:	HF/VHF contest logging program
License:	GPL-2.0-only
URL:		http://tucnak.nagano.cz/
Source0:	http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Source1:	cz.nagano.Tucnak.metainfo.xml
ExcludeArch:    i686
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libzia-devel = %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	fftw-devel
BuildRequires:	hamlib-devel
BuildRequires:	rtl-sdr-devel
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel
BuildRequires:	binutils-devel
BuildRequires:	gnutls-devel
# For fixing files encoding
BuildRequires:	recode
Requires:	hicolor-icon-theme
Provides:	tucnak2 = %{version}-%{release}
Obsoletes:	tucnak2 < 2.31-21
# This is to rename soundwrapper from the generic name to the
# tucnak-soundwrapper, it can avoid name conflicts with other
# soundwrappers possibly shipped by other packages in the future.
Patch0:		tucnak-4.18-soundwrapper.patch

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

# temporal LIBS workaround for rhbz#2174841
%if 0%{fedora} > 38
  LIBS="-lsframe"
%else
  LIBS=""
%endif
%make_build LIBS="$LIBS"

%install
%make_install

# Install icon
install -D -p -m644 data/tucnak64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install AppStream metainfo file
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml

# rename soundwrapper to tucnak-soundwrapper
mv %{buildroot}%{_bindir}/soundwrapper %{buildroot}%{_bindir}/tucnak-soundwrapper 

# drop docs installed to wrong place
rm -f %{buildroot}%{_datadir}/tucnak/doc/*
rmdir %{buildroot}%{_datadir}/tucnak/doc

# drop unneeded files/dirs
rm -f %{buildroot}%{_prefix}/lib/tucnak/tucnak.d
rmdir %{buildroot}%{_prefix}/lib/tucnak

%files
%license COPYING
%doc AUTHORS ChangeLog TODO
%doc doc/NAVOD.pdf doc/NAVOD.sxw
%doc data/*.html data/*.png
%{_bindir}/tucnak
%{_bindir}/tucnak-soundwrapper
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/*
%{_metainfodir}/cz.nagano.Tucnak.metainfo.xml
%{_datadir}/%{name}

%changelog
%autochangelog
