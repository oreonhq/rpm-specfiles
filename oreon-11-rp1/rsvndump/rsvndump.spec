%global source0_hash dd5b0b3cc9c48d2b85e3948cd5f99b22577a429603d40de29ec6264d75d535b4

Name:           rsvndump
Version:        0.6.1
Release:        10%{?dist}
Summary:        Remote Subversion repository dumping tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://rsvndump.sourceforge.net
Source0:        http://downloads.sourceforge.net/rsvndump/rsvndump-%{version}.tar.bz2

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  subversion-devel
BuildRequires:  xmlto

%description
rsvndump is a command line tool that is able to dump a subversion repository
that resides on a remote server. All data is dumped in the format that can be
read/written by svnadmin, so the data produced by rsvndump can easily be
imported into a new subversion repository.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --enable-man
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog THANKS
%{_bindir}/rsvndump
%{_mandir}/man1/rsvndump.1*

%changelog
%autochangelog
