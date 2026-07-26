%global source0_hash 33e3a54bd54b1eb325b48316a7cacc24047c533ef88e6ef98b88dfbb60e12734

Name: cadaver
Version: 0.28
Release: 3%{?dist}
Summary: Command-line WebDAV client
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: https://notroj.github.io/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
BuildRequires: gcc, make
BuildRequires: neon-devel >= 0.27.0, readline-devel, ncurses-devel, gettext

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

%files -f %{name}.lang
%doc NEWS THANKS COPYING README.md
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
