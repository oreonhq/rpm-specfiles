%global source0_hash b5a4280571ec72483b14847f18299210076e1a37628ba352e9f05ce0a2ce46c3

%global upstream_name Gyazo-for-Linux

Name: gyazo
Version: 1.2
Release: 26%{?dist}
Summary: Screen capture (screenshot) tool
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
BuildArch: noarch
URL: https://gyazo.com/
Source0: https://github.com/gyazo/Gyazo-for-Linux/archive/1.2.tar.gz
Source1: gyazo.1
Patch0: fix_desktop_version.patch
Requires: ruby rubygems rubygem(json)
Requires: %{_bindir}/ps
Requires: ImageMagick
Requires: xclip xprop xwininfo
BuildRequires: desktop-file-utils

%description
Seriously Instant Screen-Grabbing (screenshot) Gyazo
lets you instantly grab  the screen and upload the image to the web. 
You can easily share them on Chat, Twitter, Blog, Tumblr, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}
%patch -P0
%build
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/ruby/%{name}
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{SOURCE1} %{buildroot}/%{_mandir}/man1/%{name}.1
cp src/%{name}.rb %{buildroot}/%{_datadir}/ruby/%{name}
cp src/%{name}.desktop %{buildroot}/%{_datadir}/applications
cp icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps
ln -f -s %{_datadir}/ruby/%{name}/%{name}.rb %{buildroot}/%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%attr(755,root,root) %{_bindir}/%{name}
%doc README.md
%license debian/copyright
%{_datadir}/ruby/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
