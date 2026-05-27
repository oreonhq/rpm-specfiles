%global source0_hash none

Name:tpm2-openssl
Version: 1.2.0
Release: 8%{?candidate:.%{candidate}}%{?dist}
Summary: Provider for integration of TPM 2.0 to OpenSSL 3.0

License: BSD-3-Clause
URL: https://github.com/tpm2-software/tpm2-openssl
Source0: https://github.com/tpm2-software/%{name}/%{?candidate:archive/refs/tags}%{!?candidate:releases/download}/%{version}%{?candidate:-%{candidate}}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz
Source1: https://github.com/tpm2-software/%{name}/%{?candidate:archive/refs/tags}%{!?candidate:releases/download}/%{version}%{?candidate:-%{candidate}}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz.asc
Source2: gpgkey-B7201FE8031B07AF11F5423C6329CFCB6BE6FD76.gpg
# Will be included in Source0 after https://github.com/tpm2-software/tpm2-openssl/pull/100
Source3: run-with-simulator

# https://bugzilla.redhat.com/show_bug.cgi?id=2301337
Patch1: 0001-tests-rsa_pki-default-to-sha256.patch
Patch2: 0002-tests-do-not-test-sha1-by-default.patch

BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: autoconf automake libtool autoconf-archive
BuildRequires: tpm2-tss-devel
BuildRequires: openssl-devel >= 3.0.0

# Test dependencies
BuildRequires: dbus-daemon
BuildRequires: iproute
BuildRequires: openssl
BuildRequires: procps-ng
BuildRequires: swtpm
BuildRequires: tpm2-abrmd tpm2-abrmd-selinux
BuildRequires: tpm2-tools


%description
Makes the TPM 2.0 accessible via the standard OpenSSL API and command line
tools, adding TPM support to (almost) any OpenSSL 3.0-based application.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

%build
%if "%{?candidate:true}" == "true"
  sed -e '/^git.*$/d' -i bootstrap
  echo "%{version}%{?candidate:-%{candidate}}" > VERSION
  ./bootstrap
%endif
%configure
%{make_build}

%check
cp %{SOURCE3} %{_builddir}/%{name}-%{version}%{?candidate:-%{candidate}}/test/
./test/run-with-simulator swtpm skip-build

%install
%make_install

%files
%doc docs
%license LICENSE
%{_libdir}/ossl-modules/tpm2.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-8
- Import
