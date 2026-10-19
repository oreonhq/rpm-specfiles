%global source0_hash fd765256f18b5890639e93cabdf631b640966ed1ea9ebd561aede9d3be2155e4
Name:           pdf2svg
Version:        0.2.4
Release:        1%{?dist}
Summary:        Small tool to convert PDF files into SVG
License:        GPL-2.0-or-later
URL:            http://www.cityinthesky.co.uk/opensource/pdf2svg/
Source0:        https://github.com/db9052/pdf2svg/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  poppler-glib-devel
# /oreon:deps
%description
A small tool to convert PDF files into SVG using poppler and cairo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%configure
make %{?_smp_mflags}
%install
%make_install INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
