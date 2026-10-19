%global source0_hash 9318ef65f555ee3d893176349a4219f1f1260ce24d4100aeb667a546f61fc183
ExcludeArch: %{ix86}
%ifnarch s390x
%endif
%global cfgfile %{_datadir}/%{name}/%{name}
Name:           boxes
Version:        2.3.2
Release:        1%{?dist}
Summary:        Command line ASCII boxes unlimited!
License:        GPL-3.0-only
URL:            http://boxes.thomasjensen.com
Source0:        https://github.com/ascii-%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  vim-common
# /oreon:deps
%description
Boxes is a command line program which draws, removes, and repairs ASCII art
boxes. It operates as a text filter. The generated boxes may even be removed
and repaired again if they were badly damaged by editing of the text inside.
Since boxes may be open on any side, boxes can also be used to create
(regional) comments in any programming language.

Boxes is useful for making the function headers in your programming language
look better, for spicing up news postings and emails, or just for decorating
documentation files. Since the drawn box is matched in size to your input
text, you can use boxes in scripts to dynamically add boxes around stuff.

%package        vim
BuildArch:      noarch
Summary:        Vim plugin for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       vim-enhanced
%description    vim
Vim plugin for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build \
    CFLAGS_ADDTL='%{optflags}' \
    GLOBALCONF=%{cfgfile} \
    LDFLAGS_ADDTL='%{build_ldflags}' \
    debug \
    %{nil}
%if %{with tests}
%check

export TERM=xterm-color
%if 0%{?el8}
export LANG=en_US.UTF-8
%endif
%make_build test
%endif
%install
install -Dp -m 0755 out/%{name}     %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}-config  %{buildroot}%{cfgfile}
install -Dp -m 0644 doc/%{name}.1   %{buildroot}%{_mandir}/man1/%{name}.1
install -Dp -m 0644 %{name}.vim     %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%oreon_autofiles boxes-vim usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n boxes-vim -f %{oreon_filedir}/boxes-vim.list

%changelog

%autochangelog
