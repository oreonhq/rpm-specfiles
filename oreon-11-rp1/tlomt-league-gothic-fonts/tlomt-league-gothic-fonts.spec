%global source0_hash e627adc5472c2b5febe5ec82a60805f1938c4ee10e8d90fb5d7449b08dd7b218

%global fontname tlomt-league-gothic
%global fontconf 61-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.0
Release:        30%{?dist}
Summary:        A sans serif gothic typeface

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://www.theleagueofmoveabletype.com/fonts/7-league-gothic
Source0:        http://s3.amazonaws.com/theleague-production/fonts/league-gothic.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
League Gothic is a revival of an old classic, Alternate Gothic No.1.
It was originally designed by Morris Fuller Benton for the American
Type Founders Company (ATF) in 1903. The company went bankrupt in 1993.
And since the original typeface was created before 1923, the typeface
is in the public domain. It is a sans serif gothic typeface.

This is actually another version of the font which was made by
The League of Movable Type and contributed to the Open Source Type
Movement.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -L -q %{SOURCE0}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p League\ Gothic.otf %{buildroot}%{_fontdir}/

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
