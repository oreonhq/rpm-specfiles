%global source0_hash c62b1372b8c21d64c6da5a687abf3b56ee314fae5b67c1f08b5550ea5f87fdac

Name:           pick
Version:        4.0.0
Release:        %autorelease
Summary:        A fuzzy search tool for the command-line

# The entire source code is MIT except for
# compat-reallocarray.c and compat-strtonum.c files which are ISC
License:        MIT AND ISC
URL:            https://github.com/mptre/pick
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix discarded qualifier
Patch: fix-discarded-qualifiers.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

# nmh also provides /usr/bin/pick
Conflicts:      nmh

%description
The pick utility allows users to choose one option from a set of choices using
an interface with fuzzy search functionality. pick reads a list of choices on
stdin and outputs the selected choice on stdout. Therefore it is easily used
both in pipelines and subshells.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export PREFIX=%{_prefix}
export MANDIR=%{_mandir}
export INSTALL_MAN="install -p -m 0644"
%configure
%make_build CFLAGS="%{build_cflags} -D_GNU_SOURCE"

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
