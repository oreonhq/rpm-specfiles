%global source0_hash f1813561379bbb8f893e75314635ba5714af2ea7b773977a55abfc323beec292

%global srcname apache-mod-markdown
%global commit 1bf4fb4df6029e8fdfc5ce46f14e99d951230450
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		mod_markdown
Version:	1.0.4
Release:	14.20211115git%{shortcommit}%{?dist}
# Automatically converted from old format: ASL 2.0
License:	Apache-2.0
Summary:	Markdown content filters for the Apache HTTP Server
URL:		https://github.com/hamano/%{srcname}
Source0:	https://github.com/hamano/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Source1:	71_mod_markdown.conf
# https://github.com/hamano/apache-mod-markdown/issues/36
Patch0:		%{name}.diff
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	httpd-devel
# libmarkdown-devel
BuildRequires:	pkgconfig(libmarkdown)

%description
mod_markdown is Markdown filter module for Apache HTTPD Server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%build
autoupdate
autoreconf -vfi
%configure \
    --with-apxs=%{_bindir}/apxs \
    --with-discount=%{_prefix}
sed -i "s|/usr/lib$|%{_libdir}|g" Makefile
%make_build

%install
mkdir -p %{buildroot}%{_httpd_moddir}
mkdir -p %{buildroot}%{_httpd_modconfdir}
%{_libdir}/httpd/build/instdso.sh SH_LIBTOOL='%{_libdir}/apr-1/build/libtool' mod_markdown.la %{buildroot}%{_httpd_moddir}
install -Dm 0644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}

%files
%license COPYING
%doc README.md
%{_httpd_moddir}/mod_markdown.so
%config(noreplace) %{_httpd_modconfdir}/71_mod_markdown.conf

%changelog
%autochangelog
