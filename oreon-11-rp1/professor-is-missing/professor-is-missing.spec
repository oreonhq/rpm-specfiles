%global source0_hash 64721422fba6642ef91d02a7cd55ed30fd8d9ae5b7092252e9af0256706ea060
Name:		professor-is-missing
Version:	0.1
Release:        1%{?dist}
Summary:        The Professor is Missing, an AGI adventure game
License:	CC-BY-ND-4.0
URL:		http://membres.lycos.fr/agisite/prof.htm
Source0:        prof.zip
Source1:	professor-is-missing.desktop
Source2:	professor-is-missing-wrapper.sh
Source3:	professor-is-missing.xpm
Source4:	professor-is-missing-LICENSE.fedora
BuildArch:	noarch
Requires:	nagi, hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
# /oreon:deps
%description
In this little game, for a mysterious reason, the Professor is disaspeared in
Africa. As Eric, you must find a way to go to Africa to find out the
Professor.

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
sed -i 's/\r//' readme.txt
sed -i 's/\r//' walkthru.txt

%build

cp %{SOURCE4} .
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p logdir object picdir professor-is-missing-LICENSE.fedora readme.txt snddir viewdir vol.0 walkthru.txt words.tok $RPM_BUILD_ROOT%{_datadir}/%{name}
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
