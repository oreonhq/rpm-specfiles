%global source0_hash 34c09dbb29aad2a758f748f0f243850c1b5dcbd4e5662bfb473d8e434a555a4a
Name:      cptutils
Version:   1.82
Release:        1%{?dist}
Summary:        Utilities to manipulate and translate color gradients
License:   GPL-2.0-or-later
URL:       https://jjg.gitlab.io/en/code/cptutils
Source0:        https://jjg.gitlab.io/src/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
The GMT package implements colour gradients with the cpt (colour palette) file format,
and provides some tools for creating and manipulating them.The cptutils package contains
a number of additional utilities, mostly for translation to and from other formats.

The cptutils package was written to aid the construction of the cpt archive
cpt-city http://seaviewsensing.com/pub/cpt-city/ where thousands of
gradients can be downloaded.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make
%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
