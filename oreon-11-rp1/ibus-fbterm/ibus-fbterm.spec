%global source0_hash 294449bed816fb0e2aaca073851e4c9be506b5d6a015f43ed2ceb8edf81d835f
Name:       ibus-fbterm
Version:    1.0.2
Release:        1%{?dist}
Summary:        IBus front-end for fbterm
License:    GPL-3.0-only
URL:        https://github.com/fujiwarat/ibus-fbterm
Source0:        https://github.com/fujiwarat/ibus-fbterm/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0: ibus-fbterm-c99.patch
Requires:      ibus >= 1.5, fbterm >= 1.6
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ibus
BuildRequires:  ibus-devel
BuildRequires:  make
BuildRequires:  vala
# /oreon:deps
%description
ibus-fbterm is a input method for FbTerm based on IBus.

* To utilize framebuffer, user should be added into 'video' group, or install
  fbterm-udevrules package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Trigger recompilation of all Vala sources.
find -name '*.vala' -exec touch {} \;

%build

autoreconf -iv
%configure \
    --prefix=%{_prefix}
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
