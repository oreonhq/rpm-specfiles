%global source0_hash 0ca5efbfb43cfa40f6c8fea12d0d579390739abd44c2074a64f20afa961f3667
Name:           pgpdump
Version:        0.37
Release:        1%{?dist}
Summary:        PGP packet visualizer
License:        MIT
URL:            http://www.mew.org/~kazu/proj/pgpdump/
Source0:        http://www.mew.org/~kazu/proj/pgpdump/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
