%global source0_hash ee9538fce98895dcf0d108087d3ee2e13f5c08ed94c983f0218a7a3d153b725d
Name:		progress
Version:	0.17
Release:        1%{?dist}
Summary:        Coreutils Viewer
License:	GPL-3.0-only
URL:		https://github.com/Xfennec/%{name}
Source0:        https://github.com/Xfennec/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Progress can be described as a Tiny Dirty Linux Only* C command that
looks for coreutils basic commands (cp, mv, dd, tar, gzip/gunzip, cat, ...)
currently running on your system and displays the percentage of copied data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

CFLAGS="%{?optflags}"			\
LFLAGS="%{?__global_ldflags}"	\
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
