%global source0_hash 90c5d943820c70cef37eb41a382a6ea4f5dd7fd95efef13b2b5520d320f5d067

Name:           entr
Version:        5.7
Release:        3%{?dist}
Summary:        Run arbitrary commands when files change

# The entire source code is ISC except missing/sys/event.h which is BSD-2-Clause
License:        ISC AND BSD-2-Clause
URL:            http://eradman.com/entrproject/
Source0:        %{url}/code/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
# Required for make check
BuildRequires:  procps-ng
BuildRequires:  tmux
BuildRequires:  vim
BuildRequires:  git-core

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

%check
make test
make check

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
