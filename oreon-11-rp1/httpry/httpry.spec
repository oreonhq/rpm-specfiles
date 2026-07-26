%global source0_hash ef53454f895f68005f7b9ab634d1b433c4df839eacea9109e4ee48d4296fb613

%global     srcname     httpry

Summary:    A specialized packet sniffer designed for displaying and logging HTTP traffic
Name:       %{srcname}
Version:    0.1.8
Release:    27%{?dist}
License:    GPL-2.0-only and BSD-3-Clause
URL:        http://dumpsterventures.com/jason/%{srcname}/
Source:     http://dumpsterventures.com/jason/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: libpcap-devel
BuildRequires: make

%description
httpry is a specialized packet sniffer designed for displaying and logging
HTTP traffic. It is not intended to perform analysis itself, but to capture,
parse, and log the traffic for later analysis. It can be run in real-time
displaying the traffic as it is parsed, or as a daemon process that logs to
an output file. It is written to be as lightweight and flexible as possible,
so that it can be easily adaptable to different applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
sed -i 's/^CCFLAGS.*$/CCFLAGS = \$(RPM_OPT_FLAGS) \$(RPM_LD_FLAGS) -I\/usr\/include\/pcap -I\/usr\/local\/include\/pcap/' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -Dp -m 0755 %{srcname} ${RPM_BUILD_ROOT}%{_sbindir}/%{srcname}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/ChangeLog doc/COPYING doc/format-string doc/method-string doc/perl-tools doc/README
%{_sbindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
