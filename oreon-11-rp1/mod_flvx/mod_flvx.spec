%global source0_hash b20d4e03ccc25c4dd104630ec0afd95155c2ac1f91cc130d5fe1066574d86e04
%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir     %%{_libdir}/httpd/modules}}
%global gitver  48bb878
Summary:        FLV progressive download streaming for the Apache HTTP Server
Name:           mod_flvx
Version:        0
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://tperspective.blogspot.com/2009/02/apache-flv-streaming-done-right.html
Source0:        osantana-%{name}-%{gitver}.tar.gz
Source1:        flvx.conf
Patch0:         mod_flvx-c99.patch
Requires:       httpd-mmn = %{_httpd_mmn}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  httpd-devel
# /oreon:deps
%description
FLV streaming means it can be sought to any position during video, and
browser (Flash player) will buffer only from this position to the end.
Thus streaming allows to skip boring parts or see video ending without
loading the whole file, which simply saves bandwidth. Even H264 is more
efficient, FLV is still a common container format for videos, because
H264 is supported by Flash since version 9.115.

For using FLV streaming on the web, a pseudo-streaming compliant Flash
player, such as Flowplayer, is needed. Streaming requires that the FLV
has embedded key-frame markers (meta-data), that can be injected by any
supported tool, e.g. flvtool2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n osantana-%{name}-%{gitver}

%build

%{_httpd_apxs} -Wc,-Wall -c %{name}.c
%install
install -D -p -m 755 .libs/%{name}.so $RPM_BUILD_ROOT%{_httpd_moddir}/%{name}.so
head -n 5 %{SOURCE1} > 10-flvx.conf
sed -e '4,5d' %{SOURCE1} > flvx.conf
touch -c -r %{SOURCE1} 10-flvx.conf flvx.conf
install -D -p -m 644 10-flvx.conf $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-flvx.conf
install -D -p -m 644 flvx.conf $RPM_BUILD_ROOT%{_httpd_confdir}/flvx.conf
sed -e 's/\r//' README.md > README
touch -c -r README.md README
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
