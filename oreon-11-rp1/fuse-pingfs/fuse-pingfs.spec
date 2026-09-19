%global source0_hash 88b5fea5a1292d729602a73d3f807353bb1e631467cc7c2e8cdf355e09971ba4

%global srcname pingfs
%global commit f2f2b5ff1893d0531d0a0d1ea2ae96b52dcf780e
%global snapinfo 20200820git%{shortcommit}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    fuse-pingfs
Version: 0
Release: 0.14.%{snapinfo}%{?dist}
Summary:  Stores your data in ICMP ping packets

License: ISC
URL:     https://github.com/yarrick/pingfs
Source0: https://github.com/yarrick/pingfs/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(fuse)
BuildRequires: make

%description
pingfs is a filesystem where the data is stored only in the Internet itself, as
ICMP Echo packets (pings) travelling from you to remote servers and back again.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pingfs-%{commit}

%build
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a pingfs %{buildroot}%{_bindir}/pingfs

%files
%{_bindir}/pingfs

%doc README
%license LICENSE

%changelog
%autochangelog
