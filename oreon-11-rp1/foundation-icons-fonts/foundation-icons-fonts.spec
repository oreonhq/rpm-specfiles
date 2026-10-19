%global source0_hash eeec3eb793e55c65bd396b09cb04a624c167f67836e38514d557274f06ee1e2a
%global fontname foundation-icons
%global fontconf 60-%{fontname}.conf
Name:           %{fontname}-fonts
Version:        3.0
Release:        1%{?dist}
Summary:        Foundation Icons font
License:        MIT
URL:            https://zurb.com/playground/foundation-icon-fonts-3
Source0:        https://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip
Source1:        %{name}-fontconfig.conf
Patch1:         foundation-icons-fonts-3.0-fix_css.patch
BuildArch:      noarch
Requires:       fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
%description
A custom collection of 283 icons that are stored in a handy font.

This package contains the TrueType font file which is typically used locally.

%package web
Requires:       %{fontname}-fonts = %{version}-%{release}
Summary:        Foundation Icons font css file
%description web
A custom collection of 283 icons that are stored in a handy font.

This package contains the CSS file for use on a webserver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir foundation-icons
%oreon_prep
%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
mkdir -p %{buildroot}%{_datadir}/foundation-icons-web/
cp -a foundation-icons.css %{buildroot}%{_datadir}/foundation-icons-web/
%_font_pkg -f %{fontconf} *.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n foundation-icons-fonts-web -f %{oreon_filedir}/foundation-icons-fonts-web.list

%changelog

%autochangelog
