%global source0_hash a984177338127520063628ca38bf430d8fb62ade77b6064a834df23e6ef78786

Name:		naturette
Version:	1.3
Release:	34%{?dist}
Summary:	An AGI adventure game

License:	CC-BY-ND-4.0
URL:		http://membres.lycos.fr/agisite/rette.htm
Source0:	rette13e.zip
#Original from http://membres.lycos.fr/agisite/rette13e.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	naturette.desktop
Source2:	naturette-wrapper.sh
Source3:	naturette.xpm
Source4:	naturette-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, hicolor-icon-theme

%description
Naturette was made using AgiStudio. Naturette must find eight 
diamonds to go back to her house. Contains nude scenes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

#drop case
mv LOGDIR logdir
mv OBJECT object
mv PICDIR picdir
mv SNDDIR snddir
mv VIEWDIR viewdir
mv VOL.0 vol.0
mv WORDS.TOK words.tok

#char fix
sed -i 's/\r//' Readme.txt

%build
cp %{SOURCE4} .

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p logdir naturette-LICENSE.fedora object picdir snddir viewdir vol.0 words.tok $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc Readme.txt naturette-LICENSE.fedora
%{_datadir}/naturette
%{_datadir}/applications/naturette.desktop
%{_datadir}/icons/hicolor/32x32/apps/naturette.xpm
%{_bindir}/naturette-wrapper.sh

%changelog
%autochangelog
