%global source0_hash eeec8b4727efe056f6f0ac48b523b30dd8316e87e6528fe9916b0c27229237ae

Summary:   Themes for Enlightenment, DR16
Name:      e16-themes
Version:   1.0.1
Release:   29%{?dist}
# Automatically converted from old format: MIT with advertising - review is highly recommended.
License:   LicenseRef-Callaway-MIT-with-advertising
URL:       http://www.enlightenment.org/
#
# Use create-clean-tarball.sh script to create the cleaned tarball
# from the original tarball:
#   http://downloads.sourceforge.net/enlightenment/e16-themes-%{version}.tar.gz
#
Source0:   e16-themes-cleaned-%{version}.tar.gz
Source1:   create-clean-tarball.sh
BuildArch: noarch
BuildRequires: make
Requires:  e16 >= 1.0.0

%description
The BlueSteel, BrushedMetal-Tigert, Ganymede and ShinyMetal themes
for Enlightenment, DR16.  

This is part of the Enlightenment distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --enable-fsstd
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%{__rm} -rfv %{buildroot}%{_datadir}/e16/themes/ShinyMetal/epplets/images/.xvpics
%{__chmod} 0755 %{buildroot}%{_datadir}/e16/themes/Ganymede/ACTIVATE_BUTTONS
# symlink all font configs to default theme
for theme in BlueSteel BrushedMetal-Tigert Ganymede ShinyMetal ; do
    %{__rm} -f %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
    %{__ln_s} ../winter/fonts.theme.cfg \
       %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
done
# Remove refs to removed fonts
%{__sed} -i -r -e 's/face=(aircut3,ganymede|rothwell|vixar|zirkle)/face=Vera/g' \
    %{buildroot}%{_datadir}/e16/themes/*/ABOUT/MAIN

%files
%doc AUTHORS COPYING
%{_datadir}/e16/themes

%changelog
%autochangelog
