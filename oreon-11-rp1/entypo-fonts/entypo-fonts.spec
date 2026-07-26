%global source0_hash 58d5d41ed65a127d4de010bddb1558cb65f050595eae694da8fb7505fa3ad15c

%global fontname entypo
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        20121031
Release:        26%{?dist}
Summary:        Pictogram Suite font

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://www.entypo.com/
                # From "Download package" on %%{url}
Source0:        http://dl.dropbox.com/u/4339492/Entypo.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Entypo is a set of 250+ carefully crafted pictograms. The source contains
an icon font — OpenType, TrueType and @font-face — EPS, PDF and PSD files.
Only the Desktop  ttf font is packaged, the other fonts contains
trademarked symbols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%build

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
cd "Entypo/@font-face/Entypo @font-face/"
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf  %{buildroot}%{_fontdir}

%_font_pkg -f %{fontconf} *.ttf

%doc "Entypo/Glyph guide.rtf"

%changelog
%autochangelog
