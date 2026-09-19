%global source0_hash d5b79a488a88f4e4d04184efa0bc116929baf9b34617af70d8debfb37f7431f4

Name:           nq
Version:        1.0
Release:        %autorelease
Summary:        Unix command line queue utility

License:        CC0-1.0
URL:            https://github.com/leahneukirchen/nq
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl(Test::Harness)

Recommends:     (tmux or screen)

%description
The nq utility provides a very lightweight queuing system without requiring 
setup, maintenance, supervision or any long-running processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS='%{build_cflags}'

%check
%make_build check

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_bindir}/nqtail
%{_bindir}/nqterm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/nqtail.1*
%{_mandir}/man1/nqterm.1*

%changelog
%autochangelog
