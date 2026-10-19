%global source10_hash e5af06d7b737b66f7476a223e8a6cd1e2b1ca834b38b3de58901d4dbcf0a054d
%global source2_hash d090228efe3f86ba7aba1b6fc29de16d81e968dfbc1bcccc9249abcbf66da04d
%global source1_hash 328dfc22d4e7e3ca9d4378fe5588d3e1b7a45efc1902e5c14cad09f6f29abd53
%global source0_hash fc9165f733a0e28a3dba11c9b1a286bc88a853f152a6694cd993512a2f1761aa
%global version_base 4.6.0
%dnl %global version_pre beta.1
%dnl %global gitnum 1
%dnl %global githash b82d0fcbcc44eb259cf2209b04f7a41c1f324e27
%dnl %global githashshort %{lua:print(string.sub(rpm.expand('%{githash}'), 1, 11))}
%global rust_pcre2_fish_tag 0.2.9-utf32
Name:           fish
Version:        %{version_base}%{?version_pre:~%{version_pre}}%{?gitnum:^git%{gitnum}.%{githashshort}}
Release:        1%{?dist}
Summary:        Friendly interactive shell
License:        Apache-2.0 OR MIT and GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0 and Unlicense OR MIT and WTFPL and Zlib
URL:            https://fishshell.com
%if %{undefined gitnum}
Source0:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://github.com/krobelus.gpg
%else
%endif
Source10:       https://github.com/fish-shell/rust-pcre2/archive/%{rust_pcre2_fish_tag}/rust-pcre2-%{rust_pcre2_fish_tag}.tar.gz
Patch1001:      1001-cargo-Use-internal-copy-of-rust-pcre2-instead-of-fet.patch
Patch1002:      1002-cmake-Use-rpm-profile-for-RelWithDebInfo.patch
Patch1003:      1003-cargo-Drop-unneeded-dependency-on-unix_path.patch
Patch10001:     10001-rust-pcre2-cargo-Drop-workspace-definition.patch
Patch10002:     10002-tests-Raise-the-default-timeout-for-pexpect-tests.patch
%global __python %{__python3}
Requires:       ncurses-term
Recommends:     man-db
Recommends:     man-pages
Recommends:     groff-base
Provides:       bundled(js-alpine)
Provides:       bundled(crate(pcre2)) = %{rust_pcre2_fish_tag}
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glibc-langpack-en
BuildRequires:  gnupg2
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  pcre2-devel
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-pexpect
BuildRequires:  rust
# /oreon:deps
%description
fish is a fully-equipped command line shell (like bash or zsh) that is
smart and user-friendly. fish supports powerful features like syntax
highlighting, autosuggestions, and tab completions that just work, with
nothing to learn or configure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{undefined gitnum}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -N %{?gitnum:-n fish-shell-%{githash}}

# For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
mkdir -p ./third-party-forks/rust-pcre2
tar -C ./third-party-forks/rust-pcre2 --strip-components=1 -xf %{SOURCE10}

%autopatch -p1

%if %{defined gitnum}
echo "%{version}" > version
%endif

# Change the bundled scripts to invoke the python binary directly.
for f in $(find share/tools -type f -name '*.py'); do
    sed -i -e '1{s@^#!.*@#!%{__python3}@}' "$f"
done

# Do horrible things in our quest to have fish work properly
mv .cargo/config.toml fishshell-cargo-config.toml
cat fishshell-cargo-config.toml >> .cargo/config.toml

%build

export CARGO_NET_OFFLINE=true
mkdir -p %{_vpath_builddir}
%cmake_build
sed -i 's^/usr/local/^/usr/^g' %{_vpath_builddir}/*.pc
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cmake_install
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/tools/
cp -a README.rst %{buildroot}%{_pkgdocdir}
cp -a CONTRIBUTING.rst %{buildroot}%{_pkgdocdir}
%oreon_autofiles main

%check

export CI=1
%cmake_build --target fish_run_tests
%post

if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/fish" > %{_sysconfdir}/shells
    echo "/bin/fish" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/fish$" %{_sysconfdir}/shells || echo "%{_bindir}/fish" >> %{_sysconfdir}/shells
    grep -q "^/bin/fish$" %{_sysconfdir}/shells || echo "/bin/fish" >> %{_sysconfdir}/shells
  fi
fi
%postun

if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/fish$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/fish$!d' %{_sysconfdir}/shells
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
