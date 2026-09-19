%global source0_hash 912c33da6b0dfb4add5867d13584a836f86d7fadb7fa4c05d344a39cbdcb38d3

Name: pcapdiff
Version: 0.1
Release:  41%{?dist}
Summary: Compares packet captures, detects forged, dropped or mangled packets

License: GPL-2.0-or-later AND GPL-3.0-or-later
URL: http://www.eff.org/testyourisp/pcapdiff/
Source0: http://www.eff.org/files/pcapdiff-%{version}.tar.gz
Source1: pcapdiff.py
Source2: printpackets
Patch0: pcapdiff-python3.patch

BuildArch: noarch
BuildRequires: python3-devel
Requires: python3-pcapy

%description
Pcapdiff is a tool developed by the EFF to compare two packet captures and
identify potentially forged, dropped, or mangled packets. Two technically-
inclined friends can set up packet captures (e.g. tcpdump or Wireshark) on
their own computers and produce network traffic between their two computers 
over the Internet. Later, they can run pcapdiff on the two packet capture 
files to identify suspicious packets for further investigation. See 
Detecting packet injection: a guide to observing packet spoofing by ISPs 
and EFF's Test Your ISP Project for more background.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn pcapdiff
%patch -P0 -p0

%build

%install
install -D -m 755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/pcapdiff
install -D -m 644 -p pcapdiff.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/pcapdiff.py
install -D -m 755 -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/printpackets
install -D -m 644 -p printpackets.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/printpackets.py
install -D -m 644 -p pcapdiff_helper.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/pcapdiff_helper.py

%files
%doc README COPYING.2 COPYING.3
%{_bindir}/pcapdiff
%{_bindir}/printpackets
%dir %{_datadir}/pcapdiff/
%{_datadir}/pcapdiff/*.py
#%{_datadir}/pcapdiff/*.pyc
#%{_datadir}/pcapdiff/*.pyo

%changelog
%autochangelog
