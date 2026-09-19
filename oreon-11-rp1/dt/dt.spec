%global source0_hash 1273b956706eaacb35d928b682610189d9aaf5d1c0a17a37b516a6794e4ef748

Name:		dt
Version:	26
Release:	1%{?dist}
Summary:	Generic data test program
License:	MIT
URL:		https://github.com/RobinTMiller/dt

%global git_tag dt.v%{version}
Source0:	%{URL}/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

BuildRequires:	gcc
BuildRequires:	libuuid-devel
BuildRequires:	make

%description
dt is a generic data test program used to verify proper operation of
peripherals, file systems, device drivers, or any data stream supported by the
operating system. In its' simplest mode of operation, dt writes and then
verifies its' default data pattern, then displays performance statistics and
other test parameters before exiting. Since verification of data is performed,
dt can be thought of as a generic diagnostic tool.

dt command lines are similar to the dd program, which is popular on most UNIX
systems. It contains numerous options to give the user control of various test
parameters.

dt has been used to successfully test disks, tapes, serial lines, parallel
lines, pipes, and memory mapped files. In fact, dt can be used for any device
that allows the standard open, read, write, and close system calls. Special
support is necessary for some devices, such as serial lines, for setting up the
speed, parity, data bits, etc.

Available documentation is located in %{_defaultdocdir}/%{name}. Sample
scripts and config data are installed in %{_datadir}/%{name}.

%global __requires_exclude_from ^%{_datadir}/%{name}/.*$
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}

%build
mkdir tmp
cd tmp
%make_build \
	CFLAGS="%{optflags} -I.. -DAIO -DMMAP -D__linux__ -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -DSCSI -DNVME -std=gnu99" \
	LIBS="-luuid" \
	OS=linux \
	VPATH=.. \
	-f ../Makefile.linux

%install
install -d -m755 $RPM_BUILD_ROOT%{_bindir}
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man8
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/html
install -m755 tmp/dt $RPM_BUILD_ROOT%{_bindir}
install -m644 Documentation/dt.man $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
install -m755 Scripts/dt? $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 data/pattern_* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 html/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/html

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Documentation/dt-UsersGuide.txt Documentation/ReleaseNotes-dt*.txt html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/%{name}.*.gz

%changelog
%autochangelog
