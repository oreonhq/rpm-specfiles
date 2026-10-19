%global source0_hash a0c19ff7b763bb23c992bc76897d0053f26b42dfd953d33aedd6f59fd8e9591b
%global commit_long     795a815363a4401a30a1c0ef94f3381186172843
Name: dymo-cups-drivers-lw5xx
Version: 2.0.0.0
Release:        1%{?dist}
Summary:        DYMO LabelWriter 5xx Drivers for CUPS
License: GPL-2.0-or-later
URL: https://github.com/dymosoftware/Drivers
Source0:        https://github.com/dymosoftware/Drivers/archive/%{commit_long}.tar.gz#/Drivers-%{commit_long}.tar.gz
Patch0: dymo-cups-drivers-fix-fsf-address.patch
Patch1: dymo-cups-drivers-include-ctime.patch
Patch2: dymo-cups-drivers-replace-boolean-or-with-bitwise.patch
Patch3: dymo-cups-drivers-replace-deprecated-type.patch
Patch4: dymo-cups-drivers-append-cxxflags-dont-overwrite.patch
Patch5: dymo-cups-drivers-fprintf-format-specifier.patch
ExcludeArch: %{ix86}
Requires: cups
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  cups-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
This package contains DYMO LabelWriter 5xx series drivers for CUPS.
For LabelWriter 4xx and 3xx series drivers, please use the older
dymo-cups-drivers package.

%prep

%autosetup -p 1 -n Drivers-%{commit_long}

# Remove unwanted subfolders
rm -rf "LW4xx Linux"
rm -rf LW5xx_218_Beta
rm -rf LW5xx_Linux/src/boost

# move the subfolder we will build from up to the root
mv LW5xx_Linux/* ./
rmdir LW5xx_Linux

%build

autoupdate
autoreconf --force --install
chmod +x configure
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
