%global source0_hash 36ddc7f64cb3df2ca4170627c6e0f0dea33d1a6d0730629dff6f5c633f2006f9
%if 0%{?el7}
%global _hardened_build 1
%endif
Name:       proxychains-ng
Version:    4.17
Release:        1%{?dist}
Summary:        Redirect connections through proxy servers
License:    GPL-2.0-or-later
URL:        https://github.com/rofl0r/proxychains-ng
Source0:        http://ftp.barfooze.de/pub/sabotage/tarballs/proxychains-ng-%{version}.tar.xz
Patch1:     979bfef42974f80352566cbad1fd1be4ec33cd70.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
ProxyChains NG is based on ProxyChains.

ProxyChains NG hooks network-related (TCP only) libc functions in dynamically
linked programs via a preloaded DSO (dynamic shared object) and redirects the
connections through one or more SOCKS4a/5 or HTTP proxies.

Since Proxy Chains NG relies on the dynamic linker, statically linked binaries
are not supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --libdir=%{_libdir}/%{name}
%make_build
%install
%make_install install-config
ln -s ../..%{_bindir}/proxychains4 %{buildroot}%{_bindir}/proxychains
chmod +x %{buildroot}%{_libdir}/%{name}/libproxychains4.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
