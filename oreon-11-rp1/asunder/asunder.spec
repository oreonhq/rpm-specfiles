%global source0_hash b71341d746ccf56aa77b1785c6af81aa641d084ac3d34b78beb537618848b64b
Name:		asunder
Summary:        A graphical Audio CD ripper and encoder
Version:	3.0.2
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		http://littlesvr.ca/asunder
Source0:        http://littlesvr.ca/asunder/releases/asunder-%{version}.tar.bz2
Requires:	cdparanoia
Requires:	vorbis-tools
Recommends:	lame
Recommends:	flac
Recommends:	opus-tools
Suggests:	wavpack
Suggests:	mppenc
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libcddb-devel
BuildRequires:  make
# /oreon:deps
%description
It allows to save tracks from an Audio CD as WAV, OGG, MP3, OPUS, FLAC,
Wavpack, Musepack and/or Monkey's Audio, AAC (using third-party software).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	--add-category X-AudioVideoImport \
	%{buildroot}%{_datadir}/applications/asunder.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
