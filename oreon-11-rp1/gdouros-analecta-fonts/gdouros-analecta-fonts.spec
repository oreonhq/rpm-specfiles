%global source0_hash 95ca09395e15cb8d6366625d60ffd2e96dc28703ae81a206e2c6ec53399116d8

%global fontname gdouros-analecta
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        5.17
Release:        21%{?dist}
Summary:        An ecclesiastic scripts font

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Analecta.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Analecta is an ecclesiastic scripts font, covering Basic Latin, Greek and
Coptic, some Punctuation and other Symbols, Coptic, typographica varia,
Specials, Gothic and Deseret.

It was created by George Douros.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Analecta.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} Analecta.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Analecta.pdf

%changelog
%autochangelog
