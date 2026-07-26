%global source0_hash 0949915ba8eb24d89fd93d10a7ff623f42830d7c5ffc3ecbf960e4ecad3e3e79

%global fontname fira-code
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        6.2
Release:        12%{?dist}
Summary:        Monospaced font with programming ligatures

License:        OFL-1.1
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/releases/download/%{version}/Fira_Code_v%{version}.zip#/%{name}-%{version}.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
Fira Code is an extension of the Fira Mono font containing a set of ligatures
for common programming multi-character combinations. This is just a font
rendering feature: underlying code remains ASCII-compatible. This helps to
read and understand code faster. For some frequent sequences like .. or //,
ligatures allow us to correct spacing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata file
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
%autochangelog
