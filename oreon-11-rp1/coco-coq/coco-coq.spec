%global source0_hash 0732caf79c7d9b0333a8b1779256e4dfc1aada7dad062d14df8276222f17651d

Name:		coco-coq
Version:	0.1
Release:	36%{?dist}
Summary:	Coco Coq in Grostesteing's base, an AGI adventure game

License:	CC-BY-ND-4.0
URL:		http://membres.lycos.fr/agisite/coco-c.htm
Source0:	cococe.zip
#Original from http://membres.lycos.fr/agisite/cococe.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	coco-coq.desktop
Source2:	coco-coq-wrapper.sh
Source3:	coco-coq.xpm
Source4:	coco-coq-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, hicolor-icon-theme

%description
Grostesteing is back for troubles: he's kidnapped the Coco Coq's friends
to turn them into monsters. Coco must go inside the deadly base, avoids 
traps, free his friends and beat the bad scientist Grostesteing.

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

%build
cp %{SOURCE4} .

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p coco-coq-LICENSE.fedora logdir object picdir snddir viewdir vol.0 words.tok $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc coco-coq-LICENSE.fedora
%{_datadir}/coco-coq
%{_datadir}/applications/coco-coq.desktop
%{_datadir}/icons/hicolor/32x32/apps/coco-coq.xpm
%{_bindir}/coco-coq-wrapper.sh

%changelog
%autochangelog
