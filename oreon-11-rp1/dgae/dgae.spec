%global source0_hash 17fd98feabba8f16fd3f1cb1617fa95e98a5f73fd6715362fd8664e59befcaa7

Name:		dgae
Version:	1.1
Release:	37%{?dist}
Summary:	DG, a short AGI adventure game

License:	LicenseRef-Fedora-Public-Domain
URL:		http://membres.lycos.fr/agisite/agisite.htm
Source0:	dgae.zip
#Original from http://membres.lycos.fr/agisite/dgae.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content, running dos2unix on the text file, and changing
#all filenames to lowercase for agistudio compatibility.
Source1:	dgae.desktop
Source2:	dgae-wrapper.sh
Source3:	dgae.xpm
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, hicolor-icon-theme

%description
Help DG to seek out his twin brother's stick.
This game is a public domain: you can look out the codes and make your own
AGI game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
iconv -f IBM850 -t UTF8 readme.txt > readme.txt.tmp
mv readme.txt.tmp readme.txt

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p logdir object picdir readme.txt snddir viewdir vol.0 words.tok $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc readme.txt
%{_datadir}/dgae
%{_datadir}/applications/dgae.desktop
%{_datadir}/icons/hicolor/32x32/apps/dgae.xpm
%{_bindir}/dgae-wrapper.sh

%changelog
%autochangelog
