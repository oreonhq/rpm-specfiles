%global source0_hash 293b6191821641d3ed6248206f8f9df0bf46e6ee2cf8b4dd97cfd1d5909edb9a
Name:          zsync
Summary:        a file transfer program using the same algorithm as rsync over HTTP
URL:           https://zsync.moria.org.uk/
License:       Artistic-2.0 and Zlib and NTP and LicenseRef-Fedora-Public-Domain
Version:       0.8.0
Release:        1%{?dist}
Source0:        https://zsync.moria.org.uk/download/%{name}-%{version}.tar.bz2
Patch0:        zsync-0.6.3-fix-tests.patch
Provides:      bundled(zlib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
zsync is a file transfer program. It allows you to download a file from a
remote server, where you have a copy of an older version of the file on your
computer already. zsync downloads only the new parts of the file. It uses the
same algorithm as rsync. However, where rsync is designed for synchronising
data from one computer to another within an organisation, zsync is designed for
file distribution, with one file on a server to be distributed to thousands of
downloaders. zsync requires no special server software - just a web server to
host the files - and imposes no extra load on the server, making it ideal for
large scale file distribution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i '/^doc_DATA/s/COPYING//' Makefile.am # avoid duplicating license file

%build

%configure
%make_build CFLAGS+="-Wno-old-style-definition -D_DEFAULT_SOURCE"
%install
%make_install
%oreon_autofiles main

%check

./check-zsyncmake
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
