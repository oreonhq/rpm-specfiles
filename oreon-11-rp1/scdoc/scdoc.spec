%global source0_hash 98780bbdf16c1bce89ef3a8c0f537ac6e4ea77087b609e7698857614488a2a62
Name:     scdoc
Version:  1.11.5
Release:        1%{?dist}
Summary:        Tool for generating roff manual pages
License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:        https://git.sr.ht/~sircmpwn/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build

make PREFIX=%{_prefix} %{?_smp_mflags}
%install
%if 0%{?el7}
%make_install PREFIX=%{_prefix} INSTALL="%{__install} -p"
%else
%make_install PREFIX=%{_prefix}
%oreon_autofiles main
%endif
%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
