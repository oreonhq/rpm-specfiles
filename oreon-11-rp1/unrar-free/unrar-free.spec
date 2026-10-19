%global source0_hash e0d52bded7863b81cbc4313929d0ad2e4d2e449bf96c85b436658eda02c506a7
Name:           unrar-free
Version:        0.3.3
Release:        1%{?dist}
Summary:        Free software version of the non-free unrar utility
License:        GPL-2.0-or-later
URL:            https://gitlab.com/bgermann/unrar-free
Source0:        https://gitlab.com/bgermann/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libarchive-devel
BuildRequires:  make
# /oreon:deps
%description
unrar-free is a free software version of the non-free unrar utility. This
program is a simple command-line front-end to libarchive, and can list and
extract RAR archives but also other formats supported by libarchive. It does
not rival the non-free unrar in terms of features, but special care has been
taken to ensure it meets most user's needs.

%package -n     unrar
Summary:        Wrapper package for unrar-free
Requires:       %{name}%{_isa} = %{version}-%{release}
%description -n unrar
This packages is a wrapper to use unrar-free as /usr/bin/unrar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure
%make_build
%install
%make_install
ln -s unrar-free %{buildroot}%{_bindir}/unrar
ln -s unrar-free.1 %{buildroot}%{_mandir}/man1/unrar.1
%oreon_autofiles unrar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unrar -f %{oreon_filedir}/unrar.list

%changelog

%autochangelog
