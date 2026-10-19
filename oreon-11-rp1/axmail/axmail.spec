%global source0_hash 257f2590fd509ca9c8742e689242bc289f74d72036d7ffa130516a2de5bb4f78
Summary:        UROnode addon - an SMTP mailbox
Name: axmail
Version: 2.9
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://axmail.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: axmail-README.fedora
Patch: axmail-2.9-install-fix.patch
Patch: axmail-2.8-gcc-10-fix.patch
Patch: axmail-c99.patch
Provides: bundled(mailx) = 5.3b
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
# /oreon:deps
%description
axMail is an add-on to URONode or LinuxNode that provides you and your
users with the ability to send and receive SMTP-based email. It can also
be used with a HylaFax server, making it possible to send and receive faxes
using just a dumb terminal. Setup is easy and many options are available
for the SysOp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Copy Fedora readme into place
cp -p %{SOURCE1} README.fedora

# Removing old license file, this was permitted by upstream N1URO and
# will be fixed in next upstream release. The package is now licensed
# under GPLv2+ as stated in the copying.
rm -f .COPYING

# Rename welcome.txt to axmail-welcome.txt to prevent possible future conflicts
mv -f etc/welcome.txt etc/axmail-welcome.txt

%build

%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
%install
%make_install DESTDIR="%{buildroot}" MANDIR="%{_mandir}" \
  SBINDIR="%{_sbindir}" install
mkdir -p %{buildroot}%{_var}/lock
touch %{buildroot}%{_var}/lock/axmail
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
