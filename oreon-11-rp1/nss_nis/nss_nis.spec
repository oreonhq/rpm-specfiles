%global source0_hash 1c62306a379e8e6720fcb464b6c29883a93203df28657d9c8195e6160b95ec24

Name:           nss_nis
Version:        3.2
Release:        9%{?dist}
Summary:        Name Service Switch (NSS) module using NIS
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Url:            https://github.com/thkukuk/libnss_nis
Source:         https://github.com/thkukuk/libnss_nis/archive/v%{version}.tar.gz

# https://github.com/systemd/systemd/issues/7074
# https://bugzilla.redhat.com/show_bug.cgi?id=1829572
Source2:        nss_nis.conf

BuildRequires: make
BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:  systemd

# I'd recommend an explicit conflict with different versions of the package
# to ensure that 64bit and 32bit packages are equal and compatible
Conflicts:      %{name} < %{version}-%{release}


%description
The nss_nis Name Service Switch module uses the Network Information System (NIS)
to obtain user, group, host name, and other data.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n libnss_nis-%{version}

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure --libdir=%{_libdir} --includedir=%{_includedir}
%make_build

%install
%make_install
rm  %{buildroot}/%{_libdir}/libnss_nis.{a,la}
rm  %{buildroot}/%{_libdir}/libnss_nis.so

install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-logind.service.d/nss_nis.conf
install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-userdbd.service.d/nss_nis.conf

%check
make check

%files
%{_libdir}/libnss_nis.so.2
%{_libdir}/libnss_nis.so.2.0.0
%{_unitdir}/systemd-logind.service.d/*
%{_unitdir}/systemd-userdbd.service.d/*

%license COPYING
%doc NEWS


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2-9
- Prepare for Oreon 11 (RP1)
