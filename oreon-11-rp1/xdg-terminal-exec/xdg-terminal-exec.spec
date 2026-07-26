%global source0_hash b96f7a4ac67a6fce78e92f14129183c06e517c2946c484851dc7bb473504ad47

%bcond check 1

Name:           xdg-terminal-exec
Version:        0.14.1
Release:        %autorelease
Summary:        Proposed XDG Default Terminal Execution Spec implementation

License:        GPL-3.0-or-later
URL:            https://github.com/Vladimir-csp/xdg-terminal-exec
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  scdoc
%if %{with check}
BuildRequires:  bats
%endif

BuildArch:      noarch

%description
This package provides a reference shell-based implementation for a proposed XDG
Default Terminal Execution Specification. The proposal can be found at:

https://gitlab.freedesktop.org/terminal-wg/specifications/-/merge_requests/3

Please be advised that while this spec is in proposed state, backwards
compatibility is maintained as best effort and is not guaranteed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build

%install
%make_install prefix="%{buildroot}%{_prefix}"

%if %{with check}
%check
make test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
