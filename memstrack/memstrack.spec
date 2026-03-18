# vim: syntax=spec
%global gitcommit 560379ee67db48382ccc3ab3de866e239fd74ca8
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           memstrack
Version:        0.2.5
Release:        8%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPL-3.0-only
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/%{gitcommit}/memstrack-%{gitshortcommit}.tar.gz

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%setup -q -n memstrack-%{gitcommit}

%build
%{set_build_flags}
%{make_build}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.5-8
- Prepare for Oreon 11 (RP1)
