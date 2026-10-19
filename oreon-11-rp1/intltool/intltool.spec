%global source0_hash 67c74d94196b153b774ab9f89b2fa6c6ba79352407037c8c14d5aeb334e959cd
Name: intltool
Summary:        Utility for internationalizing various kinds of data files
Version: 0.51.0
Release:        1%{?dist}
License: GPL-2.0-or-later WITH Autoconf-exception-generic
Source0:        https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
URL: https://launchpad.net/intltool
BuildArch: noarch
Requires: patch
Requires: automake
Requires: gettext-devel
Requires: perl(Getopt::Long)
Requires: perl(XML::Parser)
Patch: intltool-perl5.26-regex-fixes.patch
Patch: intltool-merge-Create-cache-file-atomically.patch
Patch: intltool_distcheck-fix.patch
Patch: intltool-cache-race.patch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl-generators
# /oreon:deps
%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

if ! make check; then
    find . -type f -name 'test-suite.log' | while read trs; do
	echo "BEGIN " ${trs}; cat ${trs} 1>&2;
    done
    echo  "Exiting abnormally due to make check failure above" 1>&2
    exit 1
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.51.0-1
- Import
