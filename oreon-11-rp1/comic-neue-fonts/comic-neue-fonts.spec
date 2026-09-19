%global source0_hash 54dd998c93b8d6658b1c2d6ade9f790d10ffaa3632868dd2cfac84b405290321

%global fontname comic-neue
%global fontconf 63-%{fontname}

%global common_desc \
Comic Neue is a font created by Craig Rozynski that takes inspiration\
from Comic Sans. It is perfect as a display face, for marking up comments,\
and writing passive aggressive office memos.

Name:           %{fontname}-fonts
Version:        2.51
Release:        15%{?dist}
Summary:        A typeface family inspired by Comic Sans

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://comicneue.com/
Source0:        http://comicneue.com/%{fontname}-%{version}.zip
Source1:        %{fontname}-fontconfig.conf
Source2:        %{fontname}-angular-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       %{name}-common = %{version}-%{release}

%description
%common_desc

%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-angular-fonts
Summary:        A typeface family inspired by Comic Sans, angular variant
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-angular-fonts
%common_desc

The Comic Neue Angular variant features angular terminals rather than round.

%package -n %{fontname}-web-fonts
Summary:        A typeface family inspired by Comic Sans, web files
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-web-fonts
%common_desc

This package contains Web Open Font Format versions 1 and 2 files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/OTF/*/*.otf %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff2 %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-angular.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-angular.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%_font_pkg -f %{fontconf}.conf ComicNeue-*.otf
%_font_pkg -n angular -f %{fontconf}-angular.conf ComicNeueAngular-*.otf
%_font_pkg -n web ComicNeue*.woff ComicNeue*.woff2

%files common
%defattr(0644,root,root,-)
%doc %{fontname}-%{version}/Booklet-ComicNeue.pdf %{fontname}-%{version}/FONTLOG.txt
%license %{fontname}-%{version}/OFL.txt %{fontname}-%{version}/OFL-FAQ.txt

%changelog
%autochangelog
