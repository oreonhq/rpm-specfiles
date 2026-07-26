%global source0_hash 1033d1435cb080a740d3c5b3365422b8c318f4e04955bca35f7d21a116f16160

%global upstream_name printer-driver-ptouch

Name:           ptouch-driver
Version:        1.7.1
Release:        3%{?dist}
Summary:        CUPS driver for Brother P-touch label printers

License:        GPL-2.0-or-later
URL:            https://github.com/philpem/printer-driver-ptouch
Source0:        https://github.com/philpem/printer-driver-ptouch/releases/download/v%{version}/%{upstream_name}-%{version}.tar.gz

# gcc is no longer in buildroot by default (needed for rastertoptch filter)
BuildRequires:  gcc
# uses autosetup
BuildRequires:  git-core
# uses make
BuildRequires:  make
BuildRequires:  cups-devel
BuildRequires:  automake
# ensure we have postscript tags for drivers
BuildRequires:  python3-cups
BuildRequires:  perl(XML::LibXML)
BuildRequires:  libpng-devel
Requires:       cups

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

# On 64bits, we need to install into lib, not lib64
# (see _cups_serverbin macro from cups-devel)
# and this package for some reason uses libdir
%configure --libdir=%{_prefix}/lib

%make_build

%install
%make_install

%files
%license COPYING
%{_cups_serverbin}/filter/rastertoptch
%doc AUTHORS ChangeLog NEWS README

%files foomatic
%{_datarootdir}/foomatic/db/source/driver/ptouch-*.xml
%{_datarootdir}/foomatic/db/source/printer/Brother-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-PT-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-PTQL-*.xml
%{_datarootdir}/foomatic/db/source/opt/Brother-QL-*.xml

%changelog
%autochangelog
