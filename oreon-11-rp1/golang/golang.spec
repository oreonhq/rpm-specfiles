%global source0_hash 4e408abae126d916b6164627193f2c54f0e3ca1312d693b86db45f862ab238b1
%bcond_with bootstrap
%bcond_with dwarf5
%global debug_package %{nil}
%global _binaries_in_noarch_packages_terminate_build 0
%global __requires_exclude_from ^(%{_datadir}|/usr/lib)/%{name}/(doc|src)/.*$
%global __strip /bin/true
%define _use_internal_dependency_generator 0
%define __find_requires %{nil}
%global __spec_install_post /usr/lib/rpm/check-rpaths   /usr/lib/rpm/check-buildroot  \
  /usr/lib/rpm/brp-compress
%global golibdir %{_libdir}/golang
%{!?gopath: %global gopath %{_datadir}/gocode}
%ifarch %{ix86} x86_64 ppc64le %{arm} aarch64 s390x riscv64 loongarch64
%global external_linker 1
%else
%global external_linker 0
%endif
%ifarch %{ix86} x86_64 ppc64le %{arm} aarch64 s390x riscv64 loongarch64
%global cgo_enabled 1
%else
%global cgo_enabled 0
%endif
%if %{with bootstrap}
%global golang_bootstrap 0
%else
%global golang_bootstrap 1
%endif
%if %{with ignore_tests}
%global fail_on_tests 0
%else
%global fail_on_tests 1
%endif
%ifarch %{ix86} x86_64 ppc64le %{arm} aarch64
%global shared 1
%else
%global shared 0
%endif
%global race 0
%global goroot          /usr/lib/%{name}
%ifarch x86_64
%global gohostarch  amd64
%endif
%ifarch %{ix86}
%global gohostarch  386
%endif
%ifarch %{arm}
%global gohostarch  arm
%endif
%ifarch aarch64
%global gohostarch  arm64
%endif
%ifarch ppc64
%global gohostarch  ppc64
%endif
%ifarch ppc64le
%global gohostarch  ppc64le
%endif
%ifarch s390x
%global gohostarch  s390x
%endif
%ifarch riscv64
%global gohostarch  riscv64
%endif
%ifarch loongarch64
%global gohostarch  loong64
%endif
%global go_api 1.27
%global go_patch 1
%global go_version %{go_api}%{?go_patch:.%{go_patch}}%{?go_prerelease:~%{go_prerelease}}
%global go_source %{go_api}%{?go_patch:.%{go_patch}}%{?go_prerelease}
Name:           golang
Version:        %{go_version}
Release:        1%{?dist}
Summary:        The Go Programming Language
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://go.dev
Source0:        https://go.dev/dl/go%{version}.src.tar.gz
Source1:        fedora.go
%if !%{golang_bootstrap}
%else
%endif
Provides:       go = %{version}-%{release}
Provides: bundled(golang(github.com/google/pprof)) = 0.0.0.20260507013755.92041b743c96
Provides: bundled(golang(github.com/ianlancetaylor/demangle)) = 0.0.0.20250417193237.f615e6bd150b
Provides: bundled(golang(golang.org/x/arch)) = 0.27.1.0.20260521044007.9c1a596a2c97
Provides: bundled(golang(golang.org/x/build)) = 0.0.0.20260522210304.d55d0041b921
Provides: bundled(golang(golang.org/x/crypto)) = 0.52.1.0.20260526024921.9beb694f9766
Provides: bundled(golang(golang.org/x/mod)) = 0.36.1.0.20260813213634.8569e2639ca1
Provides: bundled(golang(golang.org/x/net)) = 0.55.1.0.20260731170536.c1d18010be90
Provides: bundled(golang(golang.org/x/sync)) = 0.20.0
Provides: bundled(golang(golang.org/x/sys)) = 0.45.0
Provides: bundled(golang(golang.org/x/telemetry)) = 0.0.0.20260519152614.eab6ae52b5e2
Provides: bundled(golang(golang.org/x/term)) = 0.43.0
Provides: bundled(golang(golang.org/x/text)) = 0.37.0
Provides: bundled(golang(golang.org/x/tools)) = 0.27.0
Provides: bundled(golang(golang.org/x/tools)) = 0.45.1.0.20260826175739.e1f45aa8aed5
Provides: bundled(golang(rsc.io/markdown)) = 0.0.0.20240306144322.0bf8f97ee8ef
Requires:       %{name}-bin = %{version}-%{release}
Requires:       %{name}-src = %{version}-%{release}
Requires:       go-filesystem
Patch1:         0001-Modify-go.env.patch
Patch5:         0005-Skip-TestCrashDumpsAllThreads.patch
Patch8:         fix_cgo_panic-with-gcc15-in-368.patch
Patch9:         skip_lsan_tests.patch
Obsoletes:      %{name}-docs < 1.1-4
Obsoletes:      %{name}-data < 1.1.1-4
Obsoletes:      %{name}-vim < 1.4
Obsoletes:      emacs-%{name} < 1.4
Obsoletes:      golang-race < 1.20~rc3-2
ExclusiveArch:  %{golang_arches}
Source100:      golang-gdbinit
# oreon:deps
BuildRequires:  gcc-go
BuildRequires:  glibc-static
BuildRequires:  hostname
BuildRequires:  pcre2-devel
# /oreon:deps
%description
%{summary}.

%package       docs
Summary:       Golang compiler docs
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
Obsoletes:     %{name}-docs < 1.1-4
%description   docs
%{summary}.

%package       misc
Summary:       Golang compiler miscellaneous sources
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
%description   misc
%{summary}.

%package       tests
Summary:       Golang compiler tests for stdlib
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
%description   tests
%{summary}.

%package        src
Summary:        Golang compiler source tree
BuildArch:      noarch
%description    src
%{summary}

%package        bin
Summary:        Golang core compiler tools
Provides:       %{name}-go = %{version}-%{release}
Requires:       go = %{version}-%{release}
Obsoletes:      %{name}-pkg-bin-linux-386 < 1.4.99
Obsoletes:      %{name}-pkg-bin-linux-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-bin-linux-arm < 1.4.99
Obsoletes:      %{name}-pkg-linux-386 < 1.4.99
Obsoletes:      %{name}-pkg-linux-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-linux-arm < 1.4.99
Obsoletes:      %{name}-pkg-darwin-386 < 1.4.99
Obsoletes:      %{name}-pkg-darwin-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-windows-386 < 1.4.99
Obsoletes:      %{name}-pkg-windows-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-plan9-386 < 1.4.99
Obsoletes:      %{name}-pkg-plan9-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-freebsd-386 < 1.4.99
Obsoletes:      %{name}-pkg-freebsd-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-freebsd-arm < 1.4.99
Obsoletes:      %{name}-pkg-netbsd-386 < 1.4.99
Obsoletes:      %{name}-pkg-netbsd-amd64 < 1.4.99
Obsoletes:      %{name}-pkg-netbsd-arm < 1.4.99
Obsoletes:      %{name}-pkg-openbsd-386 < 1.4.99
Obsoletes:      %{name}-pkg-openbsd-amd64 < 1.4.99
Obsoletes:      golang-vet < 0-12.1
Obsoletes:      golang-cover < 0-12.1
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives
Requires:       glibc
Requires:       gcc
Recommends:     git-core
%description    bin
%{summary}

# Workaround old RPM bug of symlink-replaced-with-dir failure
%pretrans -p <lua>

for _,d in pairs({"api", "doc", "include", "lib", "src"}) do
  path = "%{goroot}/" .. d
  if posix.stat(path, "type") == "link" then
    os.remove(path)
    posix.mkdir(path)
  end
end
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n go

cp %{SOURCE1} ./src/runtime/

%if %{with dwarf5}
sed -i '/^GOEXPERIMENT=nodwarf5$/d' go.env
%endif

%build

uname -a
cat /proc/cpuinfo
cat /proc/meminfo
%if !%{golang_bootstrap}
export GOROOT_BOOTSTRAP=/
%else
export GOROOT_BOOTSTRAP=%{goroot}
%endif
export GOROOT_FINAL=%{goroot}
export GOHOSTOS=linux
export GOHOSTARCH=%{gohostarch}
pushd src
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
export CC="gcc"
export CC_FOR_TARGET="gcc"
export GOOS=linux
export GOARCH=%{gohostarch}
%if !%{external_linker}
export GO_LDFLAGS="-linkmode internal"
%endif
%if !%{cgo_enabled}
export CGO_ENABLED=0
%endif
./make.bash -v
popd
%install
echo "== 1 =="
rm -rf $RPM_BUILD_ROOT
rm -rf pkg/obj/go-build/*
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{goroot}
cp -apv api bin doc lib pkg src misc test go.env VERSION \
   $RPM_BUILD_ROOT%{goroot}
echo "== 2 =="
find $RPM_BUILD_ROOT%{goroot}/src -exec touch -r $RPM_BUILD_ROOT%{goroot}/VERSION "{}" \;
touch $RPM_BUILD_ROOT%{goroot}/pkg
find $RPM_BUILD_ROOT%{goroot}/pkg -exec touch -r $RPM_BUILD_ROOT%{goroot}/pkg "{}" \;
cwd=$(pwd)
src_list=$cwd/go-src.list
pkg_list=$cwd/go-pkg.list
shared_list=$cwd/go-shared.list
race_list=$cwd/go-race.list
misc_list=$cwd/go-misc.list
docs_list=$cwd/go-docs.list
tests_list=$cwd/go-tests.list
rm -f $src_list $pkg_list $docs_list $misc_list $tests_list $shared_list $race_list
touch $src_list $pkg_list $docs_list $misc_list $tests_list $shared_list $race_list
pushd $RPM_BUILD_ROOT%{goroot}
  echo "== 3 =="
    find src/ -type d -a \( ! -name testdata -a ! -ipath '*/testdata/*' \) -printf '%%%dir %{goroot}/%p\n' >> $src_list
    find src/ ! -type d -a \( ! -ipath '*/testdata/*' -a ! -name '*_test.go' \) -printf '%{goroot}/%p\n' >> $src_list
    find bin/ pkg/ -type d -a ! -path '*_dynlink/*' -a ! -path '*_race/*' -printf '%%%dir %{goroot}/%p\n' >> $pkg_list
    find bin/ pkg/ ! -type d -a ! -path '*_dynlink/*' -a ! -path '*_race/*' -printf '%{goroot}/%p\n' >> $pkg_list
    find doc/ -type d -printf '%%%dir %{goroot}/%p\n' >> $docs_list
    find doc/ ! -type d -printf '%{goroot}/%p\n' >> $docs_list
    find misc/ -type d -printf '%%%dir %{goroot}/%p\n' >> $misc_list
    find misc/ ! -type d -printf '%{goroot}/%p\n' >> $misc_list
echo "== 5 =="
    find test/ -type d -printf '%%%dir %{goroot}/%p\n' >> $tests_list
    find test/ ! -type d -printf '%{goroot}/%p\n' >> $tests_list
    find src/ -type d -a \( -name testdata -o -ipath '*/testdata/*' \) -printf '%%%dir %{goroot}/%p\n' >> $tests_list
    find src/ ! -type d -a \( -ipath '*/testdata/*' -o -name '*_test.go' \) -printf '%{goroot}/%p\n' >> $tests_list
    find lib/ -type d -printf '%%%dir %{goroot}/%p\n' >> $tests_list
    find lib/ ! -type d -printf '%{goroot}/%p\n' >> $tests_list
popd
echo "== 6 =="
rm -rfv $RPM_BUILD_ROOT%{goroot}/doc/Makefile
mkdir -p $RPM_BUILD_ROOT%{goroot}/bin/linux_%{gohostarch}
ln -sf %{goroot}/bin/go $RPM_BUILD_ROOT%{goroot}/bin/linux_%{gohostarch}/go
ln -sf %{goroot}/bin/gofmt $RPM_BUILD_ROOT%{goroot}/bin/linux_%{gohostarch}/gofmt
echo "== 7 =="
rm -f $RPM_BUILD_ROOT%{_bindir}/go
ln -sf /etc/alternatives/go $RPM_BUILD_ROOT%{_bindir}/go
rm -f $RPM_BUILD_ROOT%{_bindir}/gofmt
ln -sf /etc/alternatives/gofmt $RPM_BUILD_ROOT%{_bindir}/gofmt
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
cp -av %{SOURCE100} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d/golang.gdb
echo "== END OF INSTALL =="
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export GOROOT=$(pwd -P)
export PATH="$GOROOT"/bin:"$PATH"
cd src
export CC="gcc"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
%if !%{external_linker}
export GO_LDFLAGS="-linkmode internal"
%endif
%if !%{cgo_enabled} || !%{external_linker}
export CGO_ENABLED=0
%endif
%ifnarch riscv64
export GO_TEST_TIMEOUT_SCALE=2
%else
export GO_TEST_TIMEOUT_SCALE=20
%endif
./run.bash --no-rebuild -v -v -v -k
cd ..
%post bin

%{_sbindir}/update-alternatives --install %{_bindir}/go \
    go %{goroot}/bin/go 90 \
    --slave %{_bindir}/gofmt gofmt %{goroot}/bin/gofmt
%preun bin

if [ $1 = 0 ]; then
    %{_sbindir}/update-alternatives --remove go %{goroot}/bin/go
fi
%files -f %{oreon_filedir}/main.list
%files -n golang-docs -f %{oreon_filedir}/golang-docs.list
%files -n golang-misc -f %{oreon_filedir}/golang-misc.list
%files -n golang-tests -f %{oreon_filedir}/golang-tests.list
%files -n golang-src -f %{oreon_filedir}/golang-src.list
%files -n golang-bin -f %{oreon_filedir}/golang-bin.list

%changelog

%autochangelog
