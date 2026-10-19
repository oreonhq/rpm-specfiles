%global source0_hash c01b471d89eda9f3c8dcb85a448e8066692d0707f9ff8b2ac7e665a602291b87
Name:              torsocks
Version:           2.4.0
Release:        1%{?dist}
Summary:        Use SOCKS-friendly applications with Tor
License:           GPL-2.0-or-later
URL:               https://gitweb.torproject.org/torsocks.git
Source0:        https://gitlab.torproject.org/tpo/core/%{name}/-/archive/v2.4.0/%{name}-v%{version}.tar.gz
Patch0:            %{name}-2.2.0-Do-not-run-tests-that-require-network-access.patch
Patch1:            torsocks-c99.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Torsocks allows you to use most SOCKS-friendly applications in a safe way
with Tor. It ensures that DNS requests are handled safely and explicitly
rejects UDP traffic from the application you're using.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

./autogen.sh
%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/torsocks/libtorsocks.{a,la}*
rm -fr %{buildroot}%{_datadir}/doc/torsocks
install -p -D -m0644 extras/torsocks-bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/torsocks
%oreon_autofiles main

%check

pushd tests/
make check-am
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
