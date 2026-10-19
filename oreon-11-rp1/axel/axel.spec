%global source0_hash f6f2a5369d78003ab162a774cff0be71096bea6929333a79c8168c82caced07d
%global forgeurl https://github.com/axel-download-accelerator/axel
Name:       axel
Version:    2.17.14
Release:        1%{?dist}
Summary:        Light command line download accelerator for Linux and Unix
%forgemeta
License:    GPL-2.0-or-later
URL:        %forgeurl
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libssl)
BuildRequires:  txt2man
# /oreon:deps
%description
Axel tries to accelerate HTTP/FTP downloading process by using
multiple connections for one file. It can use multiple mirrors for a
download. Axel has no dependencies and is lightweight, so it might
be useful as a wget clone on byte-critical systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

autoreconf -vfi
%{configure}
%make_build
%install
%make_install \
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -p -T doc/axelrc.example %{buildroot}%{_sysconfdir}/axelrc
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
