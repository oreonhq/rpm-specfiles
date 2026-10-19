%global source0_hash 460475323404460919ff48c90f7b3ebfdb66f3b9961f54dd73dd172178c07712
Name:           root-tail
Version:        1.3
Release:        1%{?dist}
Summary:        Displays a given file anywhere on your X11 root window
License:        GPL-2.0-or-later
URL:            http://software.schmorp.de/pkg/%{name}.html
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
Patch0:         root-tail-1.3-Allow-overriding-LDFLAGS-from-the-command-line.patch
Patch1:         root-tail-1.3-Install-an-uncompressed-manual-page.patch
Patch2:         root-tail-1.3-Fix-installation.patch
Patch3:         root-tail-1.3-Generate-Expose-events-when-clearing-a-window.patch
Patch4:         root-tail-1.3-Respect-width-and-height-unsigness-in-arithmetics.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  make
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Displays a given file anywhere on your X11 root window, i.e. it is kind of 
tail -f for multiple files using your desktop background as output window.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build

%{make_build} CFLAGS='%{optflags}' LDFLAGS='%{__global_ldflags}'
%install
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
