%global source0_hash 8daa0a2a63d13d60cc791b4be049c261d7b1d7a84c320ddcbb7ac5eaf73bebd2
%global forgeurl https://github.com/antirez/%{name}
%global commit          0c3bb23eb447d4ae47c7013346fa6fa97482bb1d
%forgemeta
Name:           dump1090
Version:        0
Release:        1%{?dist}
Summary:        Simple Mode S decoder specifically designed for RTLSDR devices
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        dump1090.md
Source2:	testoutput.gz
Source3:	testoutput2.gz
Patch0:         dump1090-share.patch
Patch1:         dump1090-sigwin.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pandoc
BuildRequires:  rtl-sdr-devel
# /oreon:deps
%description
Dump 1090 is a Mode S decoder specifically designed for RTLSDR devices.

Install this to use your RTL-SDR to track commercial aircraft in your area.

The main features are:

* Robust decoding of weak messages, with mode1090 many users observed
  improved range compared to other popular decoders.
* Network support: TCP30003 stream (MSG5...), Raw packets, HTTP.
* Embedded HTTP server that displays the currently detected aircraft on
  Google Map.
* Single bit errors correction using the 24 bit CRC.
* Ability to decode DF11, DF17 messages.
* Ability to decode DF formats like DF0, DF4, DF5, DF16, DF20 and DF21
  where the checksum is xored with the ICAO address by brute forcing the
  checksum field using recently seen ICAO addresses.
* Decode raw IQ samples from file (using --ifile command line switch).
* Interactive command-line interface mode where aircraft currently detected
  are shown as a list refreshing as more data arrives.
* CPR coordinates decoding and track calculation from velocity.
* TCP server streaming and receiving raw data to/from connected clients
  (using --net).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
# Extract LICENSE from source
# https://github.com/antirez/dump1090/issues/164
sed -ne 's/^ \*//' -e '/Copyright/,/DAMAGE\./p' anet.h >LICENSE
pandoc -s -tman -o %{name}.1 %{SOURCE1}
zcat %{SOURCE2} >testoutput
zcat %{SOURCE2} %{SOURCE3} >testoutput2

%build

%set_build_flags
%make_build 
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm 755 dump1090  %{buildroot}%{_bindir}
install -pm 644 gmap.html  %{buildroot}%{_datadir}/%{name}
cp -pr tools  %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 %{name}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

./dump1090 --ifile testfiles/modes1.bin >testout
diff testout testoutput || diff testout testoutput2
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
