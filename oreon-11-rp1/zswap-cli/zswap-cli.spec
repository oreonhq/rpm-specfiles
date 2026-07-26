%global source0_hash 74a3bd14b203eae824318d91fd7523439c0802a5df0ced5f6919ba09ba0750c0

Name: zswap-cli
Version: 1.1.2
Release: %autorelease

License: MIT
Summary: Command-line tool to control the zswap options
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: boost-devel
BuildRequires: glibc-headers
BuildRequires: kernel-headers

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: pandoc
BuildRequires: systemd

%{?systemd_requires}

%description
Zswap-cli is a command-line tool to control the zswap kernel module
options.

Zswap is a compressed cache for swap pages. It takes pages that are in the
process of being swapped out to disk and tries to compress them into a
RAM-based memory pool with dynamic allocation.

It trades CPU cycles for a significant performance boost since reading from
a compressed cache is much faster than reading from a swap device.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON \
    -DBUILD_SHELL_COMPLETION:BOOL=ON \
    -DSYSTEMD_INTEGRATION:BOOL=ON
%cmake_build

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%install
%cmake_install

%files
%doc docs/*
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{bash_completions_dir}/%{name}

%changelog
%autochangelog
