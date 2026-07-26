%global source0_hash 659c7b5f3f968f386e820cf7387d88c0a61c17dfbdb005bd85f8e93c537e89d6

Name:           penguin-command
Version:        1.6.11
Release:        39%{?dist}
Summary:        Open source arcade game

License:        GPL-2.0-or-later
URL:            http://www.linux-games.com/penguin-command/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.xpm
Source3:        %{name}.desktop
Patch0:         penguin-command-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils,zlib-devel,SDL_mixer-devel,SDL_image-devel
#Requires:       

%description
Penguin Command is a clone of the classic "Missile Command" Game, but it has
better graphics and music. The gameplay has only been slightly modified.
Penguin Command is licensed under the GPL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in penguin-command.ja.6; do
iconv -f eucjp -t utf-8 $f -o $f.back
mv $f.back $f
done

sed -i 's|INSTALL_DATA = @INSTALL_DATA@|INSTALL_DATA = @INSTALL_DATA@ -p|' data/{gfx,sound}/Makefile.in 

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps

desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE3}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
