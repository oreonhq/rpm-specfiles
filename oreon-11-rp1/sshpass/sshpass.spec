Summary:    Non-interactive SSH authentication utility
Name:       sshpass
Version:    1.09
Release:    12%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
Url:        http://sshpass.sourceforge.net/
Source0:    http://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 71746e5e057ffe9b00b44ac40453bf47091930cba96bbea8dc48717dedc49fb7
%global source0_file sshpass-1.09.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires:  gcc
%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sshpass-1.09.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "71746e5e057ffe9b00b44ac40453bf47091930cba96bbea8dc48717dedc49fb7" || { echo "oreon: Source0 SHA256 mismatch for sshpass-1.09.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
