%global source0_hash 289a0966c02c2008cd263d3913a8e3c84c97b8ded3e08373d63a382c71d2199c

%bcond_with tests

Name:           triehash
Version:        0.3
Release:        17%{?dist}
Summary:        Generator for order-preserving minimal perfect hash functions in C

License:        MIT
URL:            https://jak-linux.org/projects/triehash/
Source0:        https://github.com/julian-klode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with tests}
BuildRequires:  perl(Devel::Cover)
%endif
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl-generators

%{?perl_default_filter}

%description
TrieHash generates perfect hash functions as C code which then gets
compiled into optimal machine code as part of the usual program compilation.

TrieHash works by translating a list of strings to a trie, and then converting
the trie to a set of recursive switch statements; first switching by length,
and then switching by bytes.

TrieHash has various optimizations such as processing multiple bytes at once
(on GNU C), and shortcuts for reducing the complexity of case-insensitive
matching (ASCII only). Generated code performs substantially faster than
gperf, but is larger.

TrieHash was written for use in APT.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
pod2man triehash.pl triehash.1

%install
install -p -m755 -D triehash.pl %{buildroot}%{_bindir}/%{name}
install -p -m644 -D triehash.1 %{buildroot}%{_mandir}/man1/%{name}.1

%if %{with tests}
%check
./tests/run-tests.sh
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
