%global source0_hash 533bf9c9543427ff23c7460dbddbf839f7e69460df285a3fa83eb4d86cf8776a

Summary:          Simple tool to list expiring or expired X.509 certificates
Name:             x509watch
Version:          0.6.1
Release:          19%{?dist}
License:          GPL-2.0-or-later
URL:              https://ftp.robert-scheck.de/linux/%{name}/
Source:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Requires:         %{_bindir}/openssl
Requires:         %{_sbindir}/sendmail
Requires(post):   systemd >= 197
Requires(preun):  systemd >= 197
Requires(postun): systemd >= 197
BuildRequires:    systemd >= 197
BuildRequires:    make
BuildRequires:    perl-generators
BuildArch:        noarch

%description
x509watch is a simple command line application, written in Perl, that can be
used to list soon expiring or already expired X.509 certificates, such as e.g.
SSL certificates. All certificates are searched by default in the standard PKI
directory, but any other directory can be specified as parameter. Only Base64
encoded DER and PEM X.509 certificates are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun %{name}.timer

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
%autochangelog
