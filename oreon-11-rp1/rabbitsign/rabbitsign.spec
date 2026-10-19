%global source0_hash e83b56d296e5542bcd30f1a8051fe0a802a99606537c76e5e55684e47396b218
Name:           rabbitsign
Version:        2.1
Release:        1%{?dist}
Summary:        Digitally sign software for Texas Instruments calculators
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://www.ticalc.org/archives/files/fileinfo/383/38392.html
Source0:        https://www.ticalc.org/pub/unix/%{name}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
# /oreon:deps
%description
RabbitSign is a free implementation of the algorithms used to digitally sign
software for the Texas Instruments TI-73, TI-83 Plus, TI-84 Plus, TI-89, TI-92
Plus, and Voyage 200 calculators.

RabbitSign can handle a variety of common input file formats, including
GraphLink files as well as "plain" hex and binary files. It is quite a lot
faster than the official application signing programs from TI, and unlike
those programs, does not have any arbitrary limitations on file names or
contents.  It also has the ability to re-sign applications that have been
signed previously.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
