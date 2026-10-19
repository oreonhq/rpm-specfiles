%global source0_hash dc9a2bdc556b2be900c1d8cdf432de26492de5af3ffade000d4bfd97f3122bfb
Name:           entr
Version:        5.8
Release:        1%{?dist}
Summary:        Run arbitrary commands when files change
License:        ISC AND BSD-2-Clause
URL:            http://eradman.com/entrproject/
Source0:        http://eradman.com/%{name}project//code/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  tmux
BuildRequires:  vim
# /oreon:deps
%description
A utility for running arbitrary commands when files change. Uses inotify to
avoid polling. It was written to make rapid feedback and automated testing
natural and completely ordinary.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
ln -s Makefile{.linux,}

%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build
%install
export PREFIX=%{_prefix}
%make_install
%oreon_autofiles main

%check

make test
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
