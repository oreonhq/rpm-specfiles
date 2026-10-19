%global source0_hash b2da03f1e09ccb981e5d0533f5abb5f259277ec9600e567cb166b1b138c66c02
Name:           rsvndump
Version:        0.6.2
Release:        1%{?dist}
Summary:        Remote Subversion repository dumping tool
License:        GPL-3.0-or-later
URL:            http://rsvndump.sourceforge.net
Source0:        http://downloads.sourceforge.net/rsvndump/rsvndump-%{version}.tar.bz2
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  subversion-devel
BuildRequires:  xmlto
# /oreon:deps
%description
rsvndump is a command line tool that is able to dump a subversion repository
that resides on a remote server. All data is dumped in the format that can be
read/written by svnadmin, so the data produced by rsvndump can easily be
imported into a new subversion repository.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-man
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
