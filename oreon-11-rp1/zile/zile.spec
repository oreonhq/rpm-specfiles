%global source0_hash d5d44b85cb490643d0707e1a2186f3a32998c2f6eabaa9481479b65caeee57c0
%bcond_with vala
Summary:        Zile Is Lossy Emacs
Name: zile
Version: 2.6.4
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/%{name}/
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
%if %{with vala}
%endif
ExcludeArch: ppc64le
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gc-devel
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libgee-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
