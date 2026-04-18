Name:           oreon-plasmaconfig
Version:        11
Release:        2%{?dist}
Summary:        Oreon Plasma look-and-feel package

License:        GPLv2+
URL:            https://oreonproject.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        kdeglobals
BuildArch:      noarch

Requires:       plasma-workspace
# Pull common ISO leaves the live compose solver drops (anaconda-dnf-problems.log).
Requires:       libvpx
Requires:       openal-soft
Requires:       librsvg2
Requires:       libaom
Requires:       faad2
Requires:       liblc3
Requires:       libvpl
Requires:       webrtc-audio-processing
Requires:       graphene
Requires:       libcdio-paranoia
Requires:       opencore-amr
Requires:       libshout
Requires:       taglib
Requires:       libv4l
Requires:       kimageannotator-libs
Requires:       dconf
Requires:       poppler-data
Requires:       gpgmepp
Requires:       libXft
Requires:       libqalculate
Requires:       hwdata
Requires:       sound-theme-freedesktop
Requires:       ffmpeg-libs
Requires:       libaccounts-glib
Requires:       graphite2
Requires:       libdisplay-info
Requires:       libseat
Requires:       libXaw
Requires:       fftw-libs
Requires:       speexdsp
Requires:       libtdb
Requires:       soxr
Requires:       rtkit
Requires:       openexr-libs
Requires:       lm_sensors-libs
Requires:       qrencode-libs
Requires:       libdmtx
Requires:       gupnp-igd
Requires:       libxslt
Requires:       adobe-mappings-cmap
Requires:       adobe-mappings-cmap-deprecated
Requires:       adobe-mappings-pdf
Requires:       google-droid-sans-fonts
Requires:       urw-base35-fonts
Requires:       libijs
Requires:       jbig2dec-libs
Requires:       libpaper

%description
Oreon look-and-feel package for KDE Plasma.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel
cp -a org.oreonproject.oreon.desktop %{buildroot}%{_datadir}/plasma/look-and-feel/
install -D -m 0644 kdeglobals %{buildroot}%{_sysconfdir}/xdg/kdeglobals

%files
%{_datadir}/plasma/look-and-feel/org.oreonproject.oreon.desktop
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals

%changelog
* Wed Feb 04 2026 Brandon Lester <blester@oreonhq.com> - 11-1
- Initial package
