%global source0_hash 7257347993c553b5461515b4d8bc03a104036ec1d19082c7cc314e9ae7943169

# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
#

%global fontname        thibault
%global conf1           69-essays1743.conf
%global conf2           69-isabella.conf
%global conf3           69-rockets.conf
%global conf4           69-staypuft.conf

%define common_desc \
A collection of fonts from thibault.org,\
including Isabella, Essays1743, StayPuft,\
and Rockets.

Name:           %{fontname}-fonts
Version:        0.1
Release:        45%{?dist}

Summary:        Thibault.org font collection
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+

URL:            http://www.thibault.org/fonts
Source0:        http://www.thibault.org/fonts/essays/essays1743-2.000-1-ttf.tar.gz
Source1:        http://thibault.org/fonts/isabella/Isabella-1.2-ttf.tar.gz
Source2:        http://www.thibault.org/fonts/rockets/Rockets-ttf.tar.gz
Source3:        http://www.thibault.org/fonts/staypuft/StayPuft.tar.gz
Source4:        %{name}-essays1743-fontconfig.conf
Source5:        %{name}-isabella-fontconfig.conf
Source6:        %{name}-rockets-fontconfig.conf
Source7:        %{name}-staypuft-fontconfig.conf

Source10:       %{fontname}-essays1743.metainfo.xml
Source11:       %{fontname}-isabella.metainfo.xml
Source12:       %{fontname}-rockets.metainfo.xml
Source13:       %{fontname}-staypuft.metainfo.xml

#Not included due to legal concerns
#Engadget: A sort of modernistic font done to match the logo of http://www.engadget.com

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge >= 20061025-1

%description
%common_desc

%package common
Summary:        Common files for thibault (documentation…)
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-essays1743-fonts

Summary:  Thibault.org Montaigne's Essays typeface font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-essays1743 < 0.1-17

%description -n %{fontname}-essays1743-fonts
%common_desc

A font by John Stracke, based on the
typeface used in a 1743 English
translation of Montaigne's Essays.

%_font_pkg -n essays1743 -f %{conf1} Essays1743*.ttf
%{_datadir}/appdata/%{fontname}-essays1743.metainfo.xml

%package -n %{fontname}-isabella-fonts

Summary: Thibault.org Isabella Breviary calligraphic font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-isabella < 0.1-17

%description -n %{fontname}-isabella-fonts
%common_desc

This font is called Isabella because it is based on the
calligraphic hand used in the Isabella Breviary, made around 1497, in
Holland, for Isabella of Castille, the first queen of united Spain.

%_font_pkg -n isabella -f %{conf2} Isabella*.ttf
%{_datadir}/appdata/%{fontname}-isabella.metainfo.xml

%package -n %{fontname}-rockets-fonts

Summary:  Thibault.org font, vaguely space themed

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-rockets < 0.1-17

%description -n %{fontname}-rockets-fonts
%common_desc

This font is called Rockets because it's vaguely space
themed.  The A is, more or less, a 1950s SF rocket; the O is meant to
be Earth, with the Americas visible.  The other capitals are based on
curves from either A or O, to keep the theme consistent.

%_font_pkg -n rockets -f %{conf3} Rockets*.ttf
%{_datadir}/appdata/%{fontname}-rockets.metainfo.xml

%package -n %{fontname}-staypuft-fonts

Summary: Thibault.org font, rounded and marshmellowy

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-staypuft < 0.1-17

%description -n %{fontname}-staypuft-fonts
%common_desc

A rounded marshmellow type font. Good for frivolous things
like banners, and birthday cards.

%_font_pkg -n staypuft -f %{conf4} StayPuft*.ttf
%{_datadir}/appdata/%{fontname}-staypuft.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

mkdir -p staypuft
tar xvzf %{SOURCE0}
tar xvzf %{SOURCE1}
tar xvzf %{SOURCE2}
tar xvzf %{SOURCE3} -C staypuft

%build

pushd essays1743
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743.sfd ../Essays1743.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Bold.sfd ../Essays1743-Bold.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-BoldItalic.sfd ../Essays1743-BoldItalic.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Italic.sfd ../Essays1743-Italic.ttf
popd

pushd Isabella
fontforge -lang=ff -c 'Open($1); Generate($2)' Isabella-first.sfd ../Isabella.ttf
popd

pushd rockets
fontforge -lang=ff -c 'Open($1); Generate($2)' Rockets.sfd ../Rockets.ttf
popd

pushd staypuft
fontforge -lang=ff -c 'Open($1); Generate($2)' StayPuft.sfd ../StayPuft.ttf
popd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf1}

install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf2}

install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf3}

install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf4}

for fconf in %{conf1} \
                %{conf2} \
                %{conf3} \
                %{conf4} ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-essays1743.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-isabella.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-rockets.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-staypuft.metainfo.xml

%files common
%doc essays1743/COPYING essays1743/README
%doc Isabella/COPYING.LIB Isabella/README.txt
%doc rockets/COPYING.LIB rockets/README.txt
%doc staypuft/COPYING.LIB staypuft/README.txt

%changelog
%autochangelog
