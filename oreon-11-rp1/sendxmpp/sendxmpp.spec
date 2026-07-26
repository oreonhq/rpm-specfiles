%global source0_hash dfaf735b4585efd6b3b0f95db31203f9ab0fe607b50e75c6951bc18a6269837d

Summary:        Perl script to send XMPP messages
Name:           sendxmpp
Version:        1.24
Release:        24%{?dist}
License:        GPL-2.0-only
URL:            https://sendxmpp.hostname.sk/
Source:         https://github.com/lhost/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         sendxmpp-1.24-git20250721.patch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Net::XMPP)
BuildArch:      noarch

%description
Sendxmpp is a Perl script to send XMPP (Jabber) messages from the command
line, similar to what mail(1) does for mail. Messages can be sent both to
individual recipients and chat rooms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
