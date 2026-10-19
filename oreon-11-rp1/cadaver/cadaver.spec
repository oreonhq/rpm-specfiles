%global source0_hash 33e3a54bd54b1eb325b48316a7cacc24047c533ef88e6ef98b88dfbb60e12734
Name: cadaver
Version: 0.28
Release:        3%{?dist}
Summary:        Command-line WebDAV client
License: GPL-2.0-or-later
Source0:        https://notroj.github.io/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  neon-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
cadaver is a command-line WebDAV client, with support for file upload, 
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation, 
and resource locking.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --with-neon=%{_prefix}
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
