%global source0_hash e945faa283a49f33af15de915a949c9273a230fc17154925364c547adab676ca

Name:           netstat-nat
Version:        1.4.10
Release:        33%{?dist}
Summary:        A tool that displays NAT connections

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.tweegy.nl/projects/netstat-nat/
Source0:        http://www.tweegy.nl/download/%{name}-%{version}.tar.gz
Patch0: netstat-nat-c99.patch
BuildRequires: make
BuildRequires:  gcc

%description
Netstat-nat is a small program written in C. It displays NAT connections,
managed by netfilter/iptables which comes with the > 2.4.x linux kernels.
The program reads its information from '/proc/net/nf_conntrack', which is
the temporary conntrack-storage of netfilter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod a-x ChangeLog README netstat-nat*
sed -i 's|install-docDATA install-man|install-man|g' Makefile.in

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc COPYING README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
