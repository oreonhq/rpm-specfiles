%global source1_hash 9037bc91c67d173a2250f13b38e4a2ca4ed0e93e82a882af52b0531a9b077632
%global source0_hash 1d38a7258796015a92a5a6eee293340b924e4ff68e4e8e845b8bdbb5f4f7d9e8
Name:           parallel
Summary:        Shell tool for executing jobs in parallel
Version:        20260822
Release:        1%{?dist}
License:        LicenseRef-Callaway-GFDL AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/parallel/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        cda01a4208c4f74506107e7bd1ab451688888888.asc
BuildArch:      noarch
%define __requires_exclude sh$
Conflicts:      moreutils-parallel
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(FileHandle)
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  sed
# /oreon:deps
%description
GNU Parallel is a shell tool for executing jobs in parallel using one or more
machines. A job is typically a single command or a small script that has to be
run for each of the lines in the input. The typical input is a list of files, a
list of hosts, a list of users, or a list of tables.

If you use xargs today you will find GNU Parallel very easy to use. If you
write loops in shell, you will find GNU Parallel may be able to replace most of
the loops and make them run faster by running jobs in parallel. If you use ppss
or pexec you will find GNU Parallel will often make the command easier to read.

GNU Parallel also makes sure output from the commands is the same output as you
would get had you run the commands sequentially. This makes it possible to use
output from GNU Parallel as input for other programs.

GNU Parallel is command-line-compatible with moreutils' parallel, but offers
additional features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
# Replace shebang by replacing "env" by removing "env ".
# FIXME: this is quite a hack
sed -i '1s:/env :/:' src/env_parallel.*

%build

autoreconf -ivf
%configure
%make_build
%install
%make_install
rm -vrf %{buildroot}%{_pkgdocdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
