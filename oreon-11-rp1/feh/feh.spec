%global source0_hash 43d8e6742ec273ef3084bde82c5ead5a074348d9bfce28f1b0f8504623ca9b74

Name:           feh
Version:        3.11.1
Release:        2%{?dist}
Summary:        Fast command line image viewer using Imlib2
License:        MIT
URL:            https://feh.finalrewind.org
Source0:        https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
Patch0:         feh-1.10.1-dejavu.patch

BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libXt-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libexif-devel
BuildRequires:  make
BuildRequires:  perl-Test-Command
BuildRequires:  perl-Test-Harness
Requires:       dejavu-sans-fonts
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slide-show or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n feh-%{version}

%build
# Propagate values into config.mk
sed -i \
  -e "s|^doc_dir =.*$|doc_dir = \$(DESTDIR)%{_pkgdocdir}|" \
  -e "s|^example_dir =.*$|example_dir = \$(doc_dir)/examples|" \
  -e "s|^CFLAGS ?=.*$|CFLAGS = ${RPM_OPT_FLAGS}|" \
  config.mk
%make_build PREFIX="%{_prefix}" VERSION="%{version}" \
    curl=1 exif=1 test=1 xinerama=1

%install
%make_install PREFIX=%{_prefix}
rm %{buildroot}%{_datadir}/%{name}/fonts/yudit.ttf
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm %{buildroot}%{_docdir}/%{name}/examples/find-lowres

%check
make test

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%{_datarootdir}/icons/hicolor/48x48/apps/feh.png
%{_datarootdir}/icons/hicolor/scalable/apps/feh.svg

%changelog
%autochangelog
