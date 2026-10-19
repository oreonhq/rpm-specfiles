%global source2_hash b037f168f067bbe0a6a788f95cc145561ed7a280e336296e8176a09a8865a069
%global source1_hash 9b21cc1c45495553899f121b1abec9d46fc343076011cd7497a0b77ce525f0df
%global source0_hash 8cb376b14c44809750a41b74c239a47092edb8e496f657c38af9b852dd8e4ea4
%bcond check 0
Name:    newsboat
Version: 2.44
Release:        1%{?dist}
Summary:        RSS/Atom feed reader for the text console
License: MIT
URL:     https://www.newsboat.org
Source0:        https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://newsboat.org/newsboat.pgp
Patch:  0001-make-do-not-require-Cargo.lock.patch
Patch:  0002-libnewsboat-relax-requirements.patch
Patch:  0003-Do-not-build-http-test-server-by-default.patch
Obsoletes: newsbeuter < 2.9-29
Provides: podboat = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(stfl)
# /oreon:deps
%description
Newsboat is a fork of Newsbeuter, an RSS/Atom feed reader for the text console.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
# Note to self: do not use -S git_am for released builds, it messes up version string
%autosetup -p1

%build

%set_build_flags
export CFLAGS="-Wno-error ${CFLAGS}" CXXFLAGS="-Wno-error ${CXXFLAGS}"
export CARGO_BUILD_FLAGS="%{__cargo_common_opts}"
sh config.sh
%make_build CARGO="%{__cargo}" all %{?with_check:test}
%install
%make_install prefix="%{_prefix}"
find %{buildroot}%{_pkgdocdir}/ -type f -exec chmod -x '{}' +
%find_lang %{name}
%oreon_autofiles main

%check

%if %{with check}
%cargo_test
%endif
%{buildroot}%{_bindir}/newsboat --version|sed 1q|grep -v dirty
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
