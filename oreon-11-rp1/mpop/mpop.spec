%global source0_hash 4ca0d1e0d01366fe3e0cf490d88d154df511278fb595638713be3ca675665855

Name:           mpop
Version:        1.4.21
Release:        %autorelease
Summary:        Client for receiving mail from POP3 mailboxes

License:        GPL-3.0-or-later
URL:            https://marlam.de/mpop/
Source0:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz
Source1:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz.sig
Source2:        https://marlam.de/key.txt

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# for %%gpgverify
BuildRequires:  gnupg2

%description
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a very
fast POP3 implementation, many authentication methods, good TLS/SSL
support, IPv6 support, and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --with-gnome-keyring
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS NOTES README THANKS
%doc doc/mpoprc.example
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.*
%{_bindir}/%{name}
%{_bindir}/%{name}d

%changelog
%autochangelog
