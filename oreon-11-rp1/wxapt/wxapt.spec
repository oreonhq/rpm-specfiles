%global source0_hash d5ca9bdbec74a01a04c17655886d36892fdcd4de96a5ee1636949e6492983eec

Name:           wxapt
Version:        1.7.1
Release:        16%{?dist}
Summary:        Console application for decoding and saving weather images

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/apt/wxapt/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf automake libtool gettext
BuildRequires:  alsa-lib-devel
BuildRequires:  ncurses-devel
BuildRequires:  rtl-sdr-devel

%description
wxapt is a console application for decoding and saving weather images
transmitted in the APT format of NOAA and METEOR satellites.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

%build
%configure
%make_build

%install
#skip make install and do manual install, it's just one file
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 src/%{name} %{buildroot}%{_bindir}/

%files
%doc AUTHORS NEWS README doc/*.html
%license COPYING LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
