%global source0_hash 41a7da3767957727e33543a12b04b8f7ce1550f6925cd60ab43cd64f6c23493f

%global pkg_name %{name}3

Name:           starcal
Version:        3.2.2
Release:        6%{?dist}
Summary:        A full-featured international calendar written in Python

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://ilius.github.io/starcal/
Source0:        https://github.com/ilius/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       python3-gobject python3-httplib2 python3-psutil python3-cairo
Requires:       python3-dateutil python3-cachetools python3-requests
Requires:       libappindicator-gtk3

Recommends:     gtksourceview4 python3-igraph python3-pygit2
Suggests:       lxqt-openssh-askpass ntpdate

BuildArch:      noarch
BuildRequires:  python3-devel desktop-file-utils gettext git
BuildRequires:  python3-setuptools

%description
StarCalendar is a full-featured international calendar written in Python,
that supports Jalai(Iranian), Hijri(Islamic), and Indian National calendars,
as well as common English(Gregorian) calendar

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name}-%{version}
find -type f -name "*.py*" -exec chmod a+x {} \;
find -type f -exec \
   sed -i '1s=^#!/usr/bin/\(python\|env python\)[^ ]*\(.*\)$=#!%{__python3}\2=' {} \;
find -name "*.py" -exec sh -c 'if ! grep "^#\!" {} &> /dev/null;  then \
   sed -i -e "1i#!%{__python3}" {}; fi'  \;

%build

%install
echo | ./distro/base/install.sh %{buildroot} --for-pkg --prefix=%{_prefix}

# cleanups
rm -rf %{buildroot}%{_datadir}/doc/
rm -rf      \
  %{buildroot}%{_datadir}/%{pkg_name}/{*install*,README.md,donate} \
  %{buildroot}%{_datadir}/%{pkg_name}/locale.d

desktop-file-install     \
  --delete-original \
  --remove-category=Utility --set-icon=%{pkg_name}2 \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{pkg_name}.desktop

%find_lang %{pkg_name}

%files -f %{pkg_name}.lang
%doc authors donate README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{pkg_name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/%{pkg_name}*.png

%changelog
%autochangelog
