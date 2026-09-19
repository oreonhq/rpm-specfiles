%global source0_hash e50495d292a1d456c28044efbf07c16d8865f8d95e1caba86f4c5b2e3fb1d28f

Name:           gemdropx
Version:        0.9
Release:        39%{?dist}
Summary:        Falling blocks puzzlegame
License:        GPL-1.0-or-later
URL:            http://www.newbreedsoftware.com/gemdropx
Source0:        ftp://ftp.billsgames.com/unix/x/%{name}/src/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel ImageMagick desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Gem Drop X is a fast-paced puzzle game where it is your job to clear
the screen of gems before they squash you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv data/sounds/README README-sounds.txt
mv data/images/README README-images.txt

%build
make XTRA_FLAGS="$RPM_OPT_FLAGS" DATA_PREFIX=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
# Makefile always wants to install under /usr/local, so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 data/images/*.bmp $RPM_BUILD_ROOT%{_datadir}/%{name}/images
cp -a data/sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
 
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
convert data/images/%{name}-icon.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc README*.txt COPYING.txt AUTHORS.txt CHANGES.txt TODO.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
%autochangelog
