%global source0_hash 09b730d87165763222e2c86454e5565ca7003161a5c275386d82d9390ba99a5a

Name:           pgpdump
Version:        0.36
Release:        1%{?dist}
Summary:        PGP packet visualizer
License:        MIT
URL:            http://www.mew.org/~kazu/proj/pgpdump/
Source0:        http://www.mew.org/~kazu/proj/pgpdump/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc

%description
pgpdump is a PGP packet visualizer which displays the packet format of
OpenPGP (RFC 4880) and PGP version 2 (RFC 1991).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGES README.md
%license COPYRIGHT
%{_bindir}/pgpdump
%{_mandir}/man1/pgpdump.1*

%changelog
%autochangelog
