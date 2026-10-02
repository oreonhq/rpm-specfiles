%global source0_hash da99f8c573c4d9e63f493c7e24447126aea25b53b4c076ec79266874e29b1975

Summary: A remote mail retrieval and forwarding utility
Name: fetchmail
Version: 6.6.6
Release: 1%{?dist}
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
URL: http://www.fetchmail.info/
# For a breakdown of the licensing, see COPYING
License: GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
BuildRequires: gcc gettext-devel krb5-devel openssl-devel python3-devel
BuildRequires: make

%description
Fetchmail is a remote mail retrieval and forwarding utility intended
for use over on-demand TCP/IP links, like SLIP or PPP connections.
Fetchmail supports every remote-mail protocol currently in use on the
Internet (POP2, POP3, RPOP, APOP, KPOP, all IMAPs, ESMTP ETRN, IPv6,
and IPSEC) for retrieval. Then Fetchmail forwards the mail through
SMTP so you can read it through your favorite mail client.

Install fetchmail if you need to retrieve mail over SLIP or PPP
connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure --enable-POP3 --enable-IMAP --with-ssl --without-hesiod \
	--enable-ETRN --enable-NTLM --enable-SDPS --enable-RPA \
	--enable-nls --with-kerberos5 --with-gssapi \
	--enable-fallback=no
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove fetchmailconf stuff
rm -f $RPM_BUILD_ROOT%{_bindir}/fetchmailconf*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1*
rm -f $RPM_BUILD_ROOT%{python3_sitelib}/fetchmailconf.py*
rm -f $RPM_BUILD_ROOT%{python3_sitelib}/__pycache__/fetchmailconf*

%find_lang %name

%files -f %{name}.lang
%doc COPYING FAQ FEATURES NEWS NOTES README README.SSL TODO contrib/systemd
%{_bindir}/fetchmail
%{_mandir}/man1/fetchmail.1*

%changelog
%autochangelog
