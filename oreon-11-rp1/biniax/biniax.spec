%global source0_hash 70dcc61a479a393fff63b6cbae39dde49a6670cf564225359d0e3164e06a87c6

Name:		biniax
Version:	1.2
Release:	44%{?dist}
Summary:	A unique arcade logic game

License:	Zlib
URL:		http://www.biniax.com/
Source0:	http://mordred.dir.bg/%{name}/%{name}-src.zip
Source1:	%{name}.desktop
# Icon taken from the source, icon.ico
Source2:	%{name}.png
# Fixes the path in gfx.c, snd.c. and creates a ~/.biniax subdir 
# with "autosave" and "highscore" data. Patches send to upstream!
Patch0:		%{name}-%{version}-gfx.patch
Patch1:		%{name}-%{version}-snd.patch
Patch2:		%{name}-%{version}-save.patch
Patch3:		%{name}-%{version}-optflags.patch
Patch4:		%{name}-%{version}-close.patch

Requires:	hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:	SDL-devel SDL_mixer-devel desktop-file-utils
BuildRequires: make

%description
The gaming field is 5x7 pairs of elements. Every pair consists of two elements 
out of four possible types (colors). Player is a single element, who can move on
empty fields or can take a pair, if the player's element is present in the pair.
If a pair is taken, the player's element is swapped to the other element of the 
pair. The field is scrolling down on time event or after certain moves are spend
(depending on the game mode). Game over is when there is no move for the player.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}
%patch -P0 -p0 -b .gfx
%patch -P1 -p0 -b .snd
%patch -P2 -p0 -b .save
%patch -P3 -p0 -b .optflags
%patch -P4 -p0 -b .close
# Needed because of this rpmlint warning "W: wrong-file-end-of-line-encoding"
sed -i 's/\r//' Readme.txt LICENSE.txt
# Set datadir prefix, snd.patch and gfx.patch
sed -i 's!@DATADIR@!%{_datadir}!' desktop/gfx.c
sed -i 's!@DATADIR@!%{_datadir}!' desktop/snd.c

%build

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/data

install -p -m 755 biniax %{buildroot}%{_bindir}/%{name}
install -p -m 644 data/* %{buildroot}%{_datadir}/%{name}/data/

# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc LICENSE.txt Readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
