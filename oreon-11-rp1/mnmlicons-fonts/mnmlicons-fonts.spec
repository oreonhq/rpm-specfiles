%global source0_hash 9ca4efa8151dfb4330a708e19fb3a358e5096c4484808a98f7ff206cfb0a7214

%global fontname mnmlicons
%global fontconf 69-%{fontname}.conf

Name:       %{fontname}-fonts
Version:    1.1
Release:    25%{?dist}
Summary:    Perkins Less Web Framework webfonts

License:    MIT
URL:        http://code.google.com/p/perkins-less/
Source0:    http://perkins-less.googlecode.com/files/perkins-%{version}.zip
Source1:    %{name}-fontconfig.conf
BuildArch:  noarch

BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Fonts from the deprecated old version of the Perkins Less web framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%build

%install
install -m 0644 -pD stylesheets/perkins/mnmlicons/mnmliconsv21-webfont.ttf \
    %{buildroot}%{_fontdir}/mnmlicons.ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf

%doc LICENSE

%changelog
%autochangelog
