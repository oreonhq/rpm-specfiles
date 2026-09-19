%global source0_hash 6dd7ef60338e3a26a5e5246f45aa001054e8fc984e48202e4b0698e571451ac0

Summary:        Lightweight command line SMTP e-mail client
Name:           sendemail
Version:        1.56
Release:        18%{?dist}
License:        GPL-2.0-or-later
URL:            http://caspian.dotconf.net/menu/Software/SendEmail/
Source0:        http://caspian.dotconf.net/menu/Software/SendEmail/sendEmail-v%{version}.tar.gz
Source1:        sendemail.1
Patch0:         sendemail-1.56-fix_ssl_version.patch
Patch1:         sendemail-1.56-add-ipv6-support.patch
Patch2:         sendemail-1.56-local-sendmail.patch
BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       perl(IO::Socket::SSL)
Provides:       sendEmail = %{version}-%{release}

%description
SendEmail is a lightweight, completely command line based, SMTP e-mail
client. It was designed to be used in bash scripts, batch files, Perl
programs and web sites, but is also quite useful in many other contexts.

SendEmail is written in Perl and is unique in that it requires no special
modules. It has a straight forward interface, making it very easy to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sendEmail-v%{version}
%patch -P0 -p1 -b .fix_ssl_version
%patch -P1 -p1 -b .add-ipv6-support
%patch -P2 -p1 -b .local-sendmail

%build
# Empty build section, most likely nothing required.

%install
install -D -p -m 0755 sendEmail $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/sendEmail
ln -s %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/sendEmail.1

%files
%doc CHANGELOG README
%{_bindir}/%{name}
%{_bindir}/sendEmail
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/sendEmail.1*

%changelog
%autochangelog
