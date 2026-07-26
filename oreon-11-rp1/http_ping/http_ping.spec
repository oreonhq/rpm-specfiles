%global source0_hash f8b95773aaed09839a44a1927f979a62752d57aace79da3846bfb73e6c9805e9

Name:           http_ping
Version:        20160309
Release:        20%{?dist}
Summary:        HTTP latency measuring utility

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.acme.com/software/http_ping/
Source0:        http://www.acme.com/software/http_ping/%{name}_09Mar2016.tar.gz

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires: make

%description
http_ping runs an HTTP fetch every few seconds, timing how long it
takes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
f=http_ping.1 ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%build
make %{?_smp_mflags} \
  CFLAGS="$RPM_OPT_FLAGS -DUSE_SSL $(pkg-config openssl --cflags)" \
  LDFLAGS="$(pkg-config openssl --libs)"

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 http_ping $RPM_BUILD_ROOT%{_bindir}/http_ping
install -Dpm 644 http_ping.1 $RPM_BUILD_ROOT%{_mandir}/man1/http_ping.1

%files
%doc README
%{_bindir}/http_ping
%{_mandir}/man1/http_ping.1*

%changelog
%autochangelog
