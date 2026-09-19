%global source0_hash 274f6be23fd089bd9e8715b67643a66ca2f63a503028bdea3e571228d50b669e

Name:		jpeginfo
Version:	1.7.1
Release:	8%{?dist}
Summary:	Error-check and generate informative listings from JPEG files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.kokkonen.net/tjko/projects.html
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz

Provides:	bundled(md5-plumb)

BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	make

%description
Jpeginfo prints information and tests integrity of JPEG/JFIF files. It can
generate informative listings of .jpg files, and can also be used to test
them for errors (and optionally delete broken files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rm getopt*.*

%build
%configure
%make_build

%install
install -Dpm 0755 jpeginfo %{buildroot}/%{_bindir}/jpeginfo
install -Dpm 0644 jpeginfo.1 %{buildroot}/%{_mandir}/man1/jpeginfo.1

%files
%license COPYRIGHT LICENSE
%doc README
%{_bindir}/jpeginfo
%{_mandir}/man1/*.1*

%changelog
%autochangelog
