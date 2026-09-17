%global source0_hash 5275fcfc58d3d4890d074077d94497db488b2648287b3e48e67b00ea517b02ba

Summary:         A small, flexible, terminal-based text editor
Name:            mle
Version:         1.7.2
Release:         9%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:         Apache-2.0
URL:             https://github.com/adsr/mle
Source:          https://github.com/adsr/mle/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:   gcc
BuildRequires:   pcre2-devel
BuildRequires:   uthash-devel
BuildRequires:   lua-devel
BuildRequires:   glibc-langpack-en

%description
mle is a small, flexible, terminal-based text editor written in C.
Notable features include: full Unicode support, syntax highlighting,
scriptable rc file, macros, search and replace (PCRE), window
splitting, multiple cursors, and integration with various shell
commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's|-llua5.4|-llua|g' Makefile
sed -i 's|install -D |install -D -p |g' Makefile
sed -i 's|<lua5.4/lua.h>|<lua.h>|g' mle.h
sed -i 's|<lua5.4/lualib.h>|<lualib.h>|g' mle.h
sed -i 's|<lua5.4/lauxlib.h>|<lauxlib.h>|g' mle.h

%build
%make_build

%check
LC_ALL=en_US.UTF-8 make %{?_smp_mflags} test

%install
%make_install prefix=%{_prefix}
install -D -p -v -m 644 mle.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mle.1

%files
%license LICENSE
%doc README.md
%{_bindir}/mle
%{_mandir}/man1/mle.1*

%changelog
%autochangelog
