%global source0_hash 0c3ee7214e81c6ba506c1886a110d5406ee080d49a17c1e7e673b62b28b213d6

Name:       smatch
Version:    1.74
Release:    1%{?dist}
Summary:    A static analyzer for C

# License breakdown:
# - Smatch itself is GPL-2.0-or-later
# - Sparse is MIT
# - cwchash is BSD-3-clause
License:    GPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:        https://%{name}.sourceforge.net

# Upstream is https://repo.or.cz/w/smatch.git, but it does not allow an easy
# download of tarballs so we use an official GitHub mirror instead.
Source0:    https://github.com/error27/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:     do-not-build-sparse-binaries.patch
# TODO: Try to upstream these patches.
Patch1:     fix-datadir-path.patch
Patch2:     use-distribution-ldflags.patch
Patch3:     preserve-install-timestamps.patch
# TODO: File an issue upstream about the missing license.
Patch4:     add-BSD-3-license.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: sqlite-devel

Requires: %{name}-data = %{version}-%{release}

Provides: bundled(cwchash)
Provides: bundled(sparse)

%description
Smatch is a static analysis tool for C.

%package data
Summary: Data for Smatch the C static analyzer
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description data
Data for Smatch the static analysis tool for C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%if 0%{?rhel}
%set_build_flags
%endif
%make_build PREFIX='%{_prefix}'

%install
%make_install PREFIX='%{_prefix}'

%check
echo 'int main(void) { int a[2]; return a[2]; }' > test.c
./smatch test.c 2>&1 | tee out
grep "test.c:1 main() error: buffer overflow 'a' 2 <= 2" out

%files
%doc README Documentation/{arm64-detecting-tagged-addresses,smatch}.txt
%license GPL-2 LICENSE
%{_bindir}/%{name}

%files data
%{_datadir}/%{name}

%changelog
%autochangelog
