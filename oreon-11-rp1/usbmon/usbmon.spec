%global source0_hash 30985b48f3c29901a1ed2a18af6b1f70d290d5d45cc44c5afdc3ade6d1816b84

Name:		usbmon
Version:	6.1
Release:	23%{dist}
Summary:	A basic front-end to usbmon

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://people.redhat.com/zaitcev/linux/
Source:		http://people.redhat.com/zaitcev/linux/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
The usbmon program collects and prints a trace of USB transactions as they
occur between the USB core and HCDs. Analyzing the trace helps to debug the
kernel USB stack, device firmware, and applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" 
# Builds outside of the Koji/Brew fail unless we mkdir. How do other RPMs work?
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 -t $RPM_BUILD_ROOT/%{_mandir}/man8 usbmon.8
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -p -m 755 -t $RPM_BUILD_ROOT/%{_sbindir} usbmon

%files
%doc README COPYING
%{_sbindir}/usbmon
%{_mandir}/man8/usbmon.8*

%changelog
%autochangelog
