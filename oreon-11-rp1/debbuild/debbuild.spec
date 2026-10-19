%global source0_hash 0fb2693adaadc7e8425e6d65fb6885876a2b500f620b1f8de75e6895c43633a8
%global _debconfigdir %{_prefix}/lib/debbuild
Name:           debbuild
Version:        24.12.0
Release:        1%{?dist}
Summary:        Build Debian-compatible .deb packages from RPM .spec files
License:        GPL-2.0-or-later
URL:            https://github.com/debbuild/debbuild
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       bzip2
Requires:       dpkg
Requires:       dpkg-dev
Requires:       fakeroot
Requires:       gzip
Requires:       patch
Requires:       spax
Requires:       xz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl-generators
# /oreon:deps
%description
debbuild attempts to build Debian-friendly semi-native packages from
RPM spec files, RPM-friendly tarballs, and RPM source packages
(.src.rpm files).  It accepts most of the options rpmbuild does, and
should be able to interpret most spec files usefully.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --debconfigdir=%{_debconfigdir} VERSION=%{version}
make
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
