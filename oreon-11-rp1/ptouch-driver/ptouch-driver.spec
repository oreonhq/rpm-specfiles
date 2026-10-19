%global source0_hash 1033d1435cb080a740d3c5b3365422b8c318f4e04955bca35f7d21a116f16160
%global upstream_name printer-driver-ptouch
Name:           ptouch-driver
Version:        1.7.1
Release:        1%{?dist}
Summary:        CUPS driver for Brother P-touch label printers
License:        GPL-2.0-or-later
URL:            https://github.com/philpem/printer-driver-ptouch
Source0:        https://github.com/philpem/%{upstream_name}/releases/download/v%{version}/%{upstream_name}-%{version}.tar.gz
Requires:       cups
# oreon:deps
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl(XML::LibXML)
BuildRequires:  python3-cups
# /oreon:deps
%description
This is a CUPS raster filter for Brother P-touch label printers.  It is
meant to be used by the PostScript Description files of the drivers from
the foomatic package.

%package        foomatic
Summary:        Foomatic database data for Brother P-touch label printers
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       foomatic-db >= 4.0-25.20101123.fc15
%description    foomatic
This package contains foomatic database XML entries to generate PPDs
for driving the family of Brother P-touch label printers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{upstream_name}-%{version}

%build

%set_build_flags
./autogen.sh
%configure --libdir=%{_prefix}/lib
%make_build
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ptouch-driver-foomatic -f %{oreon_filedir}/ptouch-driver-foomatic.list

%changelog

%autochangelog
