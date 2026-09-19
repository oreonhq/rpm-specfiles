%global source0_hash 0d6929e2c94abb33ace303e59cf7e67b44ab3e23231fb0e64f810ff7c6a30ee7

%global gitsnap 20140818gitdf0ddc3

Name:           bind-to-tinydns
Version:        0.4.3
Release:        42.%{gitsnap}%{?dist}
Summary:        Convert DNS zone files in BIND format to tinydns format

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.erat.org/
Source0:        bind-to-tinydns-%{version}-%{gitsnap}.tar.bz2
Patch0:         bind-to-tinydns-0.4.3-cflags.patch

BuildRequires: gcc
BuildRequires: make

%description
This is a program that parses zone files used by the BIND DNS server and
converts them to the native format of the tinydns component of Dan Bernstein's
djbdns DNS server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 bind-to-tinydns $RPM_BUILD_ROOT%{_bindir}/bind-to-tinydns

%files
%doc README COPYING
%{_bindir}/bind-to-tinydns

%changelog
%autochangelog
