%global source0_hash 6184d3f7535b34f08ea4e665b55498d5f76673d2a816cf2ee3eaae203c2d780b

Summary:	Apache module to send files efficiently
Name:		mod_xsendfile
Version:	0.12
Release:	35%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://tn123.org/%{name}/
Source0:	https://tn123.org/%{name}/%{name}-%{version}.tar.bz2
Source1:	xsendfile.conf
BuildRequires:  gcc
BuildRequires:	httpd-devel
Requires:       httpd-mmn = %{_httpd_mmn}

%description
%{name} is a small Apache2 module that processes X-SENDFILE headers
registered by the original output handler.

If it encounters the presence of such header it will discard all output and
send the file specified by that header instead using Apache internals
including all optimizations like caching-headers and sendfile or mmap if
configured.

It is useful for processing script-output of e.g. php, perl or any cgi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{_httpd_apxs} -c %{name}.c

%install
rm -rf $%{buildroot}
mkdir -p %{buildroot}/%{_httpd_moddir}
%{_httpd_apxs} -i -S LIBEXECDIR=%{buildroot}/%{_httpd_moddir} -n %{name} %{name}.la
mkdir -p %{buildroot}/%{_httpd_modconfdir}
cp -p %SOURCE1 %{buildroot}/%{_httpd_modconfdir}

%files
%doc docs/*
%config(noreplace) %{_httpd_modconfdir}/xsendfile.conf
%{_httpd_moddir}/%{name}.so

%changelog
%autochangelog
