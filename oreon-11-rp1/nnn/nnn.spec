%global source0_hash 79ee69f3ced7c0778d207df76b4d4d680636975ccda002eeb19d0917fcba3d36
Name:       nnn
Version:    5.3
Release:        1%{?dist}
Summary:        The missing terminal file browser for X
License:    BSD-2-Clause
URL:        https://github.com/jarun/nnn
Source0:        https://github.com/jarun/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  readline-devel
# /oreon:deps
%description
nnn is probably the fastest and most resource-sensitive (with all
its capabilities) file browser you have ever used. It's extremely flexible
too - integrates with your DE and favourite GUI utilities, works with
the desktop opener, supports bookmarks, has smart navigation shortcuts,
navigate-as-you-type mode, disk usage analyzer mode, comprehensive file
details and much more. nnn was initially forked from noice but is
significantly different today.

Cool things you can do with nnn:

 - open any file in the default desktop application or a custom one
 - navigate-as-you-type (search-as-you-type enabled even on directory switch)
 - check disk usage with number of files in current directory tree
 - run desktop search utility (gnome-search-tool or catfish) in any directory
 - copy absolute file paths to clipboard, spawn a terminal and use the paths
 - navigate instantly using shortcuts like ~, -, & or handy bookmarks
 - use cd ..... at chdir prompt to go to a parent directory
 - detailed file stats, media info, list and extract archives
 - pin a directory you may need to revisit and jump to it anytime
 - lock the current terminal after a specified idle time
 - change directory on exit

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

sed -i "s|^install: all|install:|" Makefile

%build

%set_build_flags
%make_build STRIP=/bin/true
%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  misc/auto-completion/bash/nnn-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  misc/auto-completion/fish/nnn.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  misc/auto-completion/zsh/_nnn
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
