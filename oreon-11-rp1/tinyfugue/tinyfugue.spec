%global source0_hash 3750a114cf947b1e3d71cecbe258cb830c39f3186c369e368d4662de9c50d989
%global packageversion 50b8
Name:           tinyfugue
Version:        5.0
Release:        1%{?dist}
Summary:        A MU* client
License:        GPL-2.0-or-later
URL:            http://tinyfugue.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/tf-%{packageversion}.tar.gz
Patch1:         tf-50b8.pcre.patch
Patch2:         tf-allrootpatch.txt
Patch3:         tf-allsrcpatch.txt
Patch4:         0001-Add-DESTDIR-support.patch
Patch5:         0002-Correct-use-of-va_list.patch
Patch6:         0003-Minor-man-page-fixes.patch
Patch7:         0004-Support-GnuTLS-via-OpenSSL-compat-library.patch
Patch8:         0005-Make-the-build-reproducible.patch
Patch9:         0006-Fix-library-install-path.patch
Patch10:        0007-Fix-spelling-errors.patch
Patch11:        0008-Fix-duplicate-world_decl-definitions.patch
Patch12:        0009-Fix-spelling-error-in-manual-page.patch
Patch13:        tinyfigue-configure-c99.patch
Patch14:        tinyfugue-malloc-c99.h
Patch15:        tinyfugue-tfio-c99.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  sed
# /oreon:deps
%description
TinyFugue is the ubiquitous MUD/MOO/MUSH/MUCK/etc client for UNIX. This client
allows you to interact with multiple worlds simultaneously, create command
macros, and create hooks and triggers for automated responses to game messages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n tf-%{packageversion} -p1
# Unbundle the old PCRE and update to 8.30
rm -rfv src/pcre-2.08

%build

export CPPFLAGS="${CFLAGS} -Wno-incompatible-pointer-types -Wno-return-mismatch -Wno-return-type"
%configure \
    --enable-core \
    --enable-inet6 \
    --enable-ssl \
    --enable-atcp \
    --enable-gmcp \
    --enable-option102
%make_build
%install
mkdir %{buildroot}/%{_prefix}
%make_install
install -D -p -m 644 src/tf.1.nroffman %{buildroot}%{_mandir}/man1/tf.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
