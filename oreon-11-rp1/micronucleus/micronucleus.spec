%global source0_hash e09d4e427cde4dac43c3bac2e6f91903ae205263b1598beb8cef4f786692b506

Name:           micronucleus
Version:        2.04
Release:        14%{?dist}
Summary:        Flashing tool for USB devices with Micronucleus bootloader

# The only thing that we package -- the command line tool -- has a MIT
# license block in each file. There's a License.txt (GPLv2 or GPLv3),
# but it's for different code. Oh well.
License:        MIT
URL:            https://github.com/micronucleus/micronucleus
Source0:        https://codeload.github.com/micronucleus/micronucleus/tar.gz/%{version}#/micronucleus-%{version}.tar.gz
Source1:        60-micronucleus.rules

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libusb)
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
This package ships a "micronucleus" command line tool. It is used to upload
programs to AVR ATtiny devices that utilize the Micronucleus boot loader.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# The supplied Makefile doesn't do anything useful. It sets compiler flags
# in a way that disallows overrides and then declares a patterns that
# defeat lazy compilation. Oh well.
cc -o micronucleus -Icommandline/library \
        %{optflags} $(pkg-config --cflags --libs libusb) \
        commandline/library/littleWire_util.c \
        commandline/library/micronucleus_lib.c \
        commandline/micronucleus.c

%install
mkdir -p %{buildroot}%{_bindir}
install -pm0755 micronucleus %{buildroot}%{_bindir}

# Upstream ships some attempt at udev rules, but they essentially consist
# of comments that are not true and chmod 666. Oh well.
mkdir -p %{buildroot}%{_udevrulesdir}
install -pm644 %{SOURCE1} %{buildroot}%{_udevrulesdir}

%files
%{_bindir}/micronucleus
%{_udevrulesdir}/60-micronucleus.rules
%doc commandline/Readme

%changelog
%autochangelog
