%global source0_hash c3657b77dad57cb13e96998ca5b61e0e59412423657240d15a354a9b21dcaf8a

Name:     mod_mono
Version:  3.13
Release:  20%{?dist}
Summary:  A module to deploy an ASP.NET application on Apache with Mono

License:  MIT
URL:      http://www.mono-project.com/docs/web/mod_mono/
Source0:  http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Source1:  %{name}-tmpfiles.conf
Patch0:   mod_mono-varrun.patch
Patch1:   mod_mono-ignoresbin.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: httpd-devel
BuildRequires: mono-devel
BuildRequires: xsp-devel
BuildRequires: pkgconfig
BuildRequires: apr-devel
# For the _tmpfilesdir macro.
BuildRequires: systemd

Requires: httpd >= 2.2
Requires: mono-core
Requires: xsp

ExclusiveArch: %mono_arches

%description
mod_mono allows Apache to serve ASP.NET pages by proxying the requests
to a slightly modified version of the XSP server, called mod-mono-server,
that is installed along with XSP

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .varrun
%patch -P1 -p1 -b .ignoresbin

# fixup character set
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && \
touch -r ChangeLog ChangeLog.conv && \
mv -f ChangeLog.conv ChangeLog

%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install APXS_SYSCONFDIR="%{_sysconfdir}/httpd/conf.d/"
find %{buildroot} -type f -name "*.la" -delete

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/httpd/modules/mod_mono.so*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_mono.conf
%dir %attr(-,apache,apache) /run/%{name}/
%{_tmpfilesdir}/%{name}.conf
%doc %{_mandir}/man8/mod_mono.8*

%changelog
%autochangelog
