%global source0_hash e1f48c80ecdf5c3455d935947012c27b6bc1fade4ddaad0aa01b2e83c4ce98af

%global commit      1a3320dab988372f8910ccc838a6a7a45c8980ff
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Presently required when building with GCC Go.
%global debug_package %{nil}
%global __strip /bin/true

Name:           nex
Version:        20210330
Release:        %autorelease
Summary:        A lexer generator for Go that is similar to Lex/Flex
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://www-cs-students.stanford.edu/~blynn/nex/
Source0:        https://github.com/blynn/nex/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  compiler(go-compiler)

%description
Nex is a lexer similar to Lex/Flex that: (1) generates Go code instead
of C code, (2) integrates with Go's Yacc instead of YACC/Bison, (3)
supports UTF-8, and (4) supports nested structural regular expressions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n nex-%{commit}

%build
%gobuild -o %{gobuilddir}/bin/nex main.go nex.go

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%doc COPYING README.asciidoc
%{_bindir}/nex

%changelog
%autochangelog
