%global source0_hash 2e7b07139f47d6636aa3333b9f39f362eeb3ac5f65abe2b09790ac22208d8aca
Name:       js-jquery-prettyphoto
Version:    3.1.6
Release:        1%{?dist}
BuildArch:  noarch
License:    GPL-2.0-only
Summary:        PrettyPhoto is a jQuery based lightbox clone
URL:        https://github.com/scaron/prettyphoto
Source0:        https://github.com/scaron/prettyphoto/archive/%{version}.tar.gz
Requires:      js-jquery
Requires:      web-assets-filesystem
# oreon:deps
BuildRequires:  web-assets-devel
# /oreon:deps
%description
The prettyPhoto library provides a jQuery based lightbox clone. Not only
does it support images, it also add support for videos, flash, YouTube,
iFrames. It’s a full blown media lightbox. The setup is easy and quick,
plus the script is compatible in every major browser. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n prettyphoto-%{version}

# https://github.com/scaron/prettyphoto/pull/170
chmod 0644 README

%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/css
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/images
install -d -m 0755 %{buildroot}/%{_webassetdir}/jquery-prettyphoto/js
install -D -p -m 0644 css/*.css %{buildroot}/%{_webassetdir}/jquery-prettyphoto/css
cp -a images/* %{buildroot}/%{_webassetdir}/jquery-prettyphoto/images
install -D -p -m 0644 js/jquery.prettyPhoto.js %{buildroot}/%{_webassetdir}/jquery-prettyphoto/js
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
