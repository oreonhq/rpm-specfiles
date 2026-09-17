%global source0_hash 4fb186070b3e7d33a51821e3307dce57300a062570d028feccd4e628d50dea8a

Name:           pdf2svg
Version:        0.2.3
Release:        25%{?dist}
Summary:        Small tool to convert PDF files into SVG

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.cityinthesky.co.uk/opensource/pdf2svg/
Source0:        https://github.com/db9052/pdf2svg/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  poppler-glib-devel
BuildRequires:  cairo-devel
BuildRequires:  gtk2-devel

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

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/pdf2svg

%changelog
%autochangelog
