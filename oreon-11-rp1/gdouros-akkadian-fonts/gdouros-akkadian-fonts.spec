%global source0_hash 1f9c19c7261045a5e7cea8d9fb7d52486d8ff396798f855c08faac71c772cf21

%global fontname gdouros-akkadian
%global fontconf 65-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        7.17
Release:        21%{?dist}
Summary:        A font for Sumero-Akkadian cuneiform

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        LicenseRef-Fedora-UltraPermissive
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/AkkadianAssyrian.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Akkadian covers the following scripts and symbols supported by The Unicode
Standard 5.2: Basic Latin, Greek and Coptic, some Punctuation and other
Symbols, Cuneiform, Cuneiform Numbers and Punctuation.

It was created by George Douros.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Akkadian.ttf %{buildroot}%{_fontdir}

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

%_font_pkg -f %{fontconf} Akkadian.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Akkadian*.pdf

%changelog
%autochangelog
