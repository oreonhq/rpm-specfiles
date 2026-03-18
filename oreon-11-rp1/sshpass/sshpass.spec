Summary:    Non-interactive SSH authentication utility
Name:       sshpass
Version:    1.09
Release:    12%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
Url:        http://sshpass.sourceforge.net/
Source0:    http://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/sshpass
%{_datadir}/man/man1/sshpass.1.gz
%doc AUTHORS COPYING ChangeLog NEWS

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.09-12
- Prepare for Oreon 11 (RP1)
