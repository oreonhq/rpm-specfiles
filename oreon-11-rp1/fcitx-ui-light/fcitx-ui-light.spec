%global source0_hash 6fc12f1efdf0cb48d26eaf8a6b9dd26c4595112ee01cc051b42d548dc6c68c54

Name:		fcitx-ui-light
Version:	0.1.3
Release:	34%{?dist}
Summary:	Light UI for fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://code.google.com/p/fcitx/
Source0:	http://fcitx.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libcurl-devel, pkgconfig
BuildRequires:	fontconfig, fontconfig-devel, libXpm-devel, libXft-devel
BuildRequires:	desktop-file-utils
Requires:	fcitx

%description
Light UI is a light-weight user interface for fcitx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

desktop-file-install --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/fcitx-light.desktop

cat << EOF > %{name}.lang 
%lang(zh) /usr/share/locale/zh_TW/LC_MESSAGES/fcitx-light-ui.mo
%lang(zh) /usr/share/locale/zh_CN/LC_MESSAGES/fcitx-light-ui.mo
EOF

%files -f %{name}.lang
%doc README COPYING AUTHORS
%{_datadir}/fcitx/configdesc/*.desc
%{_datadir}/fcitx/addon/*.conf
%{_libdir}/fcitx/*.so
%{_datadir}/applications/fcitx-light.desktop

%changelog
%autochangelog
