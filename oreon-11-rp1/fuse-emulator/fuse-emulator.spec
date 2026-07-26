%global source0_hash 847f93e2bf4104d54803e3c197066ff3c073c029a017ee68df8eece190b12454

Name:           fuse-emulator
Version:        1.6.0
Release:        14%{?dist}
Summary:        The Free UNIX Spectrum Emulator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fuse-emulator.sourceforge.net
Source0:        fuse-%{version}-noroms.tar.gz
# we use
# this script to remove the roms binary before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh 0.9.0
Source1:        generate-tarball.sh
Source2:        README.z88sdk
Source3:        README_fuseroms.fedora
BuildRequires:  alsa-lib-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libgcrypt-devel >= 1.1.42
BuildRequires:  libICE-devel
BuildRequires:  libpng-devel
BuildRequires:  libspectrum-devel >= 1.4.3
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  SDL2-devel
BuildRequires:  perl
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Fuse is a spectrum emulator which emulates multiple models, including the 16K,
48K, 128K, +2, +2A, +3 and various clones.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn fuse-%{version}

# Filter unwanted dependency in the debuginfo rpm
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
    sed -e '/perl(Fuse)/d' | \
    sed -e '/perl(strict)/d' | \
    sed -e '/perl(lib)/d'
EOF

%define __perl_requires %{_builddir}/fuse-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
%configure --enable-desktop-integration
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -pm0644 %{SOURCE2} .
install -pm0644 %{SOURCE3} .

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/fuse.desktop

%files
%{_mandir}/man1/fuse.1.gz
%{_bindir}/fuse
%{_datadir}/fuse
%{_datadir}/applications/fuse.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-spectrum.png
%{_datadir}/icons/hicolor/*/apps/fuse.png
%{_datadir}/mime/packages/fuse.xml
%doc AUTHORS ChangeLog COPYING README THANKS README.z88sdk README_fuseroms.fedora

%changelog
%autochangelog
