%global source0_hash d5d44b85cb490643d0707e1a2186f3a32998c2f6eabaa9481479b65caeee57c0

%if 0%{?fedora} && 0%{?fedora} >= 40
# Trigger rebuild for GCC 14 compatibility
# https://fedoraproject.org/wiki/Changes/PortingToModernC
%bcond_without vala
%else
# The rebuild process is not necessary on older releases,
# and fails on EL9
# error: Package `gnu' not found in specified Vala API directories or GObject-Introspection GIR directories
%bcond_with vala
%endif

Summary: Zile Is Lossy Emacs
Name: zile
Version: 2.6.4
Release: %autorelease
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/%{name}/
Source0: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel gc-devel help2man autoconf automake
BuildRequires: libgee-devel
%if %{with vala}
BuildRequires: vala
%endif

# FTBFS on ppc64le, will investigate further with upstream
ExcludeArch: ppc64le

%description
Zile is a small Emacs clone. Zile is a customizable, self-documenting
real-time open-source display editor. Zile was written to be as
similar as possible to Emacs; every Emacs user should feel at home.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%if %{with vala}
find -name '*.vala' -exec touch {} \;
%endif

# convert THANKS file to utf-8 to silent rpmlint
iconv -f iso-8859-1 -t utf-8 -o THANKS{.utf8,}
touch -r THANKS{,.utf8}
mv THANKS{.utf8,}

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README THANKS FAQ src/dotzile.sample
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
