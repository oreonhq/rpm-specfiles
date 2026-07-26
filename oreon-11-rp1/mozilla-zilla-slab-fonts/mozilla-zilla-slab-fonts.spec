%global source0_hash 62490dc19cd17e2951fe88ba3e662089ca14077634cacf1f12926374281dcf42

%global fontname        mozilla-zilla-slab
%global fontconf        60-%{fontname}

# Common description
%global common_desc \
Zilla Slab is a casual and contemporary slab serif with a good amount of quirk. \
It is the official brand typeface for Mozilla. \
%{nil}

Name:      %{fontname}-fonts
Version:   1.002
Release:   14%{?dist}
Summary:   Mozilla's Zilla Slab fonts
# Automatically converted from old format: OFL - review is highly recommended.
License:   LicenseRef-Callaway-OFL
URL:       https://mozilla.design/mozilla/typography/
Source0:   https://github.com/mozilla/zilla-slab/releases/download/v%{version}/Zilla-Slab-Fonts-v%{version}.zip
Source1:   %{fontname}.conf
Source2:   %{fontname}-highlight.conf
BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: unzip
Requires:  %{name}-common = %{version}-%{release}

%description
%common_desc

%_font_pkg -f %{fontconf}.conf ZillaSlab-*.otf

%package common
Summary:  Common files for Mozilla's Zilla Slab font set
Requires: fontpackages-filesystem
%description common
%common_desc
This package consists of files used by other %{name} packages.

%package -n %{fontname}-highlight-fonts
Summary:   Highlighted version of Mozilla's Zilla Slab font
Requires:  %{name}-common = %{version}-%{release}
%description -n %{fontname}-highlight-fonts
%common_desc
This package contains the highlighted version of Mozilla's Zilla Slab font.

%_font_pkg -n highlight -f %{fontconf}-highlight.conf ZillaSlabHighlight-*.otf

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n zilla-slab
cp -p %{SOURCE1} %{SOURCE2} .

# Fix permissions for license file
chmod 644 LICENSE

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontname}.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{fontname}-highlight.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-highlight.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-highlight.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

%files common
%license LICENSE
%dir %{_fontdir}

%changelog
%autochangelog
