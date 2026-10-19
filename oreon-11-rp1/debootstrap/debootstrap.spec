%global source0_hash 7cc8f9e386ed8dfd4b062a3b9527f0f45176dfa1b065e7db270f837956516b20
%undefine __brp_mangle_shebangs
Name:           debootstrap
Version:        1.0.145
Release:        1%{?dist}
Summary:        Debian GNU/Linux bootstrapper
License:        MIT
URL:            https://wiki.debian.org/Debootstrap
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
Patch0:         sbin_move.patch
BuildArch:      noarch
Requires:       perl-interpreter
Requires:       wget
Requires:       tar
Requires:       gzip
Requires:       dpkg
Requires:       xz
Recommends:     ubu-keyring
Recommends:     debian-keyring
Recommends:     binutils
Recommends:     gettext-runtime
Recommends:     xz-utils
Recommends:     zstd
# oreon:deps
BuildRequires:  fakeroot
BuildRequires:  make
# /oreon:deps
%description
debootstrap is used to create a Debian base system from scratch, without
requiring the availability of dpkg or apt.  It does this by downloading
.deb files from a mirror site, and carefully unpacking them into a
directory which can eventually be chrooted into.

This might be often useful coupled with virtualization techniques to run
Debian GNU/Linux guest system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%install
fakeroot %make_install VERSION="%{version}-%{release}" SBINDIR="%{_sbindir}"
mkdir -p %{buildroot}%{_mandir}/man8
install -p -m 0644 debootstrap.8 %{buildroot}%{_mandir}/man8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
