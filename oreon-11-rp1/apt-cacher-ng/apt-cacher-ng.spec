%global source0_hash b0823eb2ddf6283ac3ebf30fb22db2a285d2601f91bacf0b387747d6adbafa78

%undefine __cmake_in_source_build
%global debian_release 1

Name:             apt-cacher-ng
Version:          3.7.5
Release:          2%{?dist}
Summary:          Caching proxy for package files from Debian

License:          BSD-4-Clause
URL:              http://www.unix-ag.uni-kl.de/~bloch/acng/
Source0:          http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}.orig.tar.xz
Source1:          http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%{version}-%{debian_release}.debian.tar.xz
Source2:          %{name}.conf
Source3:          %{name}.rpmlintrc
# Purpose: versioning the private shared library to comply with Fedora Policy
Patch0:           supacng.patch

BuildRequires:    gcc-c++
BuildRequires:    zlib-devel
BuildRequires:    bzip2-devel
BuildRequires:    xz-devel
BuildRequires:    fuse-devel
BuildRequires:    cmake
BuildRequires:    openssl-devel
BuildRequires:    boost-devel
BuildRequires:    systemd
BuildRequires:    systemd-devel
BuildRequires:    libevent-devel
BuildRequires:    c-ares-devel
BuildRequires:    perl-generators

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Requires:         crontabs
Requires:         logrotate
Requires:         xz

%description
A caching proxy. Specialized for package files from Linux distributors,
primarily for Debian (and Debian based) distributions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

tar xfvJ %{SOURCE1}

# Replace all instances of /usr/lib/apt-cacher-ng/ with /usr/libexec/apt-cacher-ng/
find debian -type f -exec sed -i "s#/usr/lib/apt-cacher-ng#/usr/libexec/apt-cacher-ng#g" '{}' \;

# Fix this here until UsrMerge is done in Debian too (which will take forever)
sed -i "s#/lib/systemd/system#/usr/lib/systemd/system#" systemd/CMakeLists.txt

%build
%cmake -DLIBDIR=%{_libexecdir}/%{name} -DSDINSTALL=on -DACNG_CACHE_DIR=%{_var}/cache/%{name} -DACNG_LOG_DIR=%{_var}/log/%{name}
sed -i 's/HAVE_STRLCPY/HAVE_STRLCPY 1/' */acsyscap.h
%cmake_build

%install
%cmake_install
%if "%{_bindir}" == "%{_sbindir}"
test -d %{buildroot}/usr/sbin && mv %{buildroot}/usr/sbin %{buildroot}/usr/bin
%endif

# we do not want an unversioned .so or a -devel package
rm -vf %{buildroot}%{_libdir}/libsupacng.so

## install extra scripts
mkdir -p %{buildroot}%{_libexecdir}/%{name}/
install -pm 0755 scripts/*.pl %{buildroot}%{_libexecdir}/%{name}/

## add useful content from Debian packaging
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
install -D -pm 0755 debian/apt-cacher-ng.cron.daily %{buildroot}%{_sysconfdir}/cron.daily/%{name}

install -D -pm 0644 debian/apt-cacher-ng.default    %{buildroot}%{_sysconfdir}/default/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -D -pm 0644 debian/apt-cacher-ng.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}/%{_sysusersdir}/
install -pm 644 %{SOURCE2} %{buildroot}/%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_var}/cache/%{name}
mkdir -p %{buildroot}%{_var}/lib/%{name}
mkdir -p %{buildroot}%{_var}/log/%{name}

# without this I would only get 404 for every single request
sed -i '/^Remap-debrep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf
sed -i '/^Remap-uburep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf
sed -i '/^Remap-kxlrep/s/;/# ;/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf

# https://fedoraproject.org/wiki/Changes/Deprecate_TCP_wrappers
# Warning: configured to use libwrap filters but feature is not built-in.
# --> this is lekely a bug upstream
sed -i 's/^# UseWrap: 0/UseWrap: 0/' %{buildroot}%{_sysconfdir}/apt-cacher-ng/acng.conf

%pre

%post
%sysusers_create %{name}.conf
%tmpfiles_create %{name}.conf
chown -R %{name}:%{name} /var/log/%{name}/
chown -R %{name}:%{name} /var/cache/%{name}/
chown -R %{name}:%{name} /run/%{name}/
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%{_docdir}/%{name}/
%dir %{_var}/lib/%{name}/
%attr(755,%{name},%{name}) %dir %{_var}/log/%{name}/
%attr(755,%{name},%{name}) %dir %{_var}/cache/%{name}/

%exclude %{_sysconfdir}/avahi/services/%{name}.service
%config(noreplace) %{_sysconfdir}/apt-cacher-ng/
%config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(755,%{name},%{name}) %dir %{_rundir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_libexecdir}/%{name}/
%{_libdir}/libsupacng.so*
%{_sbindir}/apt-cacher-ng
%{_mandir}/man8/*

%changelog
%autochangelog
