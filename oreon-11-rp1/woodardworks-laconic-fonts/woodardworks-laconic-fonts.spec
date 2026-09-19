%global source0_hash 00b2969906f46ab71408e476eae43801635fa5eba5f24575a9622ec3e571a330

%global fontname woodardworks-laconic
%global fontconf 60-%{fontname}

Name:		%{fontname}-fonts
Summary:	An artistic and minimal sans-serif font family
Version:	001.001
Release:	33%{?dist}
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
Source0:	http://www.woodardworks.com/laconic.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}-shadow-fonts-fontconfig.conf
Source3:        %{fontname}.metainfo.xml
Source4:        %{fontname}-shadow.metainfo.xml
URL:		http://www.woodardworks.com/type13.html
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem
BuildArch:	noarch

%description
Laconic is a typeface font design meant to be dry without quite seeming 
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in 
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.

%package -n %{fontname}-shadow-fonts
Summary:	A shadowed version of the Laconic sans-serif font family
Requires:	fontpackages-filesystem

%description -n %{fontname}-shadow-fonts
Laconic is a typeface font design meant to be dry without quite seeming
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.
This package contains the Laconic Shadow font face.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -n laconic
# We have to do this to avoid leaving a stray __MACOSX dir in the buildroot
unzip -j -L -q %{SOURCE0}
# Get rid of junk files
rm -rf ._*

%build
# Nothing to do here, already in OTF.

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shadow.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-shadow.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}-shadow.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-shadow.metainfo.xml

%_font_pkg -f %{fontconf}.conf Laconic_Bold.otf Laconic_Light.otf Laconic_Regular.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc laconic_eula.pdf

%_font_pkg -n shadow -f %{fontconf}-shadow.conf Laconic_Shadow.otf
%{_datadir}/appdata/%{fontname}-shadow.metainfo.xml
%doc laconic_eula.pdf

%changelog
%autochangelog
