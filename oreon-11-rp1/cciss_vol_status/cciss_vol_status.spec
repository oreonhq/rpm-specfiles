%global source0_hash a49abbfde6369416ac3d71bca6f60f342584eb99c786c080f8722ad19a17f91f

Name:           cciss_vol_status
Version:        1.12
Release:        20%{?dist}
Summary:        Show status of logical drives attached to HP SmartArray controllers

License:        GPL-2.0-or-later
URL:            http://cciss.sourceforge.net/#cciss_utils
Source0:        http://downloads.sourceforge.net/cciss/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: make
%description
A very lightweight program to report the status of logical drives on
Smart Array controllers and also fibre channel attached MSA1000.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
%autochangelog
