%global source0_hash 4746c04c9a4ad9e0788a38e0a2f81919a630d8070ceabc89f156b6d41d8ceb37

%define fontname sil-gentium
%define archivename ttf-sil-gentium
%define common_desc \
SIL Gentium ("belonging to the nations" in Latin) is a Unicode typeface family\
designed to enable the many diverse ethnic groups around the world who use\
the Latin script to produce readable, high-quality publications. It supports\
a wide range of Latin-based alphabets.

Name:           %{fontname}-fonts
Version:        1.02
Release:        39%{?dist}
Summary:        SIL Gentium fonts

License:        OFL-1.1
URL:            http://scripts.sil.org/Gentium_linux
# Source0 can be downloaded from the above URL, search for "tar.gz"
Source0:        %{archivename}_1.0.2.tar.gz
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-alt.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       %{name}-common = %{version}-%{release}

# Obsoleting and providing the old RPM name
Obsoletes:      gentium-fonts < 1.02-7

%description
%common_desc

This package consists of the main SIL Gentium family.

%_font_pkg Gen[RI]*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%package common
Summary:        Common files of SIL Gentium fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-alt-fonts
Summary:        SIL GentiumAlt fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-alt-fonts
%common_desc

This package consists of the SIL GentiumAlt family. GentiumAlt is a
alternative version of Gentium with flatter diacratics, to make it more
suitable for languages that use stacking diacratics, like Vietnamese. There
is no problem with having both Gentium and GentiumAlt installed at the same
time.

%_font_pkg -n alt GenA*.ttf
%{_datadir}/appdata/%{fontname}-alt.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}-%{version}

# Convert GENTIUM-FAQ from MacRoman
iconv --from=MACINTOSH --to=UTF-8 GENTIUM-FAQ > GENTIUM-FAQ.new
touch -c -r GENTIUM-FAQ GENTIUM-FAQ.new
mv GENTIUM-FAQ.new GENTIUM-FAQ

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-alt.metainfo.xml

%files common
%doc FONTLOG GENTIUM-FAQ OFL-FAQ QUOTES README
%license OFL

%changelog
%autochangelog
