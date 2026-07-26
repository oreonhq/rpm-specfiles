%global source0_hash none

Name:           boswars
Version:        2.8
Release:        %autorelease
Summary:        Bos Wars is a futuristic real-time strategy game
License:        GPL-2.0-only
URL:            https://www.boswars.org/
Source0:        https://www.boswars.org/dist/releases/boswars-2.8-src.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-48.png
Source3:        %{name}-128.png
Source4:        %{name}.appdata.xml
Source5:        %{name}.6
Patch1:		boswars-0001-Convert-to-UTF-8.patch
Patch2:		boswars-0002-fabricate.py-remove-deprecated-calls-to-os.stat_floa.patch
Patch3:		boswars-0003-build-detect-alternative-name-for-Lua-5.1-libs.patch
BuildRequires:	SDL-devel
BuildRequires:	compat-lua-devel
#BuildRequires:	compat-tolua++-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libGL-devel
BuildRequires:	libappstream-glib
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python3
Requires:       hicolor-icon-theme
Provides:	bundled(guichan)
Provides:	bundled(tolua++)

%description
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.

%prep
%autosetup -p1 -n %{name}-%{version}-src
sed -i -e "s|-Wall -fsigned-char -D_GNU_SOURCE=1 -D_REENTRANT|%{optflags}|g" make.py
find campaigns engine maps -type f -executable -exec chmod -x {} ';'
# FIXME we want to use the system version of compat-tolua++
# rm engine/tolua/*.h engine/tolua/tolua_*.cpp

%build
/usr/bin/python3 make.py

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/languages
install -D -p -m 755 fbuild/release/boswars %{buildroot}%{_bindir}/%{name}
install -p -m 644 languages/*.po languages/*.pot \
  %{buildroot}%{_datadir}/%{name}/languages
cp -a campaigns graphics intro maps scripts sounds units patches \
  %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -D -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -D -p -m 644 %{SOURCE5} %{buildroot}%{_mandir}/man6/%{name}.6

%files
%doc README.txt CHANGELOG doc/*.html
%license COPYRIGHT.txt LICENSE.txt doc/guichan-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
