%global source0_hash 4057f526b292a9fc7731c551f7aabbec41b9e0b5f044db13fe8f2a9ae69c087f
%global git_commit 29590a6719c725bc95730e72213a00ef92cfa489
%global git_date 20250901
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:		morserunner
Version:	1.68z^%{git_suffix}
Release:        2%{?dist}
Summary:        Amateur radio morse code contest simulator
License:	MPL-2.0
URL:		https://github.com/zmetzing/MorseRunner
Source0:        https://github.com/zmetzing/MorseRunner/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:	morserunner.desktop
Source2:	LICENSE.md
Requires:	hicolor-icon-theme
ExcludeArch:	s390x
Patch:		morserunner-1.68z-linux-dirs.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-tools
BuildRequires:  make
BuildRequires:  sdl12-compat-devel
# /oreon:deps
%description
Amateur radio morse code contest simulator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MorseRunner-%{git_commit}

cp %{SOURCE2} .

# Fix line endings
dos2unix *.{pas,dpr,lpr,txt,dfm,lfm} VCL/*.pas

%autopatch -p1

%build

%make_build
convert -set filename:dim '%%wx%%h' ./MorseRunner.ico morserunner-%%[filename:dim].png
for res in 16 32
do
  mkdir -p hicolor/${res}x${res}/apps
  cp morserunner-${res}x${res}.png hicolor/${res}x${res}/apps/morserunner.png
done
rm morserunner-*.png
%install
install -Dpm755 lib/*/MorseRunner %{buildroot}%{_bindir}/MorseRunner
install -Dpm644 Master.dta %{buildroot}%{_datadir}/morserunner/Master.dta
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
cp -r hicolor/* %{buildroot}%{_datadir}/icons/hicolor/
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
