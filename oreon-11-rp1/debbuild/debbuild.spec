%global source0_hash e17c4f5b37e8c16592ebd99281884cabc053fb890af26531e9825417047d1430

# This is not archful information, and mimics RPM's paths
%global _debconfigdir %{_prefix}/lib/debbuild

Name:           debbuild
Version:        20.04.0
Release:        19%{?dist}
Summary:        Build Debian-compatible .deb packages from RPM .spec files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/debbuild/debbuild
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Man)
BuildRequires: make

%if 0%{?rhel} && 0%{?rhel} < 7
Requires:       /usr/bin/lsb_release
%endif

Requires:       bash
Requires:       bzip2
Requires:       dpkg
Requires:       dpkg-dev
Requires:       fakeroot
Requires:       gzip
Requires:       patch
Requires:       spax
Requires:       xz

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     git-core
Recommends:     quilt
Recommends:     unzip
Recommends:     zip
Recommends:     zstd
%endif

%{?perl_default_filter}

%description
debbuild attempts to build Debian-friendly semi-native packages from
RPM spec files, RPM-friendly tarballs, and RPM source packages
(.src.rpm files).  It accepts most of the options rpmbuild does, and
should be able to interpret most spec files usefully.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --debconfigdir=%{_debconfigdir} VERSION=%{version}
make

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{!?_licensedir:%global license %doc}
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_debconfigdir}/
%dir %{_sysconfdir}/%{name}

%changelog
%autochangelog
