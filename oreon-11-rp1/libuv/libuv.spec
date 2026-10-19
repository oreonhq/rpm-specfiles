%global source1_hash 65ca5d646db151e403d9271202c609ff72c41781285bae310e635a90f7e28d08
%global source0_hash cb0d6dd2128d5a95bd242c6cc982a24fe608fa93da57b6b4ec763b0018c53e64
%global source2_key_fpr 612F0EAD9401622379DF4402F28C3C8DA33C03BE
%bcond tests 1
Name:           libuv
Epoch:          1
Version:        1.53.0
Release:        1%{?dist}
Summary:        Platform layer for node.js
License:        MIT AND CC-BY-4.0 AND ISC AND BSD-2-Clause
URL:            http://libuv.org/
Source0:        http://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz
Source1:        https://dist.libuv.org/dist/v%{version}/%{name}-v%{version}.tar.gz.sign
Source2:        keysuv.gpg
Source3:        libuv.abignore
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(sphinx-copybutton)
# /oreon:deps
%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on
Windows and libev on Unix systems. We intend to eventually contain all platform
differences in this library.

%package devel
Summary:        Development libraries for libuv
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Development libraries for libuv

%package static
Summary:        Platform layer for node.js - static library
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
%description static
Static library (.a) version of libuv.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -n %{name}-v%{version} -p1

%build

%if %{with tests}
%cmake -DBUILD_TESTING=ON
%else
%cmake -DBUILD_TESTING=OFF
%endif
%cmake_build
cd docs
make man
cd ..
%install
%cmake_install
mkdir -p  %{buildroot}/%{_mandir}/man1/
install -p -m 644 docs/build/man/libuv.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}%{_libdir}/libuv/
install -Dm0644 -t %{buildroot}%{_libdir}/libuv/ %{SOURCE3}
rm %{buildroot}/%{_docdir}/libuv/LICENSE
rm %{buildroot}/%{_docdir}/libuv/LICENSE-extra
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%if %{with tests}
env UV_TEST_TIMEOUT_MULTIPLIER=10 ./%{__cmake_builddir}/uv_run_tests
env UV_TEST_TIMEOUT_MULTIPLIER=10 ./%{__cmake_builddir}/uv_run_tests_a
%endif
%files -f %{oreon_filedir}/main.list
%files -n libuv-devel -f %{oreon_filedir}/libuv-devel.list
%files -n libuv-static -f %{oreon_filedir}/libuv-static.list

%changelog

%autochangelog
