%global source0_hash c8e6898773e8752dc339d6e052fc2d0281ba9e0c7ea89ee05bb32c6fad0ae538

# This package seems to have weird parallelism build bugs so...
%global smp_mflags -j16

Name:		rocksndiamonds
Version:	4.4.1.3
Release:	1%{?dist}
License:	GPL-1.0-or-later
Summary:	Underground digging game
URL:		http://www.artsoft.org/rocksndiamonds/
# We no longer have legal issues with the bundled copy of libsmpeg2, but we don't use it either
# so we just delete it along with the other prebuilt libs in prep
Source0:	https://www.artsoft.org/RELEASES/linux/rocksndiamonds/rocksndiamonds-%{version}-linux.tar.gz
Source1:	rocksndiamonds.desktop
Source2:	rocksndiamonds.png
# Additional music files we have permission for!
Source3:	rocksndiamonds-distributable-music.tar.bz2
Patch3:		rocksndiamonds-4.4.0.4-music-info-url.patch
Patch4:		rocksndiamonds-4.4.1.0-strncpy-specified-bound-1024-equals-destination-size.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	SDL2-devel, libX11-devel, desktop-file-utils, xorg-x11-proto-devel
BuildRequires:	SDL2_image-devel, SDL2_mixer-devel, SDL2_net-devel, zlib-devel
Requires:	libmodplug%{_isa}
Requires:	libxmp%{_isa}

%description
Dig for treasure and solve puzzles underground, but watch out for falling
rocks and strange creatures!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 3
%patch -P3 -p1 -b .url
%patch -P4 -p1 -b .fix

# Stawp!
rm -rf lib/*

%build
make %{?_smp_mflags} BASE_PATH=%{_datadir}/%{name}/ RW_GAME_DIR=%{_localstatedir}/games/%{name}/ EXTRA_CFLAGS="$RPM_OPT_FLAGS -DUSE_USERDATADIR_FOR_COMMONDATA"

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 rocksndiamonds $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/scores
for i in graphics levels music sounds; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/%{name}/
done
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Get rid of unnecessary patch files.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/Tutorials/*/*.orig $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/Tutorials/*/tapes/*.orig

desktop-file-install 				\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications	\
  --mode 0644					\
  %{SOURCE1}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Your Name <email@address.com> -->
<!--
BugReportURL: waiting for admin approval to post
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">rocksndiamonds.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Gem collecting puzzle game</summary>
  <description>
    <p>
      Rocks 'n' Diamonds is a action puzzle game where you have to navigate a maze
      of dirt, rocks, enemies and quicksand, while collecting gems and making it
      safely to the exit.
      Be careful not to get crushed by falling rocks or killed by an enemy.
    </p>
  </description>
  <url type="homepage">http://www.artsoft.org/rocksndiamonds/</url>
  <screenshots>
    <screenshot type="default">http://www.artsoft.org/rocksndiamonds/screenshots/emeraldmine.gif</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc ChangeLog COPYING CREDITS INSTALL
%doc docs/elements/
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_localstatedir}/games/%{name}/

%changelog
%autochangelog
