%global source0_hash 75d43f586b7662ccca7d67bc67c52e25a341c6caef89a4804fedbeaee25a13b3

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}

Name:           mod_bw
Version:        0.8
Release:        39%{?dist}
Summary:        Bandwidth Limiter For Apache

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.ivn.cl/apache
Source0:        http://www.ivn.cl/apache/files/source/mod_bw-%{version}.tgz
Source1:        mod_bw.conf
Patch0:         mod_bw-httpd24.patch

BuildRequires:  gcc
BuildRequires:  httpd-devel
Requires:       httpd-mmn = %{_httpd_mmn}

%description
mod_bw is a bandwidth administration module for Apache httpd 2.x

* Restricts the number of simultaneous connections per vhost/dir
* Limits the bandwidth for files on vhost/dir

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mod_bw
%patch -P0 -p1 -b .httpd24
mv mod_bw.txt mod_bw.txt.iso8859
iconv -f ISO-8859-1 -t UTF-8 mod_bw.txt.iso8859 > mod_bw.txt 

%build
%{_httpd_apxs} -Wc,"%{optflags}" -c mod_bw.c

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 .libs/mod_bw.so \
                 $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_bw.so
install -Dpm 644 %{SOURCE1} \
                 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/mod_bw.conf

%files
%doc ChangeLog LICENSE TODO mod_bw.txt
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_bw.conf
%{_libdir}/httpd/modules/mod_bw.so

%changelog
%autochangelog
