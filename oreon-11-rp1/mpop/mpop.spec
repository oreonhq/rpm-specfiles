%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source1_hash 29dd0aec9bce4bfb598a2f9ae2fd4c44ebf49f2138bf16ef6dca729423051047
%global source0_hash 02fc2ff44f62b8fbf427ed6d8b16e0d374751198254fb1e6ad36eb6d9a938017
Name:           mpop
Version:        1.4.23
Release:        1%{?dist}
Summary:        Client for receiving mail from POP3 mailboxes
License:        GPL-3.0-or-later
URL:            https://marlam.de/mpop/
Source0:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz
Source1:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz.sig
Source2:        https://marlam.de/key.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
