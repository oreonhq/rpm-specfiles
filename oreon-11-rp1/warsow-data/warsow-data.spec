%global source0_hash none

Name:           warsow-data
Version:        2.1.2
Release:        18%{?dist}
Summary:        Game data for Warsow

# For a breakdown of the licensing, see license.txt
# Automatically converted from old format: CC-BY-SA and CC-BY-ND - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-CC-BY-ND
URL:            https://www.warsow.net/
Source0:        http://sebastian.network/warsow/warsow-%{version}.tar.gz

BuildArch:      noarch

# Warsow is only ported to these architectures
%if 0%{?rhel} == 7
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

BuildRequires:  /usr/bin/dos2unix
Requires:       warsow = %{version}

%description
Warsow is a fast paced first person shooter consisting of cel-shaded
cartoon-like graphics with dark, flashy and dirty textures. Warsow is based on
the E-novel "Chasseur de bots" ("Bots hunter" in English) by Fabrice Demurger.
Warsow's codebase is built upon Qfusion, an advanced modification of the Quake
II engine.

This package installs the game data files (textures, maps, sounds, etc.).

%prep
%setup -q -n warsow-%{version}

# Convert to utf-8 and Unix line breaks
dos2unix docs/license.txt

# Remove executable permissions from data files
chmod 644 docs/*
find basewsw -type f | xargs chmod 644

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/warsow
cp -a basewsw $RPM_BUILD_ROOT%{_datadir}/warsow/

%files
%license docs/license.txt
%{_datadir}/warsow/

%changelog
%autochangelog
