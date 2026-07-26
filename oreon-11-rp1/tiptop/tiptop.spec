%global source0_hash a14b1b59ea4856844e27bc4e22129b7906b8815afaf50a25ac60998dafcc93a7

Name:           tiptop
Version:        2.3.2
Release:        6%{?dist}
Summary:        Performance monitoring tool based on hardware counters
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

URL:            https://team.inria.fr/pacap/software/tiptop/
Source:         https://files.inria.fr/pacap/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Hardware performance monitoring counters have recently received a lot of
attention. They have been used by diverse communities to understand and
improve the quality of computing systems: For example, architects use them to
extract application characteristics and propose new hardware mechanisms;
compiler writers study how generated code behaves on particular hardware;
software developers identify critical regions of their applications and
evaluate design choices to select the best performing implementation. We
propose that counters be used by all categories of users, in particular
non-experts, and we advocate that a few simple metrics derived from these
counters are relevant and useful. For example, a low IPC (number of executed
instructions per cycle) indicates that the hardware is not performing at its
best; a high cache miss ratio can suggest several causes, such as conflicts
between processes in a multicore environment.

Tiptop is a performance monitoring tool for Linux. It provides a dynamic
real-time view of the tasks running in the system. Tiptop is very similar to
the top utility, but most of the information displayed comes from hardware
counters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure CFLAGS='%optflags -Wno-error=unused-function'
%make_build -j1

%install
%make_install

%files
%doc AUTHORS README tiptoprc
%license COPYING
%{_bindir}/*tiptop
%{_mandir}/man1/*tiptop.1*

%changelog
%autochangelog
