%global source0_hash b56288b4bd0ef0cba7756708df3c193a4879e0733432380effde483e1db1c128

%define prerelease r77
%define relcand rc2
%define realname xmpphp
%define REALNAME XMPPHP

Name:           php-%{realname}
Version:        0.1
Release:        0.37.%{relcand}.%{prerelease}%{?dist}
Summary:        XMPPHP is the successor to Class.Jabber.PHP

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://code.google.com/p/xmpphp/
Source0:        http://xmpphp.googlecode.com/files/%{realname}-%{version}%{relcand}-%{prerelease}.tgz

Patch0:         %{name}-php7.patch

BuildArch:      noarch

Requires:       php-curl
Requires:       php-date
Requires:       php-dom
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-session
Requires:       php-simplexml
Requires:       php-spl
Requires:       php-xml

%description
XMPPHP is the successor to Class.Jabber.PHP which can connect to XMPP
1.0 server (google talk, jabber.orgf, LJ Talk, etc, supports TLS,
several XML processing approaches and supported styles, persistent
connection, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{realname}-%{version}%{relcand}-%{prerelease}

%patch -P0 -p1

%build
# Empty build

%install
rm -rf %{buildroot}

# Library
mkdir -p %{buildroot}%{_datadir}/php/%{realname}
install -p -m 644 %{REALNAME}/*.php %{buildroot}%{_datadir}/php/%{realname}/

# Examples (for doc)
mkdir examples
cp -p *.php examples

%files
%doc README LICENSE examples
%{_datadir}/php/%{realname}

%changelog
%autochangelog
