%global source0_hash 19cfcb611991757100ceb8b37b173085fb5cb8d355527a76e4022ebc5ae060e3
Name:           k3guitune
Version:        1.01
Release:        1%{?dist}
Summary:        Musical instrument tuner
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            http://home.planet.nl/~lamer024/k3guitune.html
Source0:        http://home.planet.nl/~lamer024/files/k3guitune-%{version}.tar.gz
Source1:        %{name}.xpm
Patch0:         %{name}-1.01-fix-multiple-parameters-bug.patch
Patch1:         %{name}-desktop-file.patch
Patch2:         %{name}-1.01-fftw.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  bio2jack-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  kdelibs3-devel
BuildRequires:  make
# /oreon:deps
%description
K3Guitune is a guitar-and-other-instruments tuner. It takes a signal from the 
microphone, calculates its frequency, and displays it on a note scale 
graphic and an oscilloscope. It supports normal, Wien, and physical tuning.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix-multiple-parameters-bug
%patch -P1 -p1 -b .desktop-file
%patch -P2 -p1 -b .fftw
%{__rm} -rf po/*.gmo

# fix UTF-8 encodings
for nonutffile in ChangeLog AUTHORS; do
  iconv -f iso8859-1 -t utf-8 $nonutffile > $nonutffile.conv 
  touch -r $nonutffile $nonutffile.conv
  %{__mv} -f $nonutffile.conv $nonutffile
done

# adjustment to allow input via bio2jack
sed -i 's|JACKSoundInput::JACKSoundInput|JACKSoundInput|' k3guitune/soundinput.h

%build

%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}
%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__install} -p -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
desktop-file-install                           \
    --add-category="AudioVideo"                \
    --add-category="Audio"                     \
    --delete-original                          \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applnk/Multimedia/%{name}.desktop
%{__rm} %{buildroot}/%{_docdir}/HTML/*/%{name}/common
cd %{buildroot}/%{_docdir}/HTML/
for lang in *; do
  ln -sf ../common $lang/%{name}/
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
