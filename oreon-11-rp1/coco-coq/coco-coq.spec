%global source0_hash 0732caf79c7d9b0333a8b1779256e4dfc1aada7dad062d14df8276222f17651d
Name:		coco-coq
Version:	0.1
Release:        36%{?dist}
Summary:        Coco Coq in Grostesteing's base, an AGI adventure game
License:	CC-BY-ND-4.0
URL:		http://membres.lycos.fr/agisite/coco-c.htm
Source0:        cococe.zip
Source1:	coco-coq.desktop
Source2:	coco-coq-wrapper.sh
Source3:	coco-coq.xpm
Source4:	coco-coq-LICENSE.fedora
BuildArch:	noarch
Requires:	nagi, hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
# /oreon:deps
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
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
