%global source0_hash 6016e41fdda9166b86b09a0ac601a0c453c3b35acdf904c97a8a555459ad73c0
Name:           bmon
Version:        5.0
Release:        1%{?dist}
Summary:        Bandwidth monitor and rate estimator
License:        BSD-2-Clause and MIT
URL:            https://github.com/tgraf/bmon
Source0:        https://github.com/tgraf/bmon/releases/download/v%{version}/bmon-%{version}.tar.gz
Patch1:         bmon-4.0-buffer_size.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libconfuse-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
bmon is a monitoring and debugging tool to capture networking related
statistics and prepare them visually in a human friendly way. It
features various output methods including an interactive curses user
interface and a programmable text output for scripting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
