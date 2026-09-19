%global source0_hash 7cf8ff7b6476ef477c42ca558e6329dcc3a641b1d19ccd4de669aa8e41a7b9fc

Name:		sergueis-destiny
Version:	1.1
Release:	35%{?dist}
Summary:	Serguei's Destiny, an AGI adventure game

License:	CC-BY-ND-4.0
URL:		http://membres.lycos.fr/agisite/serguei.htm
Source0:	serguei.zip
#Original from http://membres.lycos.fr/agisite/serguei.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content, running dos2unix on the text file, and changing
#all filenames to lowercase for agistudio compatibility.
Source1:	sergueis-destiny.desktop
Source2:	sergueis-destiny-wrapper.sh
Source3:	sergueis-destiny.xpm
Source4:	sergueis-destiny-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, hicolor-icon-theme

%description
A bad wizard Blackmagic has cast his evil spell to the peaceful village
Jolimy. 50 years later, an apprentice sorcerer Serguei must break the
Blackmagic's spell and free Jolimy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
iconv -f IBM850 -t UTF8 serguei.txt > tmp
mv tmp serguei.txt
cp %{SOURCE4} .

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p logdir object picdir serguei.txt sergueis-destiny-LICENSE.fedora snddir viewdir vol.0 words.tok $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc serguei.txt sergueis-destiny-LICENSE.fedora
%{_datadir}/sergueis-destiny
%{_datadir}/applications/sergueis-destiny.desktop
%{_datadir}/icons/hicolor/32x32/apps/sergueis-destiny.xpm
%{_bindir}/sergueis-destiny-wrapper.sh

%changelog
%autochangelog
