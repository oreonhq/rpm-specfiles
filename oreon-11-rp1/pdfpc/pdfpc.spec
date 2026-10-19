%global source0_hash 0083a958a2e9288a15c31aabb76b3eadf104672b4e815017f31ffa0d87db02ec
Name:           pdfpc
Version:        4.7.0
Release:        1%{?dist}
Summary:        A GTK based presentation viewer application for GNU/Linux
License:        GPL-3.0-or-later
URL:            https://%{name}.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libvala-devel
BuildRequires:  pango-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  qrencode-devel
BuildRequires:  vala
BuildRequires:  webkit2gtk4.1-devel
# /oreon:deps
%description
pdfpc is a GTK based presentation viewer application for GNU/Linux which uses
Keynote like multi-monitor output to provide meta information to the speaker
during the presentation. It is able to show a normal presentation window on one
screen, while showing a more sophisticated overview on the other one providing
information like a picture of the next slide, as well as the left over time
till the end of the presentation. The input files processed by pdfpc are PDF
documents, which can be created using nearly any of today's presentation
software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DSYSCONFDIR=/etc
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
