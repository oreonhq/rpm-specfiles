%global source0_hash 85af5d3d9bf5fb01d1ba04c814de3b43660cb0bb54122517429113cdb2b198fe

Name:           mod_auth_token
Version:        1.0.5
Release:        40%{?dist}
Summary:        Token based URI access module for Apache

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://code.google.com/p/mod-auth-token/
Source0:        http://mod-auth-token.googlecode.com/files/%{name}-%{version}.tar.gz

Patch0:         mod_auth_token-1.0.5-autotools.patch
Patch1:         mod_auth_token-1.0.5-fix-Wformat.patch
Patch2:         mod_auth_token-1.0.5-apache24.patch
Patch3:         mod_auth_token-1.0.5-add_ip_limitation_config.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  libxcrypt-devel

%description
mod_auth_token allows you to generate URIS for a determined
time window, you can also limit them by IP.  This is very
useful to handle file downloads, as generated URIS can't be
hot-linked (after it expires), also it allows you to protect
very large files that can't be piped trough a script languages
due to memory limitation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
rm -fr .svn*
find . -type f -and -not -xtype l -print0 | xargs -0 dos2unix -k
mv configure.{in,ac}
mkdir -p m4
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog README
%license AUTHORS LICENSE
%{_libdir}/httpd/modules/%{name}.so

%changelog
%autochangelog
