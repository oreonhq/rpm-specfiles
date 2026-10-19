%global source0_hash b2721b1c0147aaafc98e6a31d875316ba032ad336bec7f2a8bc538f9e3c6db60
%bcond autoreconf 1
Name:           rlwrap
Version:        0.48
Release:        1%{?dist}
Summary:        Wrapper for GNU readline
License:        GPL-2.0-or-later
URL:            https://github.com/hanslub42/rlwrap
Source0:        https://github.com/hanslub42/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with autoreconf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libptytty-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-rpm-macros
BuildRequires:  readline-devel
# /oreon:deps
%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%dnl workaround for RPM < 4.18 not having %conf
%{?conf:%conf}
%{!?conf:%build}
autoreconf -fiv

%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
# issues with rl_message function signature even though readline is not upgraded
# https://gcc.gnu.org/gcc-15/porting_to.html
# readline.c: In function ‘message_in_echo_area’:
# readline.c:192:5: error: too many arguments to function ‘rl_message’; expected 0, have 1
#   192 |     rl_message(message);
#       |     ^~~~~~~~~~ ~~~~~~~
# In file included from rlwrap.h:189,
#                  from readline.c:23:
# /usr/include/readline/readline.h:410:12: note: declared here
#   410 | extern int rl_message ();
#       |            ^~~~~~~~~~
# seems related to the switch to -std=gnu23 but not sure how:
# https://gcc.gnu.org/gcc-15/porting_to.html
# reported upstream in https://github.com/hanslub42/rlwrap/issues/195
export CFLAGS="%{optflags} -std=gnu17"
%endif

%configure

%{?conf:%build}
%make_build

%install
%make_install
%{__sed} -r -i \
    -e 's|^#!.*perl$|#!%{__perl}|g' \
    -e 's|^#!.*python3$|#!%{__python3}|g' \
    $(find %{buildroot}%{_datadir}/%{name}/ -type f)
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
