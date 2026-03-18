%global fontname lohit-gurmukhi
%global fontconf0 66-%{fontname}.conf
%global fontconf1 30-%{fontname}.conf
%global metainfo io.pagure.lohit.gurmukhi.font.metainfo


Name:           %{fontname}-fonts
Version:        2.91.2
Release:        24%{?dist}
Summary:        Free Gurmukhi truetype font for Punjabi language

License:        OFL-1.1
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source1:        %{name}.conf
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem
Provides:       lohit-punjabi-fonts = %{version}-%{release}
Obsoletes:      lohit-punjabi-fonts < 2.5.3-5


%description
This package provides a free Gurmukhi script truetype font for Punjabi language.


%prep
%setup -q -n %{fontname}-%{version}

%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf0} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf0}
ln -s %{_fontconfig_templatedir}/%{fontconf0} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf0}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f *.conf  *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-gurmukhi.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.91.2-24
- Prepare for Oreon 11 (RP1)
