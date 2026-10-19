%global source0_hash ad5d01bb4c91ff274a8333cbad06da2c15fd637db4954bf3c69572245a54f19b
%global source1_hash none
%global source2_hash none
%global     npm_name undici
%bcond      wasm_opt %[0%{?fedora} > 39]
%global     llhttp_version_major    9
%global     llhttp_version_minor    3
%global     llhttp_version_patch    0
Name:       nodejs-%{npm_name}
Summary:        An HTTP/1.1 client, written from scratch for Node.js
Version:    8.10.2
Release:        1%{?dist}
License:    MIT
URL:        https://undici.nodejs.org
Source0:        https://github.com/nodejs/undici/archive/v7.24.0/undici-v7.24.0.tar.gz#/nodejs-undici-7.24.0.tar.gz
Source3:    %{npm_name}-%{version}-bundled-licenses.txt
Source4:    %{npm_name}-sources.sh
Source5:        test-runner.sh
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 aarch64 ppc64le riscv64 noarch
%if %{with wasm_opt}
%endif
Provides:   bundled(llhttp) = %{llhttp_version_major}.%{llhttp_version_minor}.%{llhttp_version_patch}
# oreon:deps
BuildRequires:  /usr/bin/npm
BuildRequires:  binaryen
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  lld
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging-bundler
BuildRequires:  npm
BuildRequires:  wasi-libc-devel
# /oreon:deps
%description
An HTTP/1.1 client, written from scratch for Node.js.

%prep

_nm1="%{npm_name}-%{version}-nm-prod.tgz"
_nm2="%{npm_name}-%{version}-nm-dev.tgz"
if test ! -f "$_nm1" || test ! -f "$_nm2"; then
  nodejs-packaging-bundler %{npm_name} %{version} %{SOURCE0}
fi
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{npm_name}-%{version} -S git_am
cp -p %{S:3} .

# Check for bundled llhttp version
if ! grep -q 'LLHTTP_VERSION_MAJOR %{llhttp_version_major}' deps/llhttp/include/llhttp.h \
|| ! grep -q 'LLHTTP_VERSION_MINOR %{llhttp_version_minor}' deps/llhttp/include/llhttp.h \
|| ! grep -q 'LLHTTP_VERSION_PATCH %{llhttp_version_patch}' deps/llhttp/include/llhttp.h
then
    echo 'llhttp version mismatch' >&2; exit 2
fi

# Link node_modules
mkdir -p node_modules/.bin/
tar -xzf "$_nm1"
ln -srt node_modules/       node_modules_prod/*
ln -srt node_modules/.bin/  node_modules_prod/.bin

%build

export WASM_CC=clang
export WASM_CFLAGS='--target=wasm32-wasi --sysroot=/usr/wasm32-wasi'
export WASM_LDFLAGS='-nodefaultlibs'
export WASM_LDLIBS='-lc'
%if %{with wasm_opt}
export WASM_OPT=/usr/bin/wasm-opt
%endif
env EXTERNAL_PATH='%{nodejs_sitelib}/%{npm_name}' %{__nodejs} build/wasm.js
npm --offline pack
%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
tar -C   %{buildroot}%{nodejs_sitelib}/%{npm_name} -xzf %{npm_name}-%{version}.tgz --strip-components=1
cp -prt  %{buildroot}%{nodejs_sitelib}/%{npm_name} node_modules_prod node_modules
install -p -Dt %{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/llhttp/ lib/llhttp/*.wasm lib/llhttp/*.js
install -p -Dt %{buildroot}%{nodejs_sitelib}/%{npm_name}/            loader.js
%oreon_autofiles main

%check

%{__nodejs} -e 'require("./")'
tar -xzf "$_nm2"
ln -fsrt node_modules/      node_modules_dev/*
ln -fsrt node_modules/.bin/ node_modules_dev/.bin/*
bash %{S:5} || exit
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.24.0-1
- Import
