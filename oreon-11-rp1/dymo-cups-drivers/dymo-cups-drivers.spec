%global source0_hash c60797e7e986ca329f46e9a6ab1cb6382383952b15685ed69fd91f3c7ed64f71

%global short_version 1.4.0

Name: dymo-cups-drivers
Version: %{short_version}.5
Release: 25%{?dist}
Summary: DYMO LabelWriter Drivers for CUPS
License: GPL-2.0-or-later
URL: http://www.dymo.com

Source0: http://download.dymo.com/dymo/Software/Download%20Drivers/Linux/Download/dymo-cups-drivers-%{short_version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/matthiasbock/dymo-cups-drivers/pull/6
Patch0: dymo-cups-drivers-fix-fsf-address.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/2433fa303dd9925f8b36b18406863c56766c651b
Patch1: dymo-cups-drivers-replace-boolean-or-with-bitwise.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/d7ef90a48c61c898a3d69f353673d81d7540c892
Patch2: dymo-cups-drivers-unused-var-statusok.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/697cfb8115054fb95b9e91d54d68f47ee3805060
Patch3: dymo-cups-drivers-replace-deprecated-type.patch
# https://github.com/matthiasbock/dymo-cups-drivers/pull/7
Patch4: dymo-cups-drivers-autotools-deprecations.patch

# Patch files obtained from printer-driver-dymo Debian source package
Patch5: 0001-Inheritate-CXXFLAGS-from-the-environment-to-use-dpkg.patch
Patch6: 0002-Port-to-newer-cups-headers-ppd_file_t-is-only-define.patch
Patch7: 0005-Include-cups-sidechannel.h-for-cupsBackChannelRead-s.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cups-devel
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: sed
BuildRequires: make

Requires: cups

# Provide additional aliases for this package, consistent with dymo-cups-drivers-lw5xx package
Provides:       dymo-cups-drivers-lw4xx%{?_isa} = %{version}-%{release}
Provides:       dymo-cups-drivers-lw3xx%{?_isa} = %{version}-%{release}

%description
This package contains DYMO LabelWriter 4xx and 3xx series drivers for CUPS.
For LabelWriter 5xx series drivers, use the dymo-cups-drivers-lw5xx package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
autoreconf --force --install
# Must enable c++11 for el7
%{configure} CXXFLAGS="${CXXFLAGS} -std=c++11"
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog README docs/ samples/
%{_cups_serverbin}/filter/*
%{_datadir}/cups/model/*

%changelog
%autochangelog
