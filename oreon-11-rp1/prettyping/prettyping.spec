%global source0_hash e8484492e3c704b2460a00b0e417a07ad7112b5f4ad9a211931ee031fe64b4b6

Name: prettyping
Version: 1.1.0
Release: 3%{?dist}
Summary: Compact, colorful ping tool for your terminal
License: MIT

URL: http://denilson.sa.nom.br/prettyping
Source0: https://github.com/denilsonsa/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: bash coreutils gawk iputils
BuildArch: noarch

%description
prettyping runs the standard ping in background and parses its output,
showing ping responses in a graphical way at the terminal, by using colors
and Unicode characters.

Don’t have support for UTF-8 in your terminal?
No problem, you can disable it and use standard ASCII characters instead.

Don’t have support for colors?
No problem, you can also disable them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -e 's|#!/usr/bin/env bash|#!/usr/bin/bash|' -i ./%{name}

%build
# Nothing to do here

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 ./%{name}  %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
