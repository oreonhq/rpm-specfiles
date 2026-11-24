# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5dc2d15f65c031e963e653409de52ce50223df0db32c43811addcbe03024283a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gitcommit 560379ee67db48382ccc3ab3de866e239fd74ca8
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           memstrack
Version:        0.2.5
Release:        1%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPL-3.0-only
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires: oreon-rpm-macros
BuildRequires:  make
BuildRequires:  clang
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/%{gitcommit}/memstrack-%{gitshortcommit}.tar.gz

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%oreon_sha256
%setup -q -n memstrack-%{gitcommit}

%build
%{set_build_flags}
%{make_build} CC=%{__cc}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
%autochangelog
