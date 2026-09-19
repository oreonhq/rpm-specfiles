%global source0_hash f2d8d8ba6caa785a966ef17996822ab14ba91ec423431a29e1b6c4b14bc4cda5

%global fontname levien-inconsolata
%global fontconf 75-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        3.000
Release:        16%{?dist}
Summary:        Inconsolata fonts

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            https://levien.com/type/myfonts/inconsolata.html
Source0:        https://github.com/googlefonts/Inconsolata/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
BuildRequires:  git-core
Requires:       fontpackages-filesystem

%description
A monospace font, designed for code listings and the like, in print.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Inconsolata-%{version} -p1 -S git

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

        
%_font_pkg -f %{fontconf} *.ttf
%doc documentation/*.pdf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
%autochangelog
