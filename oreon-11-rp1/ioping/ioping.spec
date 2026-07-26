%global source0_hash 7aa48e70aaa766bc112dea57ebbe56700626871052380709df3a26f46766e8c8

Name:           ioping
Version:        1.3
Release:        %{autorelease}
Summary:        Simple disk I/O latency monitoring tool
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/koct9i/ioping
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
%description
ioping lets you monitor I/O latency in real time. It shows disk latency in 
the same way as ping shows network latency.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export CFLAGS="-Wextra -pedantic -funroll-loops -ftree-vectorize %{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc changelog README.md
%license LICENSE
%{_bindir}/ioping
%{_mandir}/man1/ioping.1*

%changelog
%autochangelog
