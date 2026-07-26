%global source0_hash 8868e2e1b97b6687c800e7f612262a316bb857edd39883768ce628b6d253376b

Name:		asunder
Summary:	A graphical Audio CD ripper and encoder
Version:	3.0.1
Release:	9%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://littlesvr.ca/asunder
Source0:	http://littlesvr.ca/asunder/releases/asunder-%{version}.tar.bz2
Requires:	cdparanoia
# Supported audio encoders
Requires:	vorbis-tools
Recommends:	lame
Recommends:	flac
Recommends:	opus-tools
# Additional supported audio encoders
Suggests:	wavpack
Suggests:	mppenc
# FDK-AAC encoder is available only in RPM Fusion
#Suggests:	fdkaac
# Monkey’s Audio lossless encoder - available only in RPM Fusion
# (anyway seems to be broken as of Asunder 2.9.2)
#Suggests:	mac

# Versions were taken from the program's website
BuildRequires:	gcc
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool >= 0.34.90
BuildRequires:	make

%description
It allows to save tracks from an Audio CD as WAV, OGG, MP3, OPUS, FLAC,
Wavpack, Musepack and/or Monkey's Audio, AAC (using third-party software).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
	--vendor fedora \
	%endif
	--add-category X-AudioVideoImport \
	%{buildroot}%{_datadir}/applications/asunder.desktop

%files -f %{name}.lang
%{_bindir}/asunder
%doc AUTHORS ChangeLog README TODO NEWS
%license COPYING
%{_datadir}/applications/*asunder.desktop
%{_datadir}/pixmaps/asunder.png
%{_datadir}/pixmaps/asunder.svg

%changelog
%autochangelog
