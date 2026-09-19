%global source0_hash f42d02821d587dbdee5f5c5b03483d81b42512d73e43f6eff9b9833ce02b961b

Name:           vis
Version:        0.9
Release:        %autorelease
Summary:        A vim-like editor with structural regex from plan9

# The entire source code is ISC except for the following exceptions,
# that are also found in the LICENSE-file of the project:
# ./configure is MIT licensed
# map.c and map.h are under CC0
# libutf.c and libutf.h are MIT licensed
# sam.c and sam.h are under a ISC-like license
# All files under lua/lexers/ are MIT licensed
License:        ISC AND MIT AND CC0-1.0
URL:            https://git.sr.ht/~martanne/%{name}
Source0:        https://git.sr.ht/~martanne/%{name}/archive/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(tre)
BuildRequires:  pkgconfig(lua) >= 5.2
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig(libselinux)
Requires:       lua-lpeg >= 0.12
Requires:       xsel

%description
A Vim-like editor with structural regular expressions
inspired by Plan9's Sam-editor.

%package doc
Summary:        Docs for the Lua API of Vis
BuildRequires:  lua-ldoc
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n vis-v%{version}

%build
%configure
%make_build

# create Lua API docs
%make_build luadoc-all

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/vis
%{_bindir}/vis-clipboard
%{_bindir}/vis-complete
%{_bindir}/vis-digraph
%{_bindir}/vis-menu
%{_bindir}/vis-open
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1.*
%exclude %{_pkgdocdir}/LICENSE

%files doc
%doc lua/doc/index.html lua/doc/ldoc_fixed.css

%changelog
%autochangelog
