%global source0_hash 0be90252c4bf8e06bbca16ef376bd1d7891f3353a5145289bff8a48563568259

Name:           elementary-xfce-icon-theme
Version:        0.22
Release:        2%{?dist}
Summary:        Icons for Xfce based on the elementary Project Icon Theme
 

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/shimmerproject/elementary-xfce 
Source0:       https://github.com/shimmerproject/elementary-xfce/releases/tag/%{version}#/elementary-xfce-%{version}.tar.gz 

BuildArch:      noarch

BuildRequires:  gtk3-devel >= 3.18
BuildRequires:  optipng

%description
This is an icon-theme maintained with Xfce in mind,
but it supports other desktops like Gnome3 as well.
It's a fork of the upstream elementary-project, 
which took place because the team decided to
drop a lot of desktop-specific symlinks. 
This icon-theme is supposed to keep everything 
working, but we'll still pull new icons from upstream 
and integrate them occasionally.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q %{name}/
mkdir -p doc/elementary-xfce
# fix for the wrong naming inside the tar.gz
mv elementary-xfce-%{version}/{README.md,LICENSE,CONTRIBUTORS,AUTHORS} doc/elementary-xfce/

%build

%install
mkdir -p  %{buildroot}%{_datadir}/icons
cp -a elementary-xfce-%version/elementary-xfce/  %{buildroot}%{_datadir}/icons

chmod 0644  %{buildroot}%{_datadir}/icons/elementary-xfce/index.theme

# Remove broken links
rm -rf %{buildroot}%{_datadir}/icons/elementary-xfce/{README.md,LICENSE,CONTRIBUTORS,AUTHORS}

%post
touch --no-create %{_datadir}/icons/elementary-xfce &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
         touch --no-create %{_datadir}/icons/elementary-xfce &>/dev/null   
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce &>/dev/null
&>/dev/null

fi

%posttrans
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce &>/dev/null

%files
%{_datadir}/icons/elementary-xfce/
%doc doc/*

%changelog
%autochangelog
