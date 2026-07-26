%global source0_hash c95eb2aeb952b3fd09f4a07859115d40c4d04a8d551b3071b0a10fcd0db7ebc4

# Read https://bugzilla.redhat.com/show_bug.cgi?id=1654765
# mangling shebang in /usr/sbin/debootstrap from /bin/sh to /usr/bin/sh
%undefine __brp_mangle_shebangs

#global postfix nmu1

Name:           debootstrap
Version:        1.0.140
Release:        6%{?dist}
Summary:        Debian GNU/Linux bootstrapper

License:        MIT
URL:            https://wiki.debian.org/Debootstrap
Source0:        https://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_%{version}%{?postfix:+%{postfix}}.tar.gz
Patch0:         sbin_move.patch

BuildArch:      noarch

BuildRequires:  fakeroot
BuildRequires:  make
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

%description
debootstrap is used to create a Debian base system from scratch, without
requiring the availability of dpkg or apt.  It does this by downloading
.deb files from a mirror site, and carefully unpacking them into a
directory which can eventually be chrooted into.

This might be often useful coupled with virtualization techniques to run
Debian GNU/Linux guest system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
# nothing to do

%install
fakeroot %make_install VERSION="%{version}-%{release}" SBINDIR="%{_sbindir}"

# install manual page
mkdir -p %{buildroot}%{_mandir}/man8
install -p -m 0644 debootstrap.8 %{buildroot}%{_mandir}/man8

%files
%doc debian/changelog README
%license debian/copyright
%{_datadir}/debootstrap
%{_sbindir}/debootstrap
%{_mandir}/man8/debootstrap.8*

%changelog
%autochangelog
