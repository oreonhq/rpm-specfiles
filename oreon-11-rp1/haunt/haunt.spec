%global source1_hash 7735b2ad86ca3e64feec8f03ffad074d996e12bad9b9b461b56c551a8a24a3cf
%global source0_hash 98babed06be54a066c3ebc94410a91eb7cc48367e94d528131d3ba271499992b
%global debug_package %{nil}
%global mver 3.0
Name:           haunt
Version:        0.3.0
Release:        1%{?dist}
Summary:        Hackable static site generator in guile scheme
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://dthompson.us/projects/haunt.html
Source0:        https://files.dthompson.us/releases/haunt/haunt-%{version}.tar.gz
Source1:        https://files.dthompson.us/releases/haunt/haunt-%{version}.tar.gz.asc
Source2:        8ccba7f552b9cbeae1fb29158328c7470ff1d807.asc
%ifnarch %{ix86}
%endif
Requires:       guile-commonmark
Requires:       guile-reader
%ifnarch %{ix86}
Requires:       hut
%endif
Requires:       rsync
Requires:       tar
ExcludeArch:  %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  guile-commonmark
BuildRequires:  guile-reader-devel
BuildRequires:  guile30-devel
BuildRequires:  hut
BuildRequires:  make
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  texinfo
# /oreon:deps
%description
Haunt is a simple, functional, hackable static site generator that gives
authors the ability to treat websites as Scheme programs.

By giving authors the full expressive power of Scheme, they are able to
control every aspect of the site generation process. Haunt provides a simple,
functional build system that can be easily extended for this purpose.

Haunt has no opinion about what markup language authors should use to write
posts, though it comes with support for the popular Markdown format. Likewise,
Haunt has no opinion about how authors structure their sites. Though it comes
with support for building simple blogs or Atom feeds, authors should feel
empowered to tweak, replace, or create builders to do things that aren't
provided out-of-the-box.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

autoreconf -vif
%configure
%make_build
make info
%install
%make_install
DESTDIR=%{buildroot} make install-info
test -f %{buildroot}/%{_infodir}/dir && rm %{buildroot}/%{_infodir}/dir
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
