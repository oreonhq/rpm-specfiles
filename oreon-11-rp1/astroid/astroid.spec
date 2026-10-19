%global source0_hash dd419d4e11d1efa95979472e17cca5066799a5c64a595d5cea2b9e8d9f60f9c8
Name:           astroid
Version:        0.17
Release:        1%{?dist}
Summary:        Notmuch e-mail client
License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/astroidmail/astroid
Source0:        https://github.com/%{name}mail/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        astroid.metainfo.xml
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmark
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  gmime30-devel
BuildRequires:  gnupg2
BuildRequires:  gnupg2-gpg-agent
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpeas-devel
BuildRequires:  libsass-devel
BuildRequires:  ninja-build
BuildRequires:  notmuch-devel
BuildRequires:  protobuf-devel
BuildRequires:  scdoc
BuildRequires:  vte291-devel
BuildRequires:  w3m
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Astroid is a lightweight and fast Mail User Agent that provides a graphical
interface to searching, displaying and composing email, organized in threads
and tags. Astroid uses the notmuch backend for blazingly fast searches
through tons of email. Astroid searches, displays and composes emails - and
rely on other programs for fetching, syncing and sending email.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Ensure library gets installed in correct location
sed -i "s|lib/astroid/web-extensions|%{_lib}/astroid/web-extensions|g" CMakeLists.txt

%build

%cmake -G Ninja
%cmake_build
%install
%cmake_install
mkdir -p  %{buildroot}/%{_metainfodir}/
install -Dpm0644 %{SOURCE1} %{buildroot}/%{_metainfodir}/
%oreon_autofiles main

%check

xvfb-run %__ctest \
         --test-dir "%{__cmake_builddir}" \
         --output-on-failure \
         --force-new-ctest-process \
         --timeout 6000 \
         -j1
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/astroid.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/astroid.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
