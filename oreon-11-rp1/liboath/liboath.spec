%global source0_hash 8b1da365759f1249be57a82aec6e107f7b57dc77d813f96dc0aaf81624f28971
%global toolkit_version 2.6.14
Summary:        Library for OATH handling (HOTP/TOTP one-time passwords)
Name:           liboath
Version:        2.6.14
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://oath-toolkit.codeberg.page/
Source0:        https://codeberg.org/oath-toolkit/oath-toolkit/releases/download/v%{version}/oath-toolkit-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
liboath is a shared and static C library for OATH (Open AuTHentication)
handling, implementing both the HOTP event-based and TOTP time-based
one-time password algorithms (RFC 4226 and RFC 6238).

Built from the oath-toolkit source release, liboath is packaged standalone
since it has its own configure/build inside the toolkit tree and does not
require the other toolkit components (oathtool, pam_oath, libpskc).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and pkgconfig file for developing against liboath, the OATH
one-time password library used by plasma-pass.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n oath-toolkit-%{toolkit_version}

%build

cd liboath
autoreconf -fvi
%configure --disable-static
%make_build
%install
cd liboath
%make_install
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liboath-devel -f %{oreon_filedir}/liboath-devel.list

%changelog

%autochangelog
