%global source0_hash 785cd3bf51e05f6bb86ab0d649b7ed20e31892eb635bc5a25c963bf934088445
Name:           feh
Version:        3.13.1
Release:        1%{?dist}
Summary:        Fast command line image viewer using Imlib2
License:        MIT
URL:            https://feh.finalrewind.org
Source0:        https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
Patch0:         feh-1.10.1-dejavu.patch
Requires:       dejavu-sans-fonts
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl-Test-Command
BuildRequires:  perl-Test-Harness
# /oreon:deps
%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slide-show or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir feh-%{version}
%oreon_prep
%build

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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
