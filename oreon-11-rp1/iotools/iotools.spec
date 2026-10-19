%global source0_hash 5b31af5b947d33b7b8d079a5ad091af1b013e8509a1230acbe0531e18af11588
%global tag 1.7pre0
Name:           iotools
Version:        1.7~pre0
Release:        1%{?dist}
Summary:        Set of command line tools to access hardware device registers
License:        GPL-2.0-or-later
URL:            https://github.com/aaron-sierra/iotools
Source0:        https://github.com/aaron-sierra/%{name}/archive/v%{tag}/%{name}-%{tag}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
The iotools package provides a set of simple command line tools which allow
access to hardware device registers. Supported register interfaces include
PCI, IO, memory mapped IO, SMBus, CPUID, and MSR. Also included are some
utilities which allow for simple arithmetic, logical, and other operations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{tag}

# Do not abort on warnings
sed -i 's/-Werror//' Makefile

%build

%set_build_flags
%if 0%{?el8}
export CC="%{__cc}"
%endif
%make_build STATIC=0 DEBUG=0 CC="$CC" EXTRA_CFLAGS="$CFLAGS"
%install
install -Dpm0755 -t %{buildroot}%{_sbindir} iotools
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
