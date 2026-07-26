%global source0_hash b65d6706b537f4a1807716ed96e53b5813191593bbf4d7137d8eb069abe9c342

Name:       ramond
Version:    0.5
Release:    31%{?dist}
Summary:    Router advertisement monitoring daemon
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://%{name}.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2 
Source1:    %{name}.service
# Respect distribution compiler options
Patch0:     %{name}-0.5-Respect-CFLAGS-and-LDFLAGS.patch
# Fix compiler warnings
Patch1:     %{name}-0.5-Fix-compiler-warnings-about-unused-variables-and-imp.patch
# Fix compiler warnings
Patch2:     %{name}-0.5-Fix-warnings-about-incompatible-types.patch
# Fix compiler warnings, undefined behavior on glibc
Patch3:     %{name}-0.5-Do-not-unset-variables-by-setenv.patch
# Fix building with GCC 10
Patch4:     %{name}-0.5-Fix-building-with-GCC-10.patch
BuildRequires:  apr-devel
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

# Do not find depenendecies in the documentation
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc

%description
This program monitors IPv6 networks for router advertisements. When an
advertisement is received, a configurable action occurs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%global _hardened_build 1
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
sed -e '/All Routers Mac List/,/<\/ramond>/ c </ramond>' \
    <ramond.conf.example >ramond.conf

%install
install -d '%{buildroot}%{_sbindir}'
install -m 0755 -t '%{buildroot}%{_sbindir}' %{name}
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' %{name}.conf
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc CHANGELOG README THANKS
%doc demo.pl ramond.conf.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
