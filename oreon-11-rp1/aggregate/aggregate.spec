%global source0_hash 166503005cd8722c730e530cc90652ddfa198a25624914c65dffc3eb87ba5482

Name:           aggregate
Version:        1.6
Release:        35%{?dist}
Summary:        IPv4 CIDR prefix aggregator

License:        ISC
URL:            http://ftp.isc.org/isc/aggregate/
Source0:        http://ftp.isc.org/isc/aggregate/aggregate-%{version}.tar.gz
Patch0:         aggregate-fedora.patch
Patch1:         aggregate-configure-c99.patch

BuildRequires:         gcc
BuildRequires:         perl-generators
BuildRequires: make

%description
aggregate takes a list of prefixes in conventional format on stdin, 
and performs two optimizations to attempt to reduce the length of 
the prefix list.

%package ios
Summary: Cisco/IOS IPv4 prefix lists aggregator
Requires: aggregate
BuildArch: noarch

%description ios
aggregate-ios takes Cisco IOS configuration on stdin, and optimizes 
any prefix filters found using aggregate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
chmod -x LICENSE

%build
%configure
%make_build

%install
%make_install

%files
%doc HISTORY
%license LICENSE
%{_bindir}/aggregate
%{_mandir}/man1/aggregate.1.*

%files ios
%{_bindir}/aggregate-ios
%{_mandir}/man1/aggregate-ios.1.*

%changelog
%autochangelog
