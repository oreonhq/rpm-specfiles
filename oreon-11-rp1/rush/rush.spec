%global source1_hash 1bf346dd872779e62355554d92ccae386d6e51254f7ef2a12262d5e473c91284
%global source0_hash fa95af9d2c7b635581841cc27a1d27af611f60dd962113a93d23a8874aa060f4
Name:             rush
Version:          2.4
Release:        1%{?dist}
Summary:        GNU Restricted User Shell
License:          GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
URL:              https://www.gnu.org/software/rush/
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:          http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:          gpgkey-79FFD94BFCE230B1.gpg
Provides:         bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
GNU Rush is a Restricted User Shell, designed for sites providing
limited remote access to their resources, such as, for example,
https://savannah.gnu.org/. Its main program, rush, is configured
as a user login shell for users that are allowed only remote access
to the machine. Using a flexible configuration file, GNU Rush gives
administrator complete control over the command lines that users
execute, and allows to tune the usage of system resources, such as
virtual memory, CPU time, etc. on a per-user basis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

export CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS"
%configure
%make_build
%check

make check
%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
